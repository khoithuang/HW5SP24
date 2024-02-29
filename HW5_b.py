import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Colebrook equation as a function
def colebrook(f, Re, eD):
    return 1/np.sqrt(f) + 2.0*np.log10((eD)/3.7 + 2.51/(Re*np.sqrt(f)))

# Function to calculate friction factor for turbulent flow using the Colebrook equation
def calculate_friction_factor(Re, eD):
    # Initial guess for f is given by the approximation of the Colebrook equation
    f_initial_guess = 0.02
    # Solve for the root of the Colebrook equation
    f_turbulent, = fsolve(colebrook, f_initial_guess, args=(Re, eD))
    return f_turbulent

# Function to plot the Moody Diagram with a point for a given Re and e/D
def plot_moody_with_point(Re_input, eD_input):
    # Create Moody diagram
    plt.figure(figsize=(10, 8))

    # Laminar flow region
    Re_laminar = np.linspace(1, 2000, 100)
    f_laminar = 64 / Re_laminar
    plt.loglog(Re_laminar, f_laminar, 'k', linewidth=1, label='Laminar Flow')

    # Transitional flow region - plotted as a grey area
    Re_transitional = np.linspace(2000, 4000, 100)
    plt.fill_between(Re_transitional, 64 / Re_transitional, calculate_friction_factor(4000, 0.02), color='grey', alpha=0.3)

    # Turbulent flow region
    Re_turbulent = np.logspace(np.log10(4000), 8, 100)
    relative_roughnesses = [0.0, 0.00005, 0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02]
    for eD in relative_roughnesses:
        f_turbulent = [calculate_friction_factor(Re, eD) for Re in Re_turbulent]
        plt.loglog(Re_turbulent, f_turbulent, label=f'e/D = {eD}')

    # Determine the flow type and calculate the friction factor for the input values
    if Re_input < 2000:
        # Laminar flow
        f_input = 64 / Re_input
        marker = 'o'  # Circle for laminar
    elif 2000 <= Re_input <= 4000:
        # Transitional flow
        f_lam = 64 / Re_input
        f_CB = calculate_friction_factor(Re_input, eD_input)
        mu_f = f_lam + (f_CB - f_lam) * (Re_input - 2000) / 2000
        sigma_f = 0.2 * mu_f
        f_input = np.random.normal(mu_f, sigma_f)
        marker = '^'  # Triangle for transition
    else:
        # Turbulent flow
        f_input = calculate_friction_factor(Re_input, eD_input)
        marker = 'o'  # Circle for turbulent

    # Plot the input point on the Moody Diagram
    plt.loglog(Re_input, f_input, marker=marker, color='red', markersize=10)

    # Labeling the axes and the chart
    plt.xlabel('Reynolds number, Re')
    plt.ylabel('Friction factor, f')
    plt.title('Moody Diagram')
    plt.grid(True, which="both", ls="--")
    plt.legend()

    plt.show()

# Mock user input for demonstration purposes (replace with input() function calls in actual use)
Re_input = 3000  # Example Reynolds number
eD_input = 0.0001  # Example relative roughness

plot_moody_with_point(Re_input, eD_input)
