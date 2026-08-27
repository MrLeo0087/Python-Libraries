# Pandas Practice — 10 Client Projects (114 Tasks)

You're working as a **freelance data analyst**. Ten different "clients" have sent over a dataset and a list of things they want done. Each project uses a real, well-known dataset from Kaggle. Projects are roughly ordered **easy → hard**, with the last one being a full messy-data cleaning job.

Together, the 10 projects touch every major pandas area: I/O, inspection, indexing/selection, filtering, sorting, missing data, duplicates, string methods, `apply`/`map`, dtype conversion, `groupby`/`agg`/`transform`, `merge`/`join`/`concat`, `pivot_table`/`melt`/`crosstab`/`unstack`, MultiIndex, datetime/`resample`/`rolling`/`shift`, binning (`cut`/`qcut`), categorical dtype, outlier handling, and exporting. A coverage map is at the bottom so you can double check nothing was skipped.

## How to use this

1. Go to the Kaggle link for a project, download the CSV(s) (you'll need a free Kaggle account; click "Download" on the dataset page, or use the Kaggle API: `kaggle datasets download -d <dataset-slug>`).
2. Load it into a fresh notebook/script.
3. Work through the numbered tasks **in order** — later tasks in a project sometimes build on earlier ones (e.g., "using the column you created in task 3...").
4. No answer key is included on purpose — that's the point of practice. When you're done with a project (or stuck on a specific task), paste your code here and I'll review it, debug it, or explain the concept you're missing.
5. Some tasks are intentionally a little under-specified (real client requests are like that) — make a reasonable judgment call, and be ready to explain *why* you chose that approach.

---

## Project 1 — Meridian Insurance Co. (Titanic passenger data)
**Difficulty:** Easy
**Dataset:** [Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
**Brief:** *"We're an actuarial team modeling historical risk data. Give us a clean, well-understood view of the Titanic passenger list before we build anything on top of it."*
**Focus:** reading data, inspection, `loc`/`iloc`, filtering, missing values, `value_counts`, `cut`, sorting, basic `groupby`, exporting

1. Load the dataset and display the first 8 rows and the last 5 rows.
2. Print the shape, column names, and dtype of every column.
3. Use `.info()` and `.describe()` to summarize the dataset; note in a comment which columns have missing values and how many.
4. Select only `Name`, `Sex`, `Age`, and `Survived` into a new DataFrame.
5. Using `.loc`, get all passengers older than 60. Using `.iloc`, get rows 100 through 110.
6. Filter to show only female, 1st-class passengers who survived.
7. Count how many passengers embarked from each port (`Embarked`) with `value_counts()`, including missing values in the count.
8. Fill missing `Age` with the median age, fill missing `Embarked` with the most frequent port, and drop the `Cabin` column entirely (it's mostly missing).
9. Create an `AgeGroup` column that bins `Age` into `Child` (0–12), `Teen` (13–19), `Adult` (20–59), `Senior` (60+) using `pd.cut()`.
10. Sort by `Fare` descending and show the top 10 highest-paying passengers.
11. Group by `Pclass` and `Sex` together and calculate the mean survival rate for each combination.
12. Export the cleaned dataset to `cleaned_titanic.csv` without the index column.

---

## Project 2 — PixelMetrics Analytics (video game sales)
**Difficulty:** Easy–Medium
**Dataset:** [Video Game Sales](https://www.kaggle.com/datasets/gregorut/videogamesales)
**Brief:** *"We advise publishers on where to invest. We need the historical sales numbers sliced by genre, platform, and region."*
**Focus:** `nlargest`, `groupby`+`agg`, `pivot_table`, `value_counts`, `rank`, `idxmax`, dtype cleanup

1. Load `vgsales.csv` and check for missing values in each column.
2. Find the top 10 best-selling games globally using `nlargest()` on `Global_Sales`.
3. Group by `Genre` and calculate total `Global_Sales` per genre, sorted descending.
4. Build a `pivot_table` with `Platform` as rows, `Genre` as columns, and the mean `Global_Sales` as values.
5. Find which `Publisher` has released the most games using `value_counts()`.
6. Create a `TopRegion` column that shows which region (`NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`) contributed the most for each game, using `idxmax()` across those four columns.
7. Filter to games released after 2010 and find the best-selling genre in that period.
8. Use `rank()` to add a `GlobalRank` column ranking games by `Global_Sales` descending (1 = highest).
9. Drop rows where `Year` is missing, then convert `Year` to an integer dtype.
10. Using `groupby().agg()`, compute min, max, and mean of `Global_Sales` per `Platform` in a single call, and rename the resulting columns.
11. Create a pivot table showing total `Global_Sales` with `Genre` as rows and a `Decade` column (derived from `Year`, e.g. 1990s/2000s/2010s) as columns.

---

## Project 3 — GlobalPulse Research (World Happiness Report, 2015–2019)
**Difficulty:** Medium
**Dataset:** [World Happiness Report](https://www.kaggle.com/datasets/unsdsn/world-happiness) — files `2015.csv` through `2019.csv`
**Brief:** *"We publish an annual well-being index. Stitch five years of reports into one clean trend dataset — the column names have drifted year to year, so don't just concat blindly."*
**Focus:** schema alignment, `rename`, `concat`, `merge`, long-format reshaping, `pivot`

1. Load all five yearly CSVs (2015–2019) into separate DataFrames.
2. Inspect the column names of each year and note which ones differ between years (e.g., `Happiness Rank` vs `Overall rank`, `Happiness Score` vs `Score`, `Country` vs `Country or region`).
3. Standardize the column names across all five DataFrames so they match (e.g., rename everything to `Country`, `Score`, `Rank`).
4. Add a `Year` column to each DataFrame (a constant value per file) before combining them.
5. Use `pd.concat()` to stack all five years into one long-format DataFrame.
6. Use `merge()` to combine just the 2015 and 2019 data on `Country`, keeping only countries present in both, and use `suffixes` to distinguish the two `Score` columns.
7. From the merged 2015/2019 table, calculate the change in `Score` for each country and find the 10 countries with the biggest improvement.
8. From the long-format DataFrame, group by `Country` and compute the average `Score` across all 5 years.
9. Identify which countries are missing from at least one of the five years (i.e., not present in all five original DataFrames).
10. Pivot the long-format DataFrame so `Country` is the index, `Year` is the columns, and `Score` is the values.

---

## Project 4 — Vantage HR Consulting (IBM employee attrition)
**Difficulty:** Medium
**Dataset:** [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
**Brief:** *"Turnover is costing us. Build a profile of who's leaving and why, broken down by department, role, and income."*
**Focus:** `crosstab`, category dtype, `cut`, `apply` with a custom function, `groupby().transform()`, correlation, filtering small groups

1. Identify columns that contain only a single unique value across the whole dataset (e.g., `EmployeeCount`, `Over18`, `StandardHours`) and drop them — they add nothing analytically.
2. Convert `Attrition` and `OverTime` to `category` dtype (or boolean, your call — justify it).
3. Use `crosstab()` to build a table of `Attrition` counts by `Department`.
4. Use `crosstab()` with `normalize='index'` to get the attrition **rate** (%) per `Department`.
5. Group by `JobRole` and calculate mean `MonthlyIncome` and mean `Age`, sorted by income descending.
6. Use `pd.cut()` to bin `Age` into 5 equal-width groups, then find the attrition rate per age bin.
7. Use `apply()` with a custom function to create an `IncomeLevel` column labeling `MonthlyIncome` as `'Low'`, `'Medium'`, or `'High'` based on thresholds you choose and justify.
8. Encode `Attrition` as 0/1 and find its correlation with `YearsAtCompany` and `MonthlyIncome`.
9. Group by `Department` and `Gender` together, and calculate the average `JobSatisfaction` for each combination.
10. Use `groupby().transform()` to add a `DeptAvgIncome` column showing each employee's department average income right next to their own income.
11. Find the top 5 `JobRole`s with the highest attrition rate, but only consider roles with at least 20 employees (filter out small, unreliable groups first).

---

## Project 5 — StreamScope Media (Netflix catalog)
**Difficulty:** Medium
**Dataset:** [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
**Brief:** *"We're mapping our content library. We need genres, countries, and durations broken out properly — right now they're all jammed into comma-separated text fields."*
**Focus:** string methods (`str.split`, `str.contains`), `explode()`, datetime parsing, multi-value column handling, duplicates, pivot

1. Check how many missing values exist in `director`, `cast`, and `country`.
2. Fill missing values in `director`, `cast`, and `country` with the string `"Unknown"`.
3. Convert `date_added` to a proper datetime column (watch for leading whitespace in the raw text).
4. Extract the year and month from `date_added` into two new columns, `YearAdded` and `MonthAdded`.
5. Use `str.split()` and `explode()` to turn `listed_in` (comma-separated genres) into one genre per row, then find the 10 most common genres.
6. Use `str.contains()` to find all titles whose `description` mentions "love" (case-insensitive).
7. Split `duration` into a numeric value and a unit (e.g., `"90 min"` → `90` and `"min"`; `"2 Seasons"` → `2` and `"Season"`), producing two new columns.
8. Count Movies vs TV Shows with `value_counts()` and express the result as a percentage.
9. Split and explode the `country` column the same way you did `listed_in`, then find the top 10 countries by number of titles.
10. Group by `rating` and `type` together to find the most common content rating for Movies vs TV Shows.
11. Find and remove fully duplicated rows using `duplicated()` and `drop_duplicates()`.
12. Build a pivot table showing counts of titles added per `YearAdded` (rows) and `type` (columns).

---

## Project 6 — CineMetrics Studio (TMDB 5000 movies + credits)
**Difficulty:** Medium–Hard
**Dataset:** [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) — files `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`
**Brief:** *"Our metadata team exported two files that need to be joined, and half the interesting fields (genres, cast, crew) are dumped as JSON-looking text instead of real columns. Unpack it."*
**Focus:** merging two files, `ast.literal_eval`/`apply` on nested strings, `explode()`, ROI-style feature engineering, `query()`

1. Load both `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`.
2. Merge the two DataFrames into one on the movie id/title — watch for duplicate `title` columns after the merge and handle them with `suffixes`.
3. Use `ast.literal_eval` (or `json.loads` after cleaning quotes) inside an `apply()` call to turn the `genres` column — a string that looks like a list of dicts — into an actual Python list.
4. From the parsed `genres`, extract just the genre names into a `GenreNames` column, then `explode()` it so each movie-genre pair is its own row.
5. Do the same parsing for `cast` and extract only the first-billed (lead) actor's name into a `LeadActor` column.
6. Parse `crew` and extract the director's name into a `Director` column by filtering for the entry where `job == "Director"`.
7. Using the exploded genre table, find the average `budget` and `revenue` per genre, sorted by average revenue descending.
8. Create a `Profit` column (`revenue - budget`) and an `ROI` column (`Profit / budget`), safely handling movies with a `budget` of 0.
9. Find the 10 directors with the highest total revenue across their movies, requiring at least 3 movies directed to qualify.
10. Convert `release_date` to datetime, extract the release decade, and find which decade has the highest average `vote_average`.
11. Use `query()` to filter for movies with `vote_count > 1000` and `vote_average > 7.5`, sorted by `revenue` descending.

---

## Project 7 — RetailIQ Consulting (Superstore sales)
**Difficulty:** Medium–Hard
**Dataset:** [Sample Superstore](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
**Brief:** *"We need a proper sales performance breakdown — by category, region, and month — plus we want to know which sub-categories are actually losing us money."*
**Focus:** multi-level `groupby`, `pivot_table` with `margins`, `transform`, MultiIndex, `resample`, `rolling`, named aggregation, `to_excel`

1. Load the dataset (you may need `encoding='latin1'` or similar for it to read cleanly).
2. Convert `Order Date` and `Ship Date` to datetime, and create a `ShippingDays` column (`Ship Date - Order Date`) as an integer number of days.
3. Group by `Category` and `Sub-Category` together and calculate total `Sales` and total `Profit` for each combination.
4. Build a `pivot_table` with `Region` as rows, `Category` as columns, `Sales` summed as values, and `margins=True` for row/column totals.
5. Use `groupby().transform()` to add a `CategoryAvgProfit` column showing each row's category-level average profit.
6. Set a MultiIndex on `Region` and `State`, then use `.loc` to pull all rows for one specific Region/State pair.
7. Set `Order Date` as the index and `resample()` to monthly totals to build a `Sales` time series.
8. Find the 5 sub-categories with the worst total `Profit` (i.e., losing the most money).
9. Apply a rolling 3-month window to the monthly sales time series to compute a smoothed rolling average.
10. Find which customer `Segment` has the highest average `Discount`, and check with `groupby` whether higher discounts line up with negative `Profit`.
11. Use named aggregation (the `col=('source_col', 'func')` syntax inside `.agg()`) to build a summary table with `TotalSales`, `AvgProfit`, and `OrderCount` per `Region`.
12. Export a summary table (`Region`, `Category`, `TotalSales`, `TotalProfit`) to an Excel file with `to_excel()`.

---

## Project 8 — PublicHealth Analytics Group (COVID-19 case data)
**Difficulty:** Hard
**Dataset:** [COVID-19 Dataset](https://www.kaggle.com/datasets/imdevskp/corona-virus-report) — file `covid_19_clean_complete.csv`
**Brief:** *"We track outbreak trajectories by country. We need daily new-case counts (not just cumulative totals), smoothed trends, and week-over-week growth."*
**Focus:** `resample`, `.diff()`, `.rolling()`, `.shift()`, MultiIndex + `.xs()`, time-indexed `groupby`

1. Load the dataset and convert `Date` to a proper datetime column.
2. Group by `Country/Region` and `Date`, summing `Confirmed`, `Deaths`, and `Recovered` (several countries have multiple province rows per date that need combining first).
3. Filter to a single country, set `Date` as the index, and `resample('W')` to get weekly totals.
4. After grouping by country and sorting by date, use `.diff()` on the cumulative `Confirmed` column to get new daily cases.
5. Apply a 7-day rolling average (`.rolling(7).mean()`) to the new daily cases to smooth the curve.
6. For each country, find the date it first crossed 100,000 confirmed cases, using boolean filtering combined with `groupby`.
7. Build a `pivot_table` with `Date` as rows, `Country/Region` as columns, and `Confirmed` as values, limited to the top 5 countries by total confirmed cases.
8. Calculate the case fatality rate (`Deaths / Confirmed`) per country as of the latest date, sorted descending.
9. Use `groupby()` with multiple aggregation functions to find, per `WHO Region`, the sum of `Confirmed` and the single largest daily increase.
10. Use `.shift(7)` to compare each day's `Confirmed` to the value exactly 7 days earlier, and compute a `WeekOverWeekGrowth` percentage column.
11. Build a MultiIndex DataFrame indexed by `[Country/Region, Date]`, then use `.xs()` to pull out all rows for one country without losing the `Date` level.

---

## Project 9 — UrbanStay Analytics (NYC Airbnb listings)
**Difficulty:** Hard
**Dataset:** [New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)
**Brief:** *"We help hosts price their listings. We need outliers handled properly (not just deleted), a neighborhood pricing profile, and a memory-efficient version of this file — it's getting big."*
**Focus:** memory optimization with `category` dtype, IQR outlier detection, `.clip()`, `.qcut()`, `unstack()`, `.where()`/`.mask()`, correlation

1. Check memory usage with `.info(memory_usage='deep')`, then convert `neighbourhood_group`, `neighbourhood`, and `room_type` to `category` dtype and compare memory usage before/after.
2. Fill missing `reviews_per_month` with 0 (no reviews means 0 per month); decide and apply a strategy for the other columns with missing data (`last_review`, `name`, `host_name`).
3. Find and remove listings with `price == 0` (a real listing can't be free — treat these as data errors).
4. Use the IQR method (Q1, Q3, 1.5×IQR) to identify and count price outliers.
5. Instead of removing them, use `.clip()` to cap `price` at the 1st and 99th percentiles, and compare the mean price before vs. after.
6. Group by `neighbourhood_group` and `room_type` together to find median price per combination, then reshape the result with `.unstack()`.
7. Use `pd.qcut()` to bin `price` into 4 quartile-based groups (`Budget`, `Mid`, `Premium`, `Luxury`) and check how many listings land in each.
8. Find the top 10 hosts by listing count (using `calculated_host_listings_count` vs. counting `host_id` occurrences directly) and check whether the two methods agree.
9. Convert `last_review` to datetime and find how many listings haven't been reviewed in over a year from the most recent date in the dataset.
10. Build a neighborhood profile table with `groupby().agg()`: number of listings, average price, average `minimum_nights`, and average `availability_365`, per `neighbourhood`.
11. Calculate the correlation between `price`, `number_of_reviews`, `minimum_nights`, and `availability_365`, and identify the strongest relationship.
12. Use `.where()` or `.mask()` to flag listings as `'Possible Data Error'` where `minimum_nights > 365`, without removing them from the DataFrame.

---

## Project 10 — Brew & Bean Co. (raw POS export — the messy one)
**Difficulty:** Very Hard / genuinely dirty data
**Dataset:** [Cafe Sales — Dirty Data for Cleaning Training](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training)
**Brief:** *"Our point-of-sale export is a disaster — missing fields, literal `'ERROR'` and `'UNKNOWN'` text instead of blanks, numbers stored as broken text, and some totals that don't even math out. Give us something we can actually report on."*
**Focus:** the full cleaning pipeline — sentinel-value replacement, `pd.to_numeric(errors='coerce')`, cross-column imputation, row-wise `apply`, dedup, dtype locking, before/after data-quality reporting

1. Load the dataset and get a full picture of the mess: run `.info()`, and count exact-match `"ERROR"` and `"UNKNOWN"` string occurrences per column separately from true `NaN` counts.
2. Replace every literal `"ERROR"` and `"UNKNOWN"` string across the whole DataFrame with real `NaN` using `.replace()`.
3. Convert `Quantity`, `Price Per Unit`, and `Total Spent` to numeric dtype with `pd.to_numeric(errors='coerce')`, and report how many *additional* NaNs this introduces (values that weren't valid numbers at all).
4. Write a function that recomputes `Total Spent` as `Quantity × Price Per Unit` whenever `Total Spent` is missing but the other two are present, and apply it.
5. Extend the logic: also recompute a missing `Price Per Unit` from `Total Spent / Quantity`, and a missing `Quantity` from `Total Spent / Price Per Unit`, whenever solvable. Chain all three "fill from the other two" rules and report how many rows were rescued in total.
6. For the `Item` column, use the dataset's known menu price list (or infer typical prices from the clean rows yourself) to fill missing `Item` values by matching `Price Per Unit` back to the item it uniquely identifies, wherever that's possible.
7. Convert `Transaction Date` to datetime with `errors='coerce'` and report how many rows have an unparseable date.
8. Decide and justify a strategy for the remaining unrecoverable missing values in `Payment Method` and `Location` (e.g., fill with `"Unknown"` vs. drop the rows), then implement it.
9. Identify and drop fully duplicated transactions with `drop_duplicates()` (keeping the first occurrence), and report how many rows were removed.
10. Use `.astype()` to lock in final dtypes for every column (numeric, category, datetime) and verify with `.dtypes`.
11. Build a small before/after data-quality report (a DataFrame or dict) showing, per column, the % missing before cleaning vs. after cleaning.
12. Export the final cleaned file as `cleaned_cafe_sales.csv`, and separately export a `rejected_rows.csv` containing any rows you chose to drop entirely, with a `Reason` column explaining why each was dropped.

---

## Pandas topic coverage map

| Topic | Where it's covered |
|---|---|
| I/O (`read_csv`, `to_csv`, `to_excel`) | P1, P7, P10 (read), all projects (write at the end) |
| Inspection (`head`/`tail`/`info`/`describe`/`shape`/`dtypes`) | P1, P10 |
| `loc` / `iloc` / boolean indexing | P1, P7, P8 |
| `query()` | P6 |
| Sorting / `nlargest`/`nsmallest` | P1, P2 |
| Missing data (`isna`, `fillna`, `dropna`) | P1, P4, P5, P9, P10 |
| Duplicates (`duplicated`, `drop_duplicates`) | P5, P10 |
| String methods (`str.split`, `str.contains`, `str.strip`) | P5 |
| `explode()` | P5, P6 |
| `apply()` / custom functions / `ast.literal_eval` | P4, P6, P10 |
| `idxmax` / `rank` | P2 |
| dtype conversion (`astype`, `to_numeric`, `to_datetime`, `category`) | P2, P4, P9, P10 |
| `cut()` / `qcut()` (binning) | P1, P4, P9 |
| `groupby` + `agg` (incl. named aggregation) | P2, P3, P4, P7, P8 |
| `groupby().transform()` | P4, P7 |
| `crosstab()` | P4 |
| `merge()` / `join()` | P3, P6 |
| `concat()` | P3 |
| `pivot()` / `pivot_table()` / `unstack()` | P2, P3, P5, P7, P8, P9 |
| MultiIndex + `.xs()` | P7, P8 |
| Datetime / `.dt` accessor | P5, P6, P7, P8, P9 |
| `resample()` | P7, P8 |
| `.rolling()` | P7, P8 |
| `.diff()` / `.shift()` | P8 |
| Correlation | P4, P9 |
| Outlier handling (IQR, `.clip()`, `.where()`/`.mask()`) | P9 |
| Memory optimization (`category` dtype) | P9 |
| Cross-column imputation / data-quality reporting | P10 |

That's **114 tasks across 10 datasets** — send me your code for any of them whenever you want it checked.
