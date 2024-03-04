# I got help form ChaptGPT
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Colebrook equation as a lambda function for convenience
colebrook = lambda f, Re, eD: 1/np.sqrt(f) + 2.0*np.log10((eD)/3.7 + 2.51/(Re*np.sqrt(f)))

# Function to calculate friction factor for turbulent flow using the Colebrook equation
def calculate_friction_factor(Re, eD):
    # Initial guess for f is given by the approximation of the Colebrook equation: f = 1/(1.8*log10(Re)-1.5)^2
    f_initial_guess = (1.8*np.log10(Re)-1.5)**-2
    # Solve for the root of the Colebrook equation
    f_turbulent, = fsolve(colebrook, f_initial_guess, args=(Re, eD))
    return f_turbulent

# Reynolds number range
Re_laminar = np.linspace(1, 2000, 100)
Re_transitional = np.linspace(2000, 4000, 100)
Re_turbulent = np.logspace(np.log10(4000), 8, 100)

# Relative roughness values
relative_roughnesses = [0.0, 0.00005, 0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02]

# Create Moody diagram
plt.figure(figsize=(10, 8))

# Laminar flow region
f_laminar = 64 / Re_laminar
plt.loglog(Re_laminar, f_laminar, 'k', linewidth=1, label='Laminar Flow')

# Transitional flow region - plotted as a grey area
plt.fill_between(Re_transitional, 64 / Re_transitional, calculate_friction_factor(4000, 0.02), color='grey', alpha=0.3)

# Turbulent flow region
for eD in relative_roughnesses:
    f_turbulent = [calculate_friction_factor(Re, eD) for Re in Re_turbulent]
    plt.loglog(Re_turbulent, f_turbulent, label=f'e/D = {eD}')

# Labeling the axes and the chart
plt.xlabel('Reynolds number, Re')
plt.ylabel('Friction factor, f')
plt.title('Moody Diagram')
plt.grid(True, which="both", ls="--")
plt.legend()

plt.show()
