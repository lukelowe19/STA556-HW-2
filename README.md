# STA556-HW-2
## Purpose
This homework is an exploratory data analysis of a World Bank World Development Indicators. The data is a collection of macroeconomic indicators from 2020-2025, with 266 unique countries or regions included.

## Data Source
- **Source**: World Bank, World development indicators, downloaded as CSV from this [DataBank](https://databank.worldbank.org/source/world-development-indicators)
- **Local File**: ../data/raw/world_dev_indicators.csv

| Column Name | Series Code | Definition |
|---|---|---|
| gdp_growth | NY.GDP.MKTP.KD.ZG | GDP growth (annual %)|
| inflation | FP.CPI.TOTL.ZG | Inflation, consumer prices (annual %)|
| unemployment | SL.UEM.TOTL.NE.ZS | Unemployment, total (% of labor force, national estimate) |
| private_credit | FS.AST.PRVT.GD.ZS |  Domestic credit to private sector (% of GDP) |
| trade | NE.TRD.GNFS.ZS | Trade (% of GDP) |

## Repo Structure
```
STA556-HW-2/
├── README.md
├── data/
│   ├── raw/       # original dataset
│   └── processed/ # cleaned and processed dataset
├── notebooks/
    └── hw_2.ipynb # analysis notebook
├── src/
│   └── functions.py #cleaning and summary functions
└── figures/         # plots used in analysis

```
