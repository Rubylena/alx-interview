# 0x07-rotate_2d_matrix
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.

Explanation:
To rotate an n x n 2D matrix by 90 degrees clockwise, you can perform the following steps:

-- Transpose the matrix: Swap the elements across the diagonal line (i.e., swap matrix[i][j] with matrix[j][i]).
-- Reverse each row: For each row in the transposed matrix, reverse the elements of the row.

In the code, we first calculate the size of the matrix, which is the length of the matrix (since it's a square matrix). Then, we perform the transpose of the matrix by swapping the elements across the diagonal line. Finally, we reverse each row in the transposed matrix to get the final rotated matrix.