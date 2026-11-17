import pandas as pd
import math
from itertools import combinations
# The probability of people sharing a birthday
# Birthday Paradox

df = pd.read_csv("../data/common_player_info.csv")
df.head(5)
df.shape
df["school"].value_counts(ascending=False).head(10)


# Formula to use in a group of n people
def nCr(n, k):
    f = math.factorial
    return f(n) / (f(k) * f(n - k))


(1 - (364 / 365) ** nCr(10, 2))


def birthday_probability(number_of_people):
    return 1 - (364 / 365) ** nCr(number_of_people, 2)


birthday_probability(15)

# Applying the math to our dataset
# Combining all the people in our dataset in groups of two based on school == Kentucky
ken_school_df = df.loc[df["school"] == "Kentucky"]
name_df = pd.DataFrame(
    combinations(ken_school_df["display_first_last"], 2),
    columns=("person 1", "person 2"),
)
birthday_df = pd.DataFrame(
    combinations(ken_school_df["birthdate"], 2), columns=("birthdate 1", "birthdate 2")
)

check_df = pd.concat([name_df, birthday_df], axis=1)
check_df.sample(10)
(check_df["birthdate 1"] == check_df["birthdate 2"]).sum()
check_df.loc[(check_df["birthdate 1"] == check_df["birthdate 2"])]

michi_school_df = df.loc[df["school"] == "Michigan"]
print(
    f" the chance of two people who attended Michigan school have the same birthdate is {birthday_probability(50)}"
)
#  the chance of two people who attended Michigan school have the same birthdate is 0.9652914867514426
