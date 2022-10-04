import pandas as pd
from pathlib import Path
from glob import glob
from demographic_variables import demographic_variables

# load and combine monthly files
df_combined = None
for f in glob("output/input_*.csv"):
    df_input = pd.read_csv(f)
    date = Path(f).stem[-10:]
    df_input["date"] = date
    if df_combined:
        df_combined = pd.concat([df_combined, df_input])
    else:
        df_combined = df_input

#stratify by demographics
demographics = list(demographic_variables.keys())

df_combined.groupby(['date'] + demographics).agg({"gp_consultation_count":['min','max','sum','avg']})