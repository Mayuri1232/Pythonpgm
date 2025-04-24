import numpy as np

A = np.array([[10, 20],
              [30, 40]])

B = np.array([[1, 2],
              [3, 4]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

add_result = A + B
print("\nAddition of A and B:")
print(add_result)

sub_result = A - B
print("\nSubtraction of A and B:")
print(sub_result)

mul_result = A * B
print("\nElement-wise Multiplication of A and B:")
print(mul_result)

div_result = A / B
print("\nElement-wise Division of A by B:")
print(div_result)
