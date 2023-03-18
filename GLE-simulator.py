import numpy as np
import matplotlib.pyplot as plt

# Define constants
G = 6.6743e-11  # m^3/kg*s^2
c = 299792458  # m/s
M = 4.3e6 * 1.98855e30  # kg, mass of Sagittarius A*
D_s = 8.5 * 3.086e16  # m, distance to the source (a star)
D_ls = 2.6 * 3.086e16  # m, distance between the lens (black hole) and the source
theta_E = np.sqrt(4 * G * M * D_ls / (c**2 * D_s))  # Einstein radius

# Set up coordinate system
nx = 500
ny = 500
xmin, xmax, ymin, ymax = -5, 5, -5, 5
x = np.linspace(xmin, xmax, nx)
y = np.linspace(ymin, ymax, ny)
xx, yy = np.meshgrid(x, y)

# Calculate lensing potential and deflection angle
phi = theta_E**2 / 2 * np.log((xx**2 + yy**2) / (theta_E**2))
alpha_x = 4 * G * M / (c**2 * D_ls) * xx / (xx**2 + yy**2)
alpha_y = 4 * G * M / (c**2 * D_ls) * yy / (xx**2 + yy**2)

# Calculate image positions and magnifications
x_image = xx - alpha_x
y_image = yy - alpha_y
magnification = 1 / (1 - 2 * G * M / (c**2 * (xx**2 + yy**2)))

# Plot results
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(phi, extent=(xmin, xmax, ymin, ymax), cmap='coolwarm')
ax[0].set_title('Lensing potential')
ax[1].imshow(magnification, extent=(xmin, xmax, ymin, ymax), cmap='coolwarm')
ax[1].set_title('Magnification')
plt.show()
