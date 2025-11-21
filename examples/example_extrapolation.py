import numpy as np
import matplotlib.pyplot as plt
import safeinterp as si

x = [0, 10]
y = [2, 5]

new_x = np.linspace(-10, 20, 400)

methods = ["edge", "linear", "power", "exp", "mirror", "auto"]

plt.figure(figsize=(7,5))
for method in methods:
    result = si.interp_curve(x, y, new_x, extrapolate=method)
    plt.plot(new_x, result, label=method)

plt.title("Extrapolation strategies comparison")
plt.legend()
plt.grid(True)
plt.show()
