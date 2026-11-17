import pandas as pd
import math
from itertools import combinations
# The probability of people sharing a birthday
# Birthday Paradox

df = pd.read_csv("../data/common_player_info.csv")
df.head(5)
df.shape
df["school"].value_counts(ascending=True).sample(10)


# Formula to use in a group of n people
def nCr(n, k):
    f = math.factorial
    return f(n) / (f(k) * f(n - k))


(1 - (364 / 365) ** nCr(10, 2))


def birthday_probability(number_of_people):
    return 1 - (364 / 365) ** nCr(number_of_people, 2)


birthday_probability(15)

# Applying the math to our dataset
GT_school_df = df.loc[df["school"] == "Georgia Tech"]
