import numpy as np
import matplotlib.pyplot as plt
import safeinterp as si

x = [0, 1]
y = [0, 1]
new_x = np.linspace(0, 1, 300)

modes = ["linear", "power", "exp", "logistic", "cos", "sin", "poly2", "poly3"]

plt.figure(figsize=(7,5))
for mode in modes:
    result = si.interp_curve(x, y, new_x, mode=mode)
    plt.plot(new_x, result, label=mode)

plt.title("Comparison of curve modes")
plt.legend()
plt.grid(True)
plt.show()
