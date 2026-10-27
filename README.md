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

## How to run
1. Download ../data/raw/world_dev_indicators.csv
2. Utilizing the functions found in ../src/functions.py run:
    * clean_data (creates a cleaned dataset)
    * reshape_data (reshapes data for analysis)
    * summary_by_country (creates a dataframe of summary statistics for the cleaned and reshaped data)
3. Open ../notebooks/hw_2.ipynb and run all

## Main Findings
**Questions Explored**
1. Which country had the highest average inflation?
    * The country with highest inflation is Zimbabwe with an average inflation from 2020-2025 of 253.48.
2. Which country had the largest GDP growth and in what year?
    * he country with highest GDP growth was Macao SAR, China with a max growth of 75.31 in 2023.

**Visualization**
1. Inflation and GDP growth do not show a clear relationship, although we do see an interesting cluster of countries with low GDP growth and low inflation during the year 2020. This is from the recession caused by the COVID-19 pandemic.

![Inflation vs. GDP growth](../figures/inflation_GDP_growth.png)

2. The effects of the COVID-19 pandemic can also be seen from the view of trade. When looking at the density of trade over time, there is a much denser distribution of trade at lower levels during the COVID-19 pandemic, but as restrictions on trade lifted the density of trade expanded and began to include higher values. 

![Distribution of Trade](../figures/dist_of_trade.png)

3. Inflation and trade appear to have some association. Nations with higher amounts of trade (as % of GDP) tend to have lower inflation. Just from this figure there is not sufficient evidence to imply that trade mitigates inflation, but there does seem to be some association.

![Trade vs Inflation](../figures/trade_inflation.png)

