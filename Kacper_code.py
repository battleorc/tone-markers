import pandas as pd
df = pd.read_csv("Kacper_data/SARC/pol/data.csv")


#How many of each comment there is
tab_cross = pd.crosstab(df["is_sarcasm"], df["is_formal"])

print(tab_cross)

#Percentages
tab_pct = pd.crosstab(
    df["is_sarcasm"],
    df["is_formal"],
    normalize=True
) * 100

print(tab_pct)