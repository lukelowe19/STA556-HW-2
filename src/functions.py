import pandas as pd
def clean_data(data):
    """Clean Data
    Input: Raw data
    Takes raw data and cleans it. It removes the blank footer rows at the bottom of the dataset. Makes the years more readable and interpretable
    Renames columns, and takes missing values and encodes them as NaN instead of "..".
    Output: Cleaned dataset.
    
    """
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


def reshape_data(data):
    """
    Reshape Data
    Input: Cleaned data
    Cleans data and reshapes it so that the columns are now the year, followed by the macroeconomic indicators.
    Output: Reshaped data for easier analysis.

    """
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


def summary_by_country(data):
    """
    Summary by Country
    Input: Reshaped data
    Gives mean, median, count, and distribution by country.
    Output: Dataframe of summary statistics

    """
    indicators = ["gdp_growth", "inflation", "unemployment", "private_credit", "trade"]
    summary = (
        data.groupby("country")[indicators]
        .agg(["count", "mean", "median", "min", "max", "std"])
        .round(2)
    )
    summary.columns = [f"{ind}_{stat}" for ind, stat in summary.columns]
    return summary


