ESTRUCTURA DE DADES (UB) - ENTREGA 6
====================================

## Usage

Run the file `HEAPInterface.py` or `HASHInterface.py` to load the program using the `Heap` or `Hash` class respectively.

## Requirements

This software requires the files listed below:

 - LastFM_big.dat
 - LastFM_small.dat

## Running the Benchmarks

In order to perform benchmarks, I provide a `benchmark.py` file. The file shows an output like as follows:

```
[!] All time are in seconds
Hash benchmark started!
Hash benchmark finished!
Binary Search Tree benchmark started!
Binary Search Tree benchmark finished!
Heap benchmark started!
Heap benchmark finished!

--------------------------------------------------------------------------------
                      Hash                  Binary Search Tree    Heap
--------------------------------------------------------------------------------
Add 1                 0.817639112473        1.0370259285          0.765422821045
Add 2                 0.941713094711        1.15981912613         0.896310806274
Add 3                 1.00453805923         1.19306206703         0.836898088455
Add 4                 0.933771133423        1.31232905388         0.91774392128
Add 5                 0.978356122971        1.22519516945         1.00094985962
Add 6                 1.02586007118         1.03163003922         0.888828992844
Add 7                 0.802604198456        1.29287004471         0.935245037079
Add 8                 1.08508110046         1.34782886505         0.978885889053
Add 9                 1.15590000153         1.04934692383         0.723689079285
Add 10                0.819067955017        1.42610788345         1.0383348465

Min Add               0.802604198456        1.03163003922         0.723689079285
Max Add               1.15590000153         1.42610788345         1.0383348465
Average Add           0.956453084946        1.20752151012         0.898230934143
--------------------------------------------------------------------------------
Search 1              0.0076949596405       0.0774610042572       0.183679819107
Search 2              0.00817489624023      0.0738289356232       0.747845888138
Search 3              0.00737285614014      0.0733859539032       0.469314813614
Search 4              0.0081000328064       0.0730900764465       0.820204019547
Search 5              0.0195889472961       0.07239985466         0.192242145538
Search 6              0.00794887542725      0.0730109214783       0.116698026657
Search 7              0.00717091560364      0.0721428394318       2.19667887688
Search 8              0.0070469379425       0.0730729103088       1.30623817444
Search 9              0.0583980083466       0.0692889690399       0.292951822281
Search 10             0.00803399085999      0.075779914856        0.117978096008

Min Search            0.0070469379425       0.0692889690399       0.116698026657
Max Search            0.0583980083466       0.0774610042572       2.19667887688
Average Search        0.0139530420303       0.0733461380005       0.644383168221
--------------------------------------------------------------------------------
```

This teaches us that the faster structure to insert is the heap and the slower is the tree.
On the other hand, in searching, the heap shown extremely slow.

## Author

**Rafael Arquero Gimeno**