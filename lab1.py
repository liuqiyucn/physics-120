import numpy as np
import matplotlib.pyplot as plt

# ohms section 1.5k resistor

voltage = np.array([5.06,5.98,7.03,8.01,8.94,10.04])
current = np.array([3.44, 4.11, 4.77, 5.47, 6.16, 6.79])
current = current * 10**(-3)
fig, ax = plt.subplots(figsize = (9,9))

ax.scatter(voltage, current, s=60, alpha = 0.7, edgecolors = "red")

b, a = np.polyfit(voltage, current, deg=1)
print(1/b)

xseq = np.linspace(4, 12, num=100)

ax.plot(xseq, a+b*xseq, color="red", lw = 2.5, label = "1.5K resistor")

# ohmn 1k resistor

voltage = np.array([4.99,6.02,7.08,8.03,8.96,10.01])
current = np.array([5.01, 6.06, 7.09, 8.11, 9.06, 10.06])
current = current * 10**(-3)

ax.scatter(voltage, current, s=60, alpha = 0.7, edgecolors = "blue")

b, a = np.polyfit(voltage, current, deg=1)

xseq = np.linspace(4, 12, num=100)

ax.plot(xseq, a+b*xseq, color="blue", lw = 2.5, label = "1K resistor")

ax.set_xlabel("voltage (V)")
ax.set_ylabel("current (A)")
ax.set_title("Resistors Voltage vs Current plot")

print(1/b)

plt.legend()
plt.savefig("1-1.png")

# bulb 

voltage = np.array([1.01,1.96, 2.97,4.02, 4.95, 6.01, 7.04, 8.02, 8.99, 10.03, 11.04])
current = np.array([52.64, 76.92,96.77,112.84,124.69,137.79, 150.87, 161.86, 173.40, 183.55, 193.57])
current = current * 10**(-3)
fig, ax = plt.subplots(figsize = (9,9))

ax.scatter(voltage, current, s=60, alpha = 0.7, edgecolors = "k")

b, a = np.polyfit(voltage, current, deg=1)

xseq = np.linspace(0, 12, num=100)

ax.plot(xseq, a+b*xseq, color="k", lw = 2.5, label = "resistance(1/b)= "+str(1/b))
print(1/b)
ax.set_xlabel("voltage (V)")
ax.set_ylabel("current (A)")
ax.set_title("Lamp Voltage vs Current plot")
plt.legend()
plt.savefig("1-2 lamp.png")

# diode
voltage = np.array([7, 6.92, 6.84, 6.76, 6.71, 6.66, 6.61, 6.57])
current = np.array([6.38,5.32,4.56,3.99,3.55,3.2,2.91,2.67])
current = current * 10**(-3)
fig, ax = plt.subplots(figsize = (9,9))

ax.scatter(voltage, current, s=60, alpha = 0.7, edgecolors = "black")

b, a = np.polyfit(voltage, current, deg=1)

xseq = np.linspace(6.4, 7.2, num=100)

ax.plot(xseq, a+b*xseq, color="red", lw = 2.5, label = "Diode (linear fit)")
ax.legend()
ax.set_xlabel("voltage (V)")
ax.set_ylabel("current (A)")
ax.set_title("Diode Voltage vs Current linear plot")
plt.savefig("1-3 linear.png")

fig, ax = plt.subplots(figsize = (9,9))

ax.scatter(voltage, np.log(current), s=60, alpha = 0.7, edgecolors = "black")

b, a = np.polyfit(voltage, np.log(current), deg=1)

xseq = np.linspace(6.4, 7.2, num=100)

ax.plot(xseq, a+b*xseq, color="red", lw = 2.5, label = "Diode (log-linear fit)")

ax.legend()
ax.set_xlabel("voltage (V)")
ax.set_ylabel("log(current) (log(A))")
ax.set_title("Diode Voltage vs Current log-linear plot")
plt.savefig("1-3 log-linear.png")

#b, a = np.polyfit(current, voltage, deg=1)

#xseq = np.linspace(100*10**-3, 200*10**-3, num=100)

#ax.plot(xseq, a+b*xseq, color="k", lw = 2.5)

# what happens if we put 5V across the diode

print(1/(992*10**-6))