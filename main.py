import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Pokemon.csv")
df.head(5)
df.info()


df["type1"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", figsize=(10, 8), cmap="tab20c"
)

df["total"].plot(kind="hist")
df["legendary"].value_counts().plot(kind="pie", autopct="%1.1f%%", cmap="Set3")

len(
    df.loc[df["attack"] > 150].value_counts()
)  # how many pokemon have attack more that 150?

slow_pokemon = df.query("speed <= 10")
len(df.loc[df["sp_defense"] <= 25])
