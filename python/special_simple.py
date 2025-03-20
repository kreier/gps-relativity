import math

v = 3.87 * 10**3  # Satellite velocity
c = 3.0 * 10**8   # Speed of light
day = 24 * 60 * 60  # Number of seconds in a

gamma = (v**2 / c**2)
d = math.sqrt(1 - gamma)
print(f"Relativistic Time Dilation Factor: {d} with the gamma ratio (v/c)^2: {gamma}")
print(f"Time Dilation per day: {day*(1-d)*10**6:.3f} microseconds.")

