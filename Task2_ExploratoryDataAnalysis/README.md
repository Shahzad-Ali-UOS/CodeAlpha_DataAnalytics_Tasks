# Task 2: Exploratory Data Analysis (EDA) on Retail Transactions

## Project Overview
An exploratory data analytics investigation analyzing 1,000 retail transaction records. The analysis identifies key revenue engines, isolates purchasing demographics, monitors seasonal transaction velocity, cleans anomalies via the IQR rule, and conducts statistical hypothesis testing.

## Exploratory Questions Addressed
* How does gross revenue break down across product categories?
* What are the demographic age distributions across purchasing groups?
* How does transaction volume correlate with total monthly revenue?
* Is there a statistically significant spending difference between genders?

## Analytical Workflow
1. **Structural Audit:** Assessed schema, missing data frequencies, and summary spreads.
2. **Data Cleaning:** Imputed missing demographic values and isolated statistical anomalies using the Interquartile Range (IQR).
3. **Visualization & Trend Discovery:**
   * Category sales distributions via Seaborn bar charts.
   * Demographic KDE curves across gender segments.
   * Dual-axis monthly revenue and order volume tracking.
4. **Hypothesis Validation:** Applied two-sample independent Welch's t-tests to evaluate spend disparities.

## Key Insights
* **Revenue Driver:** The **Clothing** and **Electronics** categories generate the highest cumulative gross revenue.
* **Demographic Parity:** Hypothesis testing confirmed no statistically significant difference in mean transaction spend between male and female shoppers ($p > 0.05$).
* **Outliers:** 5 transactions exceeded the upper IQR threshold (£1,500+), representing bulk purchases that should be analyzed as an enterprise customer segment.

## Tech Stack
* **Language:** Python
* **Analytics & Statistics:** Pandas, NumPy, SciPy (`stats.ttest_ind`)
* **Visualization:** Matplotlib, Seaborn