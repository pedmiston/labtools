#!/usr/bin/env python
# encoding: utf-8
"""
generateTrialsFunctions.py

Created by Pierce Edmiston on 2013-09-07.
"""
import pandas as pd
import numpy as np

def counterbalance(conditions):
    """
    Generates all possible independent variable combinations.
    
    Used primarily for full counterbalancing of within-subject variables; e.g.
    {'condition':[1,2,3], 'response':['right','left']}. Each row of the 
    resulting pandas.DataFrame contains a unique combination of conditions.
    
        conditions --> dict of conditions
        ------------------------
        returns pandas.DataFrame
    """
    import itertools as itls
    trials = list(itls.product(*conditions.values()))
    return pd.DataFrame(trials, columns=conditions.keys())
    
def expand(valid, ids, ratio=0.5, force=False, seed=None):
    """
    Duplicates invalid trials as necessary to satisfy the valid:invalid ratio.
        
    Used when complete counterbalancing is not plausible. For example, when the 
    ratio of trials requiring response A to those requiring response B is not
    50:50.
    
        valid --> pandas.DataFrame; valid trials not altered by method
        ids --> list of length 2; names for the ID columns.
        ratio --> 0.5 <= float < 1.0; % of valid trials in the resulting frame
        force --> bool; forces the ratio value
        seed --> int seed; for random sampling of invalid trials
        ------------------------
        returns pandas.DataFrame
    """
    prng = np.random.RandomState(seed)
    
    num_invalid = (len(valid)*(1.0-ratio))/ratio # invalid trials
    if force:
        invalid = valid[:]
        num_valid = (len(invalid)*ratio)/(1.0-ratio)
        copies = int(num_valid/len(valid))
        valid = pd.concat([valid]*copies, ignore_index=True)
    else:
        num_invalid = int(num_invalid)
        sampled = prng.choice(valid.index, num_invalid, replace=False)
        sampled.sort()
        invalid = valid.reindex(sampled).reset_index(drop=True)
    return pd.concat([valid, invalid], keys=[1,0], names=ids).reset_index()
    
def extend(frame, max_length, ids=['trialIter','trialID']):
    """
    Duplicates the unique trials for a total length less than the provided max.
    
        frame --> pandas.DataFrame of unique trials
        max_length --> int max trials allowable in the experiment
        ids --> list of length 2; names for the ID columns
        ------------------------
        returns pandas.DataFrame
    """
    iters = max_length/len(frame)
    return pd.concat([frame]*iters, keys=range(1,iters+1), \
        names=ids).reset_index()

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

class StimGenerator(object):
    """ Flexible object to hold multiple generators """
    def __init__(self, stim_info, valid_col, input_col, output_col=None, \
        seed=None):
        """
        StimGenerator
        """
        self.stim_info = stim_info
        self.valid_col = valid_col
        self.input_col = input_col
        self.output_col = output_col or input_col
        
        self.prng = np.random.RandomState(seed)
        self._gens = {}

    def next(self, trial):
        """
        
        """
        genID = (trial[self.input_col], trial[self.valid_col])
        if genID not in self._gens.keys():
            self._gens[genID] = self._generator(*genID)
        while True:
            generated = self._gens[genID].next()
            if self.input_col == self.output_col:
                break
            elif generated != trial[self.output_col]:
                break
        return generated

    def _generator(self, target, is_match):
        """ Generator for a randomized list iteration. """
        select = (self.stim_info[self.input_col]==target)
        _sub = self.stim_info[(is_match==select)]
        opts = np.array(_sub.index)
        self.prng.shuffle(opts)
        i = 0
        while True:
            yield _sub.ix[opts[i%len(_sub)]][self.output_col]
            if (i+1)%len(opts): 
                self.prng.shuffle(opts)
            i = (i+1)%len(opts)