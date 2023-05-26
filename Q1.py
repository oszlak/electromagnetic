import numpy as np
from utils import L1_HEIGHT, SHELL_RADIUS

N_list = [100, 200, 400, 800, 1200, 1600, 3200]


def discretize_cylinder(N):
	n_phi = int(np.sqrt(N))  # Number of points in the phi direction
	n_z = int(N / n_phi)  # Number of points in the z direction

	angles = np.linspace(0, 2 * np.pi, n_phi, endpoint=False)  # Discretize the angle phi
	z_values = np.linspace(0, L1_HEIGHT, n_z, endpoint=False)  # Discretize the z-axis

	points = []
	for z in z_values:
		for angle in angles:
			x = SHELL_RADIUS * np.cos(angle)
			y = SHELL_RADIUS * np.sin(angle)
			points.append((x, y, z))

	return points


if __name__ == "__main__":
#plot the points
	import matplotlib.pyplot as plt
	from mpl_toolkits.mplot3d import Axes3D
	from matplotlib import cm
	from matplotlib.ticker import LinearLocator, FormatStrFormatter

	for N in N_list:
		points = discretize_cylinder(N)
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')  # Use add_subplot() instead of gca()
		X = [point[0] for point in points]
		Y = [point[1] for point in points]
		Z = [point[2] for point in points]
		ax.scatter(X, Y, Z, c=Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		ax.set_xlabel('X Label')
		ax.set_ylabel('Y Label')
		ax.set_zlabel('Z Label')
		plt.show()
		print(f"N = {N}: Number of points = {len(points)}")
