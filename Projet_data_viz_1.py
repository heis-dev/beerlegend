import pandas as pd

df = pd.read_csv(
    "bars_actifs.csv",
    usecols=["codeCommuneEtablissement"],
    dtype=str
)


comptage = (
    df.groupby("codeCommuneEtablissement")
      .size()
      .reset_index(name="nombre_bars")
      .rename(columns={"codeCommuneEtablissement": "code"})
)

comptage.to_csv("bars_par_commune.csv", index=False)
print(comptage.head())