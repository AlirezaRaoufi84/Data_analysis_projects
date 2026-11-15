import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Filtering and Sorting with Pokemon - start
df = pd.read_csv("../data/Pokemon.csv")
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
df.loc[df["legendary"], ["type1"]].value_counts().plot(
    kind="bar", ylabel="quantity"
)  # most common legend type

df["generation"].value_counts().plot(kind="barh")

df.loc[(df["type1"] == "Water") & (df["generation"].isin([1, 2, 3]))].sort_values(
    "total", ascending=False
).head(3)  # strongest water type by total from first 3 generations

df.loc[
    ((df["type1"] == "Dragon") | (df["type2"] == "Dragon"))
    & (df["generation"].isin([5, 6]))
].sort_values("total", ascending=False).head(
    3
)  # strongest dragon type by total from last two generations

most_op_fire_poks = df.loc[
    ((df["type1"] == "Fire") & (df["attack"] > 100))
].sort_values("total", ascending=False)

water_fly_poks = df.loc[
    (df["type1"] == "Fire") & (df["type2"] == "Flying")
].sort_values(
    "total", ascending=False
)  # all pokemons with type1 water and type2 flying

legendary_fire_df = df.loc[
    (df["type1"] == "Fire") & (df["legendary"]), ["name", "attack", "generation"]
]

df.loc[df["speed"]].sort_values("speed", ascending=False)

ax = df["speed"].plot(kind="hist", figsize=(8, 5), bins=100, xlabel="Speed")
ax.axvline(df["speed"].quantile(0.05), color="red")
ax.axvline(df["speed"].quantile(0.95), color="red")

bottom_5, top_5 = df["speed"].quantile(0.05), df["speed"].quantile(0.95)
slow_fast_pok = df.loc[(df["speed"] < bottom_5) | (df["speed"] > top_5)]

# Filtering and Sorting with Pokemon - done
