Simple Trial Generation
=======================

counterbalance
--------------

.. autofunction:: resources.trials_functions.counterbalance

.. code:: python

    my_variables = {'version':['a','b','c'], 'response':[1,2], 'session':2}
    counterbalance(my_variables, order=['version','session','response'])

.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>version</th>
          <th>session</th>
          <th>response</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> a</td>
          <td> 2</td>
          <td> 1</td>
        </tr>
        <tr>
          <th>1</th>
          <td> a</td>
          <td> 2</td>
          <td> 2</td>
        </tr>
        <tr>
          <th>2</th>
          <td> b</td>
          <td> 2</td>
          <td> 1</td>
        </tr>
        <tr>
          <th>3</th>
          <td> b</td>
          <td> 2</td>
          <td> 2</td>
        </tr>
        <tr>
          <th>4</th>
          <td> c</td>
          <td> 2</td>
          <td> 1</td>
        </tr>
        <tr>
          <th>5</th>
          <td> c</td>
          <td> 2</td>
          <td> 2</td>
        </tr>
      </tbody>
    </table>
    </div>

expand
------

.. autofunction:: resources.trials_functions.expand

.. code:: python

    posner = expand(posner, 'valid_prime', ratio=0.75)
    posner

.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>valid_prime</th>
          <th>target_dir</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 1</td>
          <td> right</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 1</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 1</td>
          <td> right</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 1</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>5</th>
          <td> 1</td>
          <td> right</td>
        </tr>
        <tr>
          <th>6</th>
          <td> 0</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>7</th>
          <td> 0</td>
          <td> right</td>
        </tr>
      </tbody>
    </table>
    </div>

.. code:: python

    posner = expand(posner, 'prime_type', values=['present', 'neutral'], ratio=0.5)
    posner['valid_prime'][posner['prime_type'] == 'neutral'] = np.nan
    posner

.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>prime_type</th>
          <th>valid_prime</th>
          <th>target_dir</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0 </th>
          <td> present</td>
          <td>  1</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>1 </th>
          <td> present</td>
          <td>  1</td>
          <td> right</td>
        </tr>
        <tr>
          <th>2 </th>
          <td> present</td>
          <td>  1</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>3 </th>
          <td> present</td>
          <td>  1</td>
          <td> right</td>
        </tr>
        <tr>
          <th>4 </th>
          <td> present</td>
          <td>  1</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>5 </th>
          <td> present</td>
          <td>  1</td>
          <td> right</td>
        </tr>
        <tr>
          <th>6 </th>
          <td> present</td>
          <td>  0</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>7 </th>
          <td> present</td>
          <td>  0</td>
          <td> right</td>
        </tr>
        <tr>
          <th>8 </th>
          <td> neutral</td>
          <td>NaN</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>9 </th>
          <td> neutral</td>
          <td>NaN</td>
          <td> right</td>
        </tr>
        <tr>
          <th>10</th>
          <td> neutral</td>
          <td>NaN</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>11</th>
          <td> neutral</td>
          <td>NaN</td>
          <td> right</td>
        </tr>
        <tr>
          <th>12</th>
          <td> neutral</td>
          <td>NaN</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>13</th>
          <td> neutral</td>
          <td>NaN</td>
          <td> right</td>
        </tr>
        <tr>
          <th>14</th>
          <td> neutral</td>
          <td>NaN</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>15</th>
          <td> neutral</td>
          <td>NaN</td>
          <td> right</td>
        </tr>
      </tbody>
    </table>
    </div>

.. autofunction:: resources.trials_functions.extend

.. code:: python

    extend(posner, reps = 2)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>prime_type</th>
          <th>valid_prime</th>
          <th>target_dir</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0 </th>
          <td> present</td>
          <td>  1</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>1 </th>
          <td> present</td>
          <td>  1</td>
          <td> right</td>
        </tr>
        <tr>
          <th>2 </th>
          <td> present</td>
          <td>  1</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>3 </th>
          <td> present</td>
          <td>  1</td>
          <td> right</td>
        </tr>
        <tr>
          <th>4 </th>
          <td> present</td>
          <td>  1</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>5 </th>
          <td> present</td>
          <td>  1</td>
          <td> right</td>
        </tr>
        <tr>
          <th>6 </th>
          <td> present</td>
          <td>  0</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>7 </th>
          <td> present</td>
          <td>  0</td>
          <td> right</td>
        </tr>
        <tr>
          <th>8 </th>
          <td> neutral</td>
          <td>NaN</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>9 </th>
          <td> neutral</td>
          <td>NaN</td>
          <td> right</td>
        </tr>
        <tr>
          <th>10</th>
          <td> neutral</td>
          <td>NaN</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>11</th>
          <td> neutral</td>
          <td>NaN</td>
          <td> right</td>
        </tr>
        <tr>
          <th>12</th>
          <td> neutral</td>
          <td>NaN</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>13</th>
          <td> neutral</td>
          <td>NaN</td>
          <td> right</td>
        </tr>
        <tr>
          <th>14</th>
          <td> neutral</td>
          <td>NaN</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>15</th>
          <td> neutral</td>
          <td>NaN</td>
          <td> right</td>
        </tr>
        <tr>
          <th>16</th>
          <td> present</td>
          <td>  1</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>17</th>
          <td> present</td>
          <td>  1</td>
          <td> right</td>
        </tr>
        <tr>
          <th>18</th>
          <td> present</td>
          <td>  1</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>19</th>
          <td> present</td>
          <td>  1</td>
          <td> right</td>
        </tr>
        <tr>
          <th>20</th>
          <td> present</td>
          <td>  1</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>21</th>
          <td> present</td>
          <td>  1</td>
          <td> right</td>
        </tr>
        <tr>
          <th>22</th>
          <td> present</td>
          <td>  0</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>23</th>
          <td> present</td>
          <td>  0</td>
          <td> right</td>
        </tr>
        <tr>
          <th>24</th>
          <td> neutral</td>
          <td>NaN</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>25</th>
          <td> neutral</td>
          <td>NaN</td>
          <td> right</td>
        </tr>
        <tr>
          <th>26</th>
          <td> neutral</td>
          <td>NaN</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>27</th>
          <td> neutral</td>
          <td>NaN</td>
          <td> right</td>
        </tr>
        <tr>
          <th>28</th>
          <td> neutral</td>
          <td>NaN</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>29</th>
          <td> neutral</td>
          <td>NaN</td>
          <td> right</td>
        </tr>
        <tr>
          <th>30</th>
          <td> neutral</td>
          <td>NaN</td>
          <td>  left</td>
        </tr>
        <tr>
          <th>31</th>
          <td> neutral</td>
          <td>NaN</td>
          <td> right</td>
        </tr>
      </tbody>
    </table>
    </div>

.. code:: python

    posner_full = extend(posner, max_length = 390, rep_ix = 'iteration')
    len(posner_full)

.. parsed-literal::

    384

add_block
---------

.. autofunction:: resources.trials_functions.add_block

simple_shuffle
--------------

.. autofunction:: resources.trials_functions.simple_shuffle

smart_shuffle
-------------

.. autofunction:: resources.trials_functions.smart_shuffle
