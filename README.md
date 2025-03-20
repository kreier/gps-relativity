# Relative time for GPS satellites

![GitHub Release](https://img.shields.io/github/v/release/kreier/gps-relativity)
![GitHub License](https://img.shields.io/github/license/kreier/gps-relativity)
[![Deploy Jekyll with GitHub Pages](https://github.com/kreier/gps-relativity/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/kreier/gps-relativity/actions/workflows/jekyll-gh-pages.yml)

GPS satellites experience both gravitational time dilation (due to being farther from Earth's gravitational field compared to ground stations) and special relativistic time dilation (due to their high orbital velocity). Let's break it down:

1. **Gravitational Time Dilation:** The satellite's clock runs *faster* because it's farther from Earth’s gravitational field. This causes its clock to gain about **+45.7 microseconds** per day relative to a clock on the ground.

2. **Special Relativistic Time Dilation:** Due to the satellite's orbital speed (around 14,000 km/h), its clock runs *slower*. This effect leads to a loss of about **−7.2 microseconds** per day.

When we combine these effects, the net result is that the satellite clock runs about **+38.5 microseconds faster per day** compared to a clock on Earth.

Although this seems tiny, it’s a critical adjustment—GPS systems have to account for this difference to maintain precise timing, as even a small error can lead to significant inaccuracies in positioning. 


## 1. Gravitational Time Dilation (General Relativity)

According to general relativity, clocks in a stronger gravitational field tick slower. Since GPS satellites orbit at an altitude of **20,200 km** (or a radius of **26,600 km** from Earth's center), they experience **less gravitational time dilation** than clocks on Earth.

The time dilation factor due to gravity is given by:

$$
\frac{\Delta t_s}{\Delta t_e} \approx 1 + \frac{GM}{c^2}\left(\frac{1}{r_e} - \frac{1}{r_s} \right)
$$

where:

- $𝐺=6.674×10^{−11} m^3/kg/s^2$ (gravitational constant)
- $𝑀=5.972×10^{24} kg$ (Earth’s mass)
- $𝑐=3.0×10^8 m/s$ (speed of light)
- $𝑟_e = 6,378 km = 6.378 × 10^6 m$ (Earth's radius)
- $r_s = 26,600 km = 2.66 × 10^7 m$ (GPS satellite orbital radius)

Calculating the gravitational time dilation factor:

$$
\frac{𝐺𝑀}{𝑐^2} = \frac{(6.674×10^{−11})(5.972×10^{24})}{(3.0×10^8)^2} = 4.44 × 10^{−3} m
$$

$$
\frac{1}{r_e} - \frac{1}{r_s} = \frac{1}{6.378 \times 10^6} - \frac{1}{2.66 \times 10^7} = (1.567 \times 10^{-7}) − (3.759×10^{−8}) = 1.191×10^{−7} m^{−1}
$$

$$
\frac{\Delta t_s}{\Delta t_e} \approx 1 + (4.44 \times 10^{-3} \times 1.191 \times 10^{-7}) = 1 + 5.29 \times 10^{-10}
$$
 
So, the GPS satellite clock ticks faster due to the weaker gravity, gaining about **45.7 microseconds per day**.

``` py
import math

G = 6.674 * 10**-11  # Gravitational constant
M = 5.972 * 10**24   # Earth's mass
c = 3.0 * 10**8      # Speed of light
r_e = 6.378 * 10**6  # Earth's radius
r_s = 2.66 * 10**7   # GPS satellite orbital radius
day = 24 * 60 * 60   # Number of seconds in a day

# Calculate the gravitational time dilation factor
delta_t_factor = (G * M) / (c**2) * (1 / r_e - 1 / r_s)
print(f"Gravitational Time Dilation Factor: {delta_t_factor}")
print(f"Time Dilation per day: {day*delta_t_factor*10**6:.1f} microseconds.")
```

> Gravitational Time Dilation Factor: 5.278632732243486e-10 and Time Dilation per day: 45.7 microseconds.

## 2. Special Relativity Time Dilation

According to special relativity, moving clocks run slower. Since GPS satellites orbit at **3.87 km/s**, their velocity causes time dilation.

The relativistic time dilation factor is:

$$
\frac{\Delta t_s}{\Delta t_e} = \sqrt{1 - \frac{v^2}{c^2}}
$$
 
where $𝑣 = 3.87×10^3$ m/s.

$$
\frac{v^2}{c^2} = \left( \frac{3.87 \times 10^3}{3.0 \times 10^8} \right)^2 = 1.66 \times 10^{-10}
$$

$$
\sqrt{1 - 1.66 \times 10^{-10}} \approx 1 - \frac{1.66 \times 10^{-10}}{2} = 1 - 8.3 \times 10^{-11}
$$

``` py
import math

v = 3.87 * 10**3  # Satellite velocity
c = 3.0 * 10**8   # Speed of light
day = 24 * 60 * 60  # Number of seconds in a

gamma = (v**2 / c**2)
d = math.sqrt(1 - gamma)
print(f"Relativistic Time Dilation Factor: {d} with the gamma ratio (v/c)^2: {gamma}")
print(f"Time Dilation per day: {day*(1-d)*10**6:.3f} microseconds.")
```

> Relativistic Time Dilation Factor: 0.999999999916795 with the gamma ratio (v/c)^2: 1.6641e-10, leading to a time Dilation per day: 7.189 microseconds.

## Total Time Difference in 24 Hours

- Gravitational time dilation effect: +45.7 μs/day (clock runs faster)
- Velocity time dilation effect: −7.2 μs/day (clock runs slower)
- Net effect = 45.7 − 7.2 = 38.5  μs/day

### Conclusion

A GPS satellite clock runs ahead of a ground clock by about 38.5 microseconds per day. This discrepancy is corrected in GPS system design to ensure accurate positioning calculations.
  
