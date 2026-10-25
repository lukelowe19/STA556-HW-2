import pandas as pd
def clean_data(data):
    df = data.dropna(subset=["Series Code"]).copy()
    df.columns = [c.split(" [")[0] for c in df.columns]
    df = df.rename(columns={
        "Country Name": "country",
        "Country Code": "country_code",
        "Series Name": "series_name",
        "Series Code": "series_code",
    })
    year_cols = [c for c in df.columns if c.isdigit()]
    df[year_cols] = df[year_cols].apply(pd.to_numeric, errors="coerce")
    return df.reset_index(drop=True)

def melt_data(data):
    indicators = {
        "NY.GDP.MKTP.KD.ZG": "gdp_growth",
        "FP.CPI.TOTL.ZG": "inflation",
        "SL.UEM.TOTL.NE.ZS": "unemployment",
        "FS.AST.PRVT.GD.ZS": "private_credit",
        "NE.TRD.GNFS.ZS": "trade",
    }
    year = [c for c in data.columns if str(c).isdigit()]
    long = data.melt(
        id_vars = ["country","country_code","series_code"],
        value_vars = year,
        var_name = "year",
        value_name = "value",
    )
    long["year"] = long["year"].astype(int)
    wide = (
        long.set_index(["country", "country_code", "series_code", "year"])["value"]
        .unstack("series_code")
        .reset_index()
    )
    wide.columns.name = None
    wide = wide.rename(columns = indicators)

    return wide


def summary(data):
    indicators = ["gdp_growth", "inflation", "unemployment", "private_credit", "trade"]
    by_country = data.groupby("country")[indicators]
    count = by_country.count()
    mean = by_country.mean().round(2)
    median = by_country.median().round(2)
    distribution = by_country.agg(["min","max","std"]).round(2)
    return {"count": count, "mean": mean, "median": median,
            "distribution": distribution}


