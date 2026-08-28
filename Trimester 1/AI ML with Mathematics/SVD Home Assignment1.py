import numpy as np

R = np.array([
    [5, 4, 4, 5],
    [5, 4, 5, 5],
    [5, 2, 3, 3],
    [2, 1, 1, 2]
], dtype=float)

print("Original Matrix R:")
print(R)

RT_R = R.T @ R

print("\nR^T R:")
print(RT_R)

eigenvalues, eigenvectors = np.linalg.eig(RT_R)


indices = np.argsort(eigenvalues)[::-1]

eigenvalues = eigenvalues[indices]
eigenvectors = eigenvectors[:, indices]


singular_values = np.sqrt(np.maximum(eigenvalues, 0))

print("\nEigenvalues:")
print(np.round(eigenvalues, 4))

print("\nSingular Values:")
print(np.round(singular_values, 4))

V = eigenvectors
print("\nMatrix V:")
print(np.round(V, 4))

U = np.zeros_like(R)

for i in range(len(singular_values)):
    U[:, i] = (R @ V[:, i]) / singular_values[i]
print("\nMatrix U:")
print(np.round(U, 4))

Sigma = np.zeros_like(R)

for i in range(len(singular_values)):
    Sigma[i, i] = singular_values[i]
print("\nMatrix Sigma:")
print(np.round(Sigma, 4))

VT = V.T
print("\nMatrix V^T:")
print(np.round(VT, 4))

R_reconstructed = U @ Sigma @ VT
print("\nReconstructed Matrix U Sigma V^T:")
print(np.round(R_reconstructed, 4))



# second approach using numpy svd

import numpy as np

R = np.array([
    [5, 4, 4, 5],
    [5, 4, 5, 5],
    [5, 2, 3, 3],
    [2, 1, 1, 2]
], dtype=float)

U, S, VT = np.linalg.svd(R)

Sigma = np.zeros_like(R)
np.fill_diagonal(Sigma, S)

print("Original Matrix R:")
print(R)

print("\nMatrix U:")
print(np.round(U, 4))

print("\nSingular Values:")
print(np.round(S, 4))

print("\nSigma Matrix:")
print(np.round(Sigma, 4))

print("\nMatrix V^T:")
print(np.round(VT, 4))

R_reconstructed = U @ Sigma @ VT

print("\nReconstructed Matrix U * Sigma * V^T:")
print(np.round(R_reconstructed, 4))
