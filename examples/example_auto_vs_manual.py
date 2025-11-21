import numpy as np
import matplotlib.pyplot as plt
import safeinterp as si

x = [0, 10, 20, 30]
y = [0, 5, 25, 40]

new_x = np.linspace(0, 30, 400)

# auto
auto = si.interp_curve(x, y, new_x, mode="auto")

# manual segments
segments = [
    {"mode": "linear"},
    {"mode": "power", "k": 2.0},
    {"mode": "cos"},
]
manual = si.interp_curve(x, y, new_x, segments=segments)

plt.figure(figsize=(7,5))
plt.plot(x, y, "o", label="data")
plt.plot(new_x, auto, label="auto-mode")
plt.plot(new_x, manual, label="manual segments")
plt.legend()
plt.title("Auto vs Manual multi-segment interpolation")
plt.grid(True)
plt.show()
