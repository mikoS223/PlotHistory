import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('protocol3.xlsx')

x = df["Material"]
h = df["H"]
#
# plt.plot(x, df["off1"], "bx",  x, df["off2"], "bx", x, df["off3"], "bx")
# plt.plot(x, df["on1"], "rv", x, df["on2"], "rv", x, df["on3"], "rv")
#
# plt.xticks(x)
#
plt.plot(x, h, "rs")
plt.xlabel("Numer Materiału")
plt.ylabel("Histereza [mm]")


plt.show()
