import pandas as pd
import math

# The probability of people sharing a birthday
# Birthday Paradox

df = pd.read_csv("../data/common_player_info.csv")
df.head(5)

df["school"].value_counts()


# Formula to use in a group of n people
def nCr(n, k):
    f = math.factorial
    return f(n) / (f(k) * f(n - k))


(1 - (364 / 365) ** nCr(10, 2))


def birthday_probability(number_of_people):
    return 1 - (364 / 365) ** nCr(number_of_people, 2)


birthday_probability(15)

# Applying the math to our dataset
