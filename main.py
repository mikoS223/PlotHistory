import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('fotoelektryka.xlsx')

x = df["deg"]

#
# plt.plot(x, df["off1"], "bx",  x, df["off2"], "bx", x, df["off3"], "bx")
# plt.plot(x, df["on1"], "rv", x, df["on2"], "rv", x, df["on3"], "rv")

# plt.plot(x, df["off1"], "bx", label="wyłączenie")
# plt.plot(x, df["on1"], "rv", label="załączenie")
# plt.legend()
#
# plt.plot(x, df["off2"], "bx", )
# plt.plot(x, df["on2"], "rv", )
# plt.plot(x, df["off3"], "bx", )
# plt.plot(x, df["on3"], "rv", )

#plt.plot(x, abs(df["mih"]), "s")
plt.plot(x, df["P"])
plt.plot(x, df["P"], "s")
# plt.plot(x, df["I"], label="")
# plt.plot(x, df["P"], label="")

plt.xticks(x)

#plt.plot(x, h, "rs")
plt.xlabel("Odchylenie od prostopadłości [°]")
plt.ylabel("Moc [mW]")


plt.show()
