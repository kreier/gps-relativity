import math

G = 6.674 * 10**-11  # Gravitational constant
M = 5.972 * 10**24   # Earth's mass
c = 299792458        # Speed of light
r_e =  6371000       # Earth's radius
r_s = 20183000 + r_e # GPS satellite altitude (m) to orbital radius
day = 24 * 60 * 60   # Number of seconds in a day

# Calculate the gravitational time dilation factor
delta_t_factor = (G * M) / (c**2) * (1 / r_e - 1 / r_s)
print(f"Gravitational Time Dilation Factor: {delta_t_factor}")
print(f"Time Dilation per day: {day*delta_t_factor*10**6:.2f} microseconds.")
