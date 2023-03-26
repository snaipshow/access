import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Задаем точки
A = np.array([0, 0, 0])
B = np.array([6*np.sqrt(2), 0, 0])
C = np.array([6*np.sqrt(2), 10, 0])
D = np.array([0, 10, 0])
A1 = np.array([0, 0, 16])
B1 = np.array([6*np.sqrt(2), 0, 16])
C1 = np.array([6*np.sqrt(2), 10, 16])
D1 = np.array([0, 10, 16])
E = (2/3)*A1 + (1/3)*A
F = (11/16)*B + (5/16)*B1

# Создаем 3D график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Добавляем точки на график
ax.scatter(A[0], A[1], A[2], c='r')
ax.scatter(B[0], B[1], B[2], c='r')
ax.scatter(C[0], C[1], C[2], c='r')
ax.scatter(D[0], D[1], D[2], c='r')
ax.scatter(A1[0], A1[1], A1[2], c='r')
ax.scatter(B1[0], B1[1], B1[2], c='r')
ax.scatter(C1[0], C1[1], C1[2], c='r')
ax.scatter(D1[0], D1[1], D1[2], c='r')
ax.scatter(E[0], E[1], E[2], c='b')
ax.scatter(F[0], F[1], F[2], c='b')

# Добавляем названия точек
ax.text(A[0], A[1], A[2], 'A')
ax.text(B[0], B[1], B[2], 'B')
ax.text(C[0], C[1], C[2], 'C')
ax.text(D[0], D[1], D[2], 'D')
ax.text(A1[0], A1[1], A1[2], 'A1')
ax.text(B1[0], B1[1], B1[2], 'B1')
ax.text(C1[0], C1[1], C1[2], 'C1')
ax.text(D1[0], D1[1], D1[2], 'D1')
ax.text(E[0], E[1], E[2], 'E')
ax.text(F[0], F[1], F[2], 'F')

# Добавляем линии между точками
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], c='k')
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], c='k')
ax.plot([D[0], A[0]], [D[1], A[1]], [D[2], A[2]], c='k')
ax.plot([A1[0], B1[0]], [A1[1], B1[1]], [A1[2], B1[2]], c='k')
ax.plot([B1[0], C1[0]], [B1[1], C1[1]], [B1[2], C1[2]], c='k')
ax.plot([C1[0], D1[0]], [C1[1], D1[1]], [C1[2], D1[2]], c='k')
ax.plot([D1[0], A1[0]], [D1[1], A1[1]], [D1[2], A1[2]], c='k')
ax.plot([A[0], A1[0]], [A[1], A1[1]], [A[2], A1[2]], c='k')
ax.plot([B[0], B1[0]], [B[1], B1[1]], [B[2], B1[2]], c='k')
ax.plot([C[0], C1[0]], [C[1], C1[1]], [C[2], C1[2]], c='k')
ax.plot([D[0], D1[0]], [D[1], D1[1]], [D[2], D1[2]], c='k')
ax.plot([B1[0], F[0]], [B1[1], F[1]], [B1[2], F[2]], c='k')
ax.plot([E[0], F[0]], [E[1], F[1]], [E[2], F[2]], c='b')
ax.plot([E[0], A1[0]], [E[1], A1[1]], [E[2], A1[2]], c='b')
ax.plot([F[0], C1[0]], [F[1], C1[1]], [F[2], C1[2]], c='b')

ax.set_title('3D график')
ax.legend(['AB', 'BC', 'CD', 'DA', 'A1B1', 'B1C1', 'C1D1', 'D1A1', 'AB1', 'EFT', 'EA1', 'FC1'])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


plt.show()
