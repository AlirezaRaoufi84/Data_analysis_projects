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
legendary_plot = (
    df["legendary"].value_counts().plot(kind="pie", autopct="%1.1f%%", cmap="Set3")
)

len(
    df.loc[df["attack"] > 150].value_counts()
)  # how many pokemon have attack more that 150?

slow_pokemon = df.query("speed <= 10")

len(df.loc[df["sp_defense"] <= 25])

legendary_df = df.loc[df["legendary"]]
legendary_df.head(5)

ax = sns.scatterplot(data=df, x="defense", y="attack")
df.sort_values(by="defense", ascending=False).head(3)
fire_fly_pok = df.loc[(df["type1"] == "Fire") & (df["type2"] == "Flying")]
len(fire_fly_pok)  # 8

df.loc[(df["type1"] == "Poison") | (df["type2"] == "Poison")]
df.loc[df["type1"] == "Ice"].sort_values(by="defense", ascending=False).head(3)

df.loc[df["legendary"], ["type1"]].value_counts().head(1)  # most common legend type
