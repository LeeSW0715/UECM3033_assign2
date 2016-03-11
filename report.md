UECM3033 Assignment #2 Report
========================================================

- Prepared by: Lee Soon Wah
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/LeeSW0715/UECM3033_assign2](https://github.com/LeeSW0715/UECM3033_assign2)

Explain your selection criteria here.
Coding with "np.count_nonzero(A) > 1/2*len(A)" at line 37 is used to when a matrix A with number of non-zero is more than half of the length of matirx A, then the matrix A is called Sparse matrix and using if-else loop to do LU decomposition, otherwise the matirx A will do the SOR for sparse matrix.

Explain how you implement your `task1.py` here.

Two different size of Matrix A is given, this two matrix will undergo any one of the decompostion.

LU decomposition: Matrix A will seperated into two different matrix called L(Lower trianglar matrix) and U(Upper trianglar matrix), with formula A = LU.

SOR decomposition: initially with the coding "ITERATION LIMIT = 10 " at line 2, is used to control the number of iteration. Next let the value of omega = 1.05 at line 26, to let the matirx A be convergent, postive definite and symmetric. Then when starts the iteration, the first element in newA is zero vector, when every new newA will release until 10 times of iteration.
---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file (Lenna.png)

![Lenna.png](Lenna.png)

How many non zero element in $\Sigma$?
800

Put here your lower and better resolution pictures. Explain how you generate
these pictures from `task2.py`.

What is a sparse matrix?
Sparse matrix is a matrix that has relatively few non-zero entries, it may be represented in much less than n × m space; but if most of the elements are nonzero, then the matrix is considered dense. A sparse matrix is created first 30 elements of $\Sigma$ is kept and other elements in the matrix are zero element. When dimension (800,1000) is form in $\Sigma$, then it clearly show that it is a large sparse matrix, but when the matrix is dot product with matrix U and V, it will form a lower resolution of picture.
-----------------------------------

<sup>last modified: 11 March 2016</sup>
