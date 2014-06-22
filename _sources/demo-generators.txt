Generators
==========

.. code:: python

    items = ['red','orange','yellow','green','blue','indigo','violet']
    items = pd.DataFrame({'item':items}, index = pd.Index(range(len(items)),
                                                          name = 'item_id'))
    
    stroop = pd.DataFrame({'letters':items['item'].values})
    stroop = extend(stroop, reps = 4, rep_ix = 'letters_iter', 
                    row_ix = 'letters_id')
    stroop

.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>letters_iter</th>
          <th>letters_id</th>
          <th>letters</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0 </th>
          <td> 0</td>
          <td> 0</td>
          <td>    red</td>
        </tr>
        <tr>
          <th>1 </th>
          <td> 0</td>
          <td> 1</td>
          <td> orange</td>
        </tr>
        <tr>
          <th>2 </th>
          <td> 0</td>
          <td> 2</td>
          <td> yellow</td>
        </tr>
        <tr>
          <th>3 </th>
          <td> 0</td>
          <td> 3</td>
          <td>  green</td>
        </tr>
        <tr>
          <th>4 </th>
          <td> 0</td>
          <td> 4</td>
          <td>   blue</td>
        </tr>
        <tr>
          <th>5 </th>
          <td> 0</td>
          <td> 5</td>
          <td> indigo</td>
        </tr>
        <tr>
          <th>6 </th>
          <td> 0</td>
          <td> 6</td>
          <td> violet</td>
        </tr>
        <tr>
          <th>7 </th>
          <td> 1</td>
          <td> 0</td>
          <td>    red</td>
        </tr>
        <tr>
          <th>8 </th>
          <td> 1</td>
          <td> 1</td>
          <td> orange</td>
        </tr>
        <tr>
          <th>9 </th>
          <td> 1</td>
          <td> 2</td>
          <td> yellow</td>
        </tr>
        <tr>
          <th>10</th>
          <td> 1</td>
          <td> 3</td>
          <td>  green</td>
        </tr>
        <tr>
          <th>11</th>
          <td> 1</td>
          <td> 4</td>
          <td>   blue</td>
        </tr>
        <tr>
          <th>12</th>
          <td> 1</td>
          <td> 5</td>
          <td> indigo</td>
        </tr>
        <tr>
          <th>13</th>
          <td> 1</td>
          <td> 6</td>
          <td> violet</td>
        </tr>
        <tr>
          <th>14</th>
          <td> 2</td>
          <td> 0</td>
          <td>    red</td>
        </tr>
        <tr>
          <th>15</th>
          <td> 2</td>
          <td> 1</td>
          <td> orange</td>
        </tr>
        <tr>
          <th>16</th>
          <td> 2</td>
          <td> 2</td>
          <td> yellow</td>
        </tr>
        <tr>
          <th>17</th>
          <td> 2</td>
          <td> 3</td>
          <td>  green</td>
        </tr>
        <tr>
          <th>18</th>
          <td> 2</td>
          <td> 4</td>
          <td>   blue</td>
        </tr>
        <tr>
          <th>19</th>
          <td> 2</td>
          <td> 5</td>
          <td> indigo</td>
        </tr>
        <tr>
          <th>20</th>
          <td> 2</td>
          <td> 6</td>
          <td> violet</td>
        </tr>
        <tr>
          <th>21</th>
          <td> 3</td>
          <td> 0</td>
          <td>    red</td>
        </tr>
        <tr>
          <th>22</th>
          <td> 3</td>
          <td> 1</td>
          <td> orange</td>
        </tr>
        <tr>
          <th>23</th>
          <td> 3</td>
          <td> 2</td>
          <td> yellow</td>
        </tr>
        <tr>
          <th>24</th>
          <td> 3</td>
          <td> 3</td>
          <td>  green</td>
        </tr>
        <tr>
          <th>25</th>
          <td> 3</td>
          <td> 4</td>
          <td>   blue</td>
        </tr>
        <tr>
          <th>26</th>
          <td> 3</td>
          <td> 5</td>
          <td> indigo</td>
        </tr>
        <tr>
          <th>27</th>
          <td> 3</td>
          <td> 6</td>
          <td> violet</td>
        </tr>
      </tbody>
    </table>
    </div>

generate
--------

.. autofunction:: resources.generator_functions.generate

.. code:: python

    generate(stroop, items, cols = {'item':'color'}, seed = 123)

.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>letters_iter</th>
          <th>letters_id</th>
          <th>letters</th>
          <th>color</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0 </th>
          <td> 0</td>
          <td> 0</td>
          <td>    red</td>
          <td> orange</td>
        </tr>
        <tr>
          <th>1 </th>
          <td> 0</td>
          <td> 1</td>
          <td> orange</td>
          <td>  green</td>
        </tr>
        <tr>
          <th>2 </th>
          <td> 0</td>
          <td> 2</td>
          <td> yellow</td>
          <td>   blue</td>
        </tr>
        <tr>
          <th>3 </th>
          <td> 0</td>
          <td> 3</td>
          <td>  green</td>
          <td>    red</td>
        </tr>
        <tr>
          <th>4 </th>
          <td> 0</td>
          <td> 4</td>
          <td>   blue</td>
          <td> yellow</td>
        </tr>
        <tr>
          <th>5 </th>
          <td> 0</td>
          <td> 5</td>
          <td> indigo</td>
          <td> indigo</td>
        </tr>
        <tr>
          <th>6 </th>
          <td> 0</td>
          <td> 6</td>
          <td> violet</td>
          <td> violet</td>
        </tr>
        <tr>
          <th>7 </th>
          <td> 1</td>
          <td> 0</td>
          <td>    red</td>
          <td> yellow</td>
        </tr>
        <tr>
          <th>8 </th>
          <td> 1</td>
          <td> 1</td>
          <td> orange</td>
          <td> orange</td>
        </tr>
        <tr>
          <th>9 </th>
          <td> 1</td>
          <td> 2</td>
          <td> yellow</td>
          <td> violet</td>
        </tr>
        <tr>
          <th>10</th>
          <td> 1</td>
          <td> 3</td>
          <td>  green</td>
          <td> indigo</td>
        </tr>
        <tr>
          <th>11</th>
          <td> 1</td>
          <td> 4</td>
          <td>   blue</td>
          <td>   blue</td>
        </tr>
        <tr>
          <th>12</th>
          <td> 1</td>
          <td> 5</td>
          <td> indigo</td>
          <td>    red</td>
        </tr>
        <tr>
          <th>13</th>
          <td> 1</td>
          <td> 6</td>
          <td> violet</td>
          <td>  green</td>
        </tr>
        <tr>
          <th>14</th>
          <td> 2</td>
          <td> 0</td>
          <td>    red</td>
          <td> indigo</td>
        </tr>
        <tr>
          <th>15</th>
          <td> 2</td>
          <td> 1</td>
          <td> orange</td>
          <td>    red</td>
        </tr>
        <tr>
          <th>16</th>
          <td> 2</td>
          <td> 2</td>
          <td> yellow</td>
          <td>   blue</td>
        </tr>
        <tr>
          <th>17</th>
          <td> 2</td>
          <td> 3</td>
          <td>  green</td>
          <td> violet</td>
        </tr>
        <tr>
          <th>18</th>
          <td> 2</td>
          <td> 4</td>
          <td>   blue</td>
          <td>  green</td>
        </tr>
        <tr>
          <th>19</th>
          <td> 2</td>
          <td> 5</td>
          <td> indigo</td>
          <td> yellow</td>
        </tr>
        <tr>
          <th>20</th>
          <td> 2</td>
          <td> 6</td>
          <td> violet</td>
          <td> orange</td>
        </tr>
        <tr>
          <th>21</th>
          <td> 3</td>
          <td> 0</td>
          <td>    red</td>
          <td> yellow</td>
        </tr>
        <tr>
          <th>22</th>
          <td> 3</td>
          <td> 1</td>
          <td> orange</td>
          <td>  green</td>
        </tr>
        <tr>
          <th>23</th>
          <td> 3</td>
          <td> 2</td>
          <td> yellow</td>
          <td>   blue</td>
        </tr>
        <tr>
          <th>24</th>
          <td> 3</td>
          <td> 3</td>
          <td>  green</td>
          <td> violet</td>
        </tr>
        <tr>
          <th>25</th>
          <td> 3</td>
          <td> 4</td>
          <td>   blue</td>
          <td>    red</td>
        </tr>
        <tr>
          <th>26</th>
          <td> 3</td>
          <td> 5</td>
          <td> indigo</td>
          <td> indigo</td>
        </tr>
        <tr>
          <th>27</th>
          <td> 3</td>
          <td> 6</td>
          <td> violet</td>
          <td> orange</td>
        </tr>
      </tbody>
    </table>
    </div>

generate_but_not
----------------

.. autofunction:: resources.generator_functions.generate_but_not

.. code:: python

    generate_but_not(stroop, items, on = ['letters','item'],
                     cols = {'item':'color'}, seed = 124)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>letters_iter</th>
          <th>letters_id</th>
          <th>letters</th>
          <th>color</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0 </th>
          <td> 0</td>
          <td> 0</td>
          <td>    red</td>
          <td>  green</td>
        </tr>
        <tr>
          <th>1 </th>
          <td> 0</td>
          <td> 1</td>
          <td> orange</td>
          <td>  green</td>
        </tr>
        <tr>
          <th>2 </th>
          <td> 0</td>
          <td> 2</td>
          <td> yellow</td>
          <td> orange</td>
        </tr>
        <tr>
          <th>3 </th>
          <td> 0</td>
          <td> 3</td>
          <td>  green</td>
          <td>    red</td>
        </tr>
        <tr>
          <th>4 </th>
          <td> 0</td>
          <td> 4</td>
          <td>   blue</td>
          <td>    red</td>
        </tr>
        <tr>
          <th>5 </th>
          <td> 0</td>
          <td> 5</td>
          <td> indigo</td>
          <td>    red</td>
        </tr>
        <tr>
          <th>6 </th>
          <td> 0</td>
          <td> 6</td>
          <td> violet</td>
          <td>    red</td>
        </tr>
        <tr>
          <th>7 </th>
          <td> 1</td>
          <td> 0</td>
          <td>    red</td>
          <td>   blue</td>
        </tr>
        <tr>
          <th>8 </th>
          <td> 1</td>
          <td> 1</td>
          <td> orange</td>
          <td> yellow</td>
        </tr>
        <tr>
          <th>9 </th>
          <td> 1</td>
          <td> 2</td>
          <td> yellow</td>
          <td>  green</td>
        </tr>
        <tr>
          <th>10</th>
          <td> 1</td>
          <td> 3</td>
          <td>  green</td>
          <td>   blue</td>
        </tr>
        <tr>
          <th>11</th>
          <td> 1</td>
          <td> 4</td>
          <td>   blue</td>
          <td> yellow</td>
        </tr>
        <tr>
          <th>12</th>
          <td> 1</td>
          <td> 5</td>
          <td> indigo</td>
          <td> orange</td>
        </tr>
        <tr>
          <th>13</th>
          <td> 1</td>
          <td> 6</td>
          <td> violet</td>
          <td> orange</td>
        </tr>
        <tr>
          <th>14</th>
          <td> 2</td>
          <td> 0</td>
          <td>    red</td>
          <td> indigo</td>
        </tr>
        <tr>
          <th>15</th>
          <td> 2</td>
          <td> 1</td>
          <td> orange</td>
          <td>    red</td>
        </tr>
        <tr>
          <th>16</th>
          <td> 2</td>
          <td> 2</td>
          <td> yellow</td>
          <td> indigo</td>
        </tr>
        <tr>
          <th>17</th>
          <td> 2</td>
          <td> 3</td>
          <td>  green</td>
          <td> indigo</td>
        </tr>
        <tr>
          <th>18</th>
          <td> 2</td>
          <td> 4</td>
          <td>   blue</td>
          <td> violet</td>
        </tr>
        <tr>
          <th>19</th>
          <td> 2</td>
          <td> 5</td>
          <td> indigo</td>
          <td>  green</td>
        </tr>
        <tr>
          <th>20</th>
          <td> 2</td>
          <td> 6</td>
          <td> violet</td>
          <td> yellow</td>
        </tr>
        <tr>
          <th>21</th>
          <td> 3</td>
          <td> 0</td>
          <td>    red</td>
          <td> orange</td>
        </tr>
        <tr>
          <th>22</th>
          <td> 3</td>
          <td> 1</td>
          <td> orange</td>
          <td> indigo</td>
        </tr>
        <tr>
          <th>23</th>
          <td> 3</td>
          <td> 2</td>
          <td> yellow</td>
          <td> violet</td>
        </tr>
        <tr>
          <th>24</th>
          <td> 3</td>
          <td> 3</td>
          <td>  green</td>
          <td> yellow</td>
        </tr>
        <tr>
          <th>25</th>
          <td> 3</td>
          <td> 4</td>
          <td>   blue</td>
          <td>  green</td>
        </tr>
        <tr>
          <th>26</th>
          <td> 3</td>
          <td> 5</td>
          <td> indigo</td>
          <td>   blue</td>
        </tr>
        <tr>
          <th>27</th>
          <td> 3</td>
          <td> 6</td>
          <td> violet</td>
          <td>   blue</td>
        </tr>
      </tbody>
    </table>
    </div>

generate_by_group
-----------------

.. autofunction:: resources.generator_functions.generate_by_group

generate_matches
----------------

.. autofunction:: resources.generator_functions.generate_matches
