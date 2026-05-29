import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("inflation.csv")
print(df.head())

plt.figure(figsize = (10, 8))

#Inflation
plt.subplot(5,1,1)
plt.plot(df["Years"], df["Japan"], label = "Japan")
plt.plot(df["Years"], df["Philippines"], label = "Philippines")
df["Japan MA"] = df["Japan"].rolling(5).mean()
plt.plot(df["Years"], df["Japan MA"], linestyle = "--", label = "Japan MA")
df["Philippines MA"] = df["Philippines"].rolling(5).mean()
plt.plot(df["Years"], df["Philippines MA"], linestyle = "--", label = "Philippines MA")
plt.xlabel("Years")
plt.ylabel("Inflation ($)")
plt.title("Inflation Comparison: Japan vs Philippines")
plt.legend()
plt.grid()

#Differences
plt.subplot(5,1,2)
df["Differences"] = df["Japan"] - df["Philippines"]
plt.plot(df["Years"], df["Differences"], label = "Inflation Gap")
plt.xlabel("Years")
plt.ylabel("Inflation Gap($)")
plt.title("Inflation Gap: Japan - Philippines")
plt.grid()

#Growth Rate
plt.subplot(5,1,3)
df["Japan Growth"] = df["Japan"].pct_change()
plt.plot(df["Years"], df["Japan Growth"], label = "Japan Growth")
df["Philippines Growth"] = df["Philippines"].pct_change()
plt.plot(df["Years"], df["Philippines Growth"], label = "Philippines Growth")
df["Japan Growth MA"] = df["Japan Growth"].rolling(5).mean()
plt.plot(df["Years"], df["Japan Growth MA"], linestyle = "--", label = "Japan Growth MA")
df["Philippines Growth MA"] = df["Philippines Growth"].rolling(5).mean()
plt.plot(df["Years"], df["Philippines Growth MA"], linestyle = "--", label = "Philippines Growth MA")
plt.xlabel("Years")
plt.ylabel("Growth rate")
plt.title("Inflation Growth Rate Comparison: Japan vs Philippines")
plt.legend()
plt.grid()

#Ratio
plt.subplot(5,1,4)
df["Ratio"] = df["Philippines"] / df["Japan"]
plt.plot(df["Years"], df["Ratio"], label = "Inflation Ratio")
df["Ratio MA"] = df["Ratio"].rolling(5).mean()
plt.plot(df["Years"], df["Ratio MA"], linestyle = "--", label = "Ratio MA")
plt.xlabel("Years")
plt.ylabel("Inflation Ratio ($)")
plt.title("Inflation Ratio: Japan vs Philippines")
plt.legend()
plt.grid()

#Scattergram
plt.subplot(5,1,5)
plt.scatter(df["Japan"], df["Philippines"])
m, b = np.polyfit(df["Japan"], df["Philippines"], 1)
plt.plot(df["Japan"], m*df["Japan"] + b)
plt.text(df["Japan"].min(), df["Philippines"].max(), f"slope: {m:.3f}")
correlation = np.corrcoef(df["Japan"], df["Philippines"]) [0,1]
print(f"correlation: {correlation:.3f}")
plt.text(df["Japan"].min(), df["Philippines"].max()-10, f"correlation: {correlation:.3f}")
plt.xlabel("Japan")
plt.ylabel("Philippines")
plt.title("Relationship Between Japan and Philippines Inflation")
plt.grid()

plt.tight_layout()
plt.show()

#Title: Inflation Comparison: Japan vs Philippines (World Bank Data)
#Using the real life data from World Bank Data, we can see that the inflation in th Philippine is slightly higher than Japan throughout the time period recorded.
#There is a peak in inflation at around 1954 in the Philippines as they experienced severe economic crisis due to political instability, high oil prices, and expansion of the money supply
#The correlation coefficient value of 0.396 represents a weak positive relationship between Japan and the Philippine's inflation, suggesting that their inflation movements are not synchronized
