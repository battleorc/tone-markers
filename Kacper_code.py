from scipy.stats import chi2_contingency
import pandas as pd
import numpy as np
import statsmodels.api as sm
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

#Chi Squared

chi2, p, dof, expected = chi2_contingency(tab_cross)

print("chi2:", chi2)
print("p-value", p)
print("degrees of freedom:", dof)
print("expected:")
print(expected)

if p < 0.05:
    print("There is a statistically significant relation between sarcasm and formality")
else:
    print("There is no basis for statistical relation")

#Cramer's V
n = tab_cross.to_numpy().sum()
cramers_v = np.sqrt(chi2 / n)

print("Cramer's V:", cramers_v)

#Logistic Regression
X = df[["is_sarcasm"]]
X = sm.add_constant(X)
y = df["is_formal"]

model = sm.Logit(y, X).fit()

#odds ratio
odds_ratio = np.exp(model.params)

print("Logistic Regression:")
print(model.summary())
print("Odds Ratio")
print(odds_ratio)