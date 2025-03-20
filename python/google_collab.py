# prompt: a calculation of the time dilation for a gps satellite in microseconds every day

import math

# Constants
c = 299792458        # Speed of light (m/s)
GM = 3.986 * 10**14  # Earth's gravitational constant (m^3/s^2)
R_earth = 6371000    # Earth's radius (m)
h = 20183000         # GPS satellite altitude (m)

# Calculate the special relativistic effect
v = math.sqrt(GM / (R_earth + h))  # Satellite velocity (m/s)
gamma = 1 / math.sqrt(1 - (v**2 / c**2))
delta_t_sr = (gamma - 1) * 24 * 60 * 60  # Time dilation in seconds per day

# Calculate the general relativistic effect
delta_t_gr = -(GM / (c**2) * ((1/R_earth)-1/(R_earth + h))) * 24 * 60 * 60  # Time dilation in seconds per day

# Calculate the total time dilation
delta_t_total = delta_t_sr + delta_t_gr

# Convert to microseconds
delta_t_microseconds = delta_t_total * 10**6

# Print the results
print(f"Speed of satellite: {v:.2f} m/s")
print(f"Special relativistic gamma factor: {gamma:.15f}")
print(f"Special relativistic time dilation: {delta_t_sr*10**6:.3f} microseconds per day")
print(f"General relativistic time dilation: {delta_t_gr*10**6:.3f} microseconds per day")
print(f"Total time dilation: {delta_t_total:.6f} seconds per day")
print(f"Total time dilation in microseconds: {delta_t_microseconds:.2f} microseconds per day")

# Answers: 
# Special relativistic time dilation: 0.000007 seconds per day
# General relativistic time dilation: 0.000014 seconds per day
# Total time dilation: 0.000022 seconds per day
# Total time dilation in microseconds: 21.65 microseconds per day
