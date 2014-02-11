Making Trial Lists
==================

.. currentmodule:: resources

.. autofunction:: counterbalance

.. sourcecode:: ipython

    In [4]: my_variables = {'version':['a','b','c'], 'response':[1,2], 'session':[1,]}
    
    In [5]: counterbalance(my_variables, order=['version','session','response'])
    Out[5]: 
      version  session  response
    0       a        1         1
    1       a        1         2
    2       b        1         1
    3       b        1         2
    4       c        1         1
    5       c        1         2

.. autofunction:: expand

.. autofunction:: extend

.. autofunction:: add_block

.. autofunction:: smart_shuffle

.. autofunction:: simple_shuffle

.. autoclass:: StimGenerator
    :members: