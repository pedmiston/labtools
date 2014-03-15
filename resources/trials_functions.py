#!/usr/bin/env python
"""
resources.trials_functions
"""
import pandas as pd
import numpy as np
import itertools as itls
from copy import copy
from exceptions import AssertionError

def counterbalance(conditions, order=None):
    """
    Generate all independent variable combinations in a DataFrame.
    
    Each row of the resulting DataFrame contains a unique combination of 
    conditions. Use primarily for full counterbalancing of within-subject 
    variables.
    
    :param conditions: dict. Variable names and possible values.
    :param order: list, optional. Order of columns in output.
    :return: pandas.DataFrame. Each row is a unique combination of variables, 
             assuming the possible values for each variable are unique.
    """
    for k,v in conditions.items():
        if not hasattr(v, '__iter__'):
            conditions[k] = [v]
    
    combinations = list(itls.product(*conditions.values()))
    frame = pd.DataFrame(combinations, columns=conditions.keys())
    
    if order is None:
        order = frame.columns
    
    return frame[order]
    
def expand(valid, name, values=[1.,0.], ratio=0.5, sample=False, seed=None):
    """
    Copy rows as necessary to satisfy the valid:invalid ratio.
        
    Use when complete counterbalancing is not plausible. For example, when the 
    ratio of trials requiring response A to those requiring response B is not
    50:50.
    
    :param valid: pandas.DataFrame. Trials to be expanded.
    :param name: str. Name of new column containing valid and invalid values
    :param values: list of length 2. Values for valid and invalid trials, 
                   respectively.
    :param ratio: 0.0 < float < 1.0. Approximate percentage of valid trials in 
                  the resulting frame.
    :param sample: bool, default False. Should the invalid trials be sampled 
        from the valid trials? If True, len(returned) < 2*len(valid).
    :param seed: float, optional. If sample is True, seed for random sampling 
                 of invalid trials.
    :return: pandas.DataFrame. Valid and invalid trials are denoted in a new 
             column.
    """
    prng = np.random.RandomState(seed)
    num_trials = len(valid)
    
    if not sample:
        invalid = valid[:]
        num_valid = (num_trials*ratio)/(1.0-ratio)
        copies = int(num_valid/num_trials)
        valid = pd.concat([valid]*copies, ignore_index=True)
    else:
        num_invalid = int((num_trials*(1.0-ratio))/ratio)
        sampled = prng.choice(valid.index, num_invalid, replace=False)
        invalid = valid.reindex(sampled).reset_index(drop=True)
    
    frame = pd.concat([valid, invalid], keys=values, names=[name,'DEFAULT'])
    frame = frame.reset_index().drop('DEFAULT', axis=1)
    return frame
    
def extend(frame, reps=None, max_length=None, rep_ix=None, row_ix=None):
    """
    Duplicates the unique trials for a total length less than the provided max.
    
    :param frame: pandas.DataFrame. Trials to be extended.
    :param reps: int, optional. Number of times to copy the frame.
    :param max_length: int, optional. Alternately, specify a max number of 
                       trials.
    :param rep_ix: str, optional. Column name for the iteration of repetitions.
    :param row_ix: str, optional. Column name for the row identification, which
                   is the original index of frame.
    :returns: pandas.DataFrame of duplicated trials
    """
    
    reps = reps or max_length/len(frame)
    
    if reps < 1:
        reps = 1
    
    col_names = [rep_ix or 'DEFAULT1', row_ix or 'DEFAULT2']
    
    to_drop = ['DEFAULT1', 'DEFAULT2']
    if rep_ix is not None:
        to_drop.remove('DEFAULT1')
    if row_ix is not None:
        to_drop.remove('DEFAULT2')
    
    repeated = pd.concat([frame]*reps, keys=range(1,reps+1), names=col_names).reset_index()
    return repeated.drop(to_drop, axis=1)

def add_block(frame, block_size, id_col=None, seed=None):
    """
    Creates a new column for block.
        
        frame --> pandas.DataFrame of trials
        block_size --> int number of trials in each block
        id_col --> str column name; chunk frame by column before assignment
        seed --> int seed for assignment shuffling
        ------------------------
        returns pandas.DataFrame
    """
    def _assigner(blocks, prng):
        prng.shuffle(blocks)
        i = 0
        while True:
            yield blocks[i]
            if (i+1)%len(blocks):
                prng.shuffle(blocks)
            i = (i+1)%len(blocks)
            
    prng = np.random.RandomState(seed)
    blocks = range(len(frame)/block_size)
    assigner = _assigner(blocks, prng)
    
    def _add(chunk):
        chunk['block'] = [assigner.next() for _ in xrange(len(chunk))]
        return chunk
    
    if id_col is None:
        return _add(frame).sort('block')
    else:
        return frame.groupby(id_col).apply(_add).sort('block')
                
def smart_shuffle(frame, col, block=None, seed=None, verbose=True, lim=10000):
    """
    Shuffles trials such that equivalent trials never appear back to back.
        
        frame --> pandas.DataFrame of trials
        id_col --> str column name; column to ensure non-repeating trials
        block --> str column name; chunk frame by block before shuffling
        seed --> int seed; for shuffling order
        ------------------------
        returns pandas.DataFrame
    """
    prng = np.random.RandomState(seed)
        
    def _shuffle(chunk):
        orig_index = chunk.index
        repeats = None
        for i in xrange(lim):
            new = chunk.reindex(prng.permutation(chunk.index))
            r = (new[col][1:]==new[col][:-1]).sum()
            if repeats is None or r < repeats:
                repeats = r
                chunk = new
            if repeats == 0:
                break
        if i==lim-1 and verbose:
            print 'Iteration limit reached! Minimum repeats: ', str(repeats)
        
        chunk.index = orig_index
        return chunk
    
    if block is None:
        return _shuffle(frame)
    else:
        return frame.groupby(block).apply(_shuffle)
        
def simple_shuffle(frame, block=None, times=10, seed=None):
    """
    Shuffles trials a few times.
    
        frame --> pandas.DataFrame of trials
        block --> str column name; shuffle trials in groups
        times --> int number of shuffles
        seed --> int seed; for shuffling order
        ------------------------
        returns pandas.DataFrame
    """
    prng = np.random.RandomState(seed)
    
    def _shuffle(chunk):
        for _ in range(times):
            chunk = chunk.reindex(prng.permutation(chunk.index))
        return chunk
    
    if block is None:
        return _shuffle(frame)
    else:
        return frame.groupby(block).apply(_shuffle)
