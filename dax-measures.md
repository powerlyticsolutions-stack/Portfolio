# DAX Measures Reference
**Author:** Shivendra Singh Bhadauriya (Deepak)
**Role:** BI Solutions Architect and Senior Power BI Developer

> A curated collection of advanced DAX measures used across Power BI projects.
> Each measure includes purpose, syntax, and usage notes.

---

## Table of Contents

1. [Sales and Revenue](#1-sales-and-revenue)
2. [Time Intelligence](#2-time-intelligence)
3. [Running Totals and Cumulative](#3-running-totals-and-cumulative)
4. [Ranking and Top N](#4-ranking-and-top-n)
5. [Ratio and Percentage](#5-ratio-and-percentage)
6. [Dynamic Titles and Labels](#6-dynamic-titles-and-labels)
7. [Financial KPIs](#7-financial-kpis)
8. [HR Analytics](#8-hr-analytics)
9. [Advanced Patterns](#9-advanced-patterns)

---

## 1. Sales and Revenue

### Total Revenue
```dax
Total Revenue =
SUMX( Sales, Sales[Quantity] * Sales[Unit Price] )
```
> Iterates the Sales table row by row and multiplies quantity by unit price before summing.

---

### Total Orders
```dax
Total Orders =
DISTINCTCOUNT( Sales[Order ID] )
```

---

### Average Order Value
```dax
Avg Order Value =
DIVIDE( [Total Revenue], [Total Orders], 0 )
```

---

### Revenue After Discount
```dax
Revenue After Discount =
SUMX(
    Sales,
    Sales[Quantity] * Sales[Unit Price] * ( 1 - Sales[Discount %] )
)
```

---

### Gross Profit
```dax
Gross Profit =
[Total Revenue] - SUMX( Sales, Sales[Quantity] * Sales[Cost Price] )
```

---

### Gross Profit Margin %
```dax
Gross Profit Margin % =
DIVIDE( [Gross Profit], [Total Revenue], 0 )
```

---

## 2. Time Intelligence

### Revenue Last Year (SPLY)
```dax
Revenue LY =
CALCULATE( [Total Revenue], SAMEPERIODLASTYEAR( 'Date'[Date] ) )
```

---

### YoY Growth Amount
```dax
Revenue YoY Change =
[Total Revenue] - [Revenue LY]
```

---

### YoY Growth Percentage
```dax
Revenue YoY % =
VAR CurrentYear = [Total Revenue]
VAR PriorYear   = [Revenue LY]
RETURN
DIVIDE( CurrentYear - PriorYear, PriorYear, 0 )
```

---

### Month-to-Date Revenue
```dax
Revenue MTD =
CALCULATE( [Total Revenue], DATESMTD( 'Date'[Date] ) )
```

---

### Quarter-to-Date Revenue
```dax
Revenue QTD =
CALCULATE( [Total Revenue], DATESQTD( 'Date'[Date] ) )
```

---

### Year-to-Date Revenue
```dax
Revenue YTD =
CALCULATE( [Total Revenue], DATESYTD( 'Date'[Date] ) )
```

---

### Prior Month Revenue
```dax
Revenue Prior Month =
CALCULATE( [Total Revenue], DATEADD( 'Date'[Date], -1, MONTH ) )
```

---

### MoM Growth %
```dax
Revenue MoM % =
VAR CurrentMonth = [Total Revenue]
VAR PriorMonth   = [Revenue Prior Month]
RETURN
DIVIDE( CurrentMonth - PriorMonth, PriorMonth, 0 )
```

---

### Rolling 3-Month Average
```dax
Revenue Rolling 3M Avg =
CALCULATE(
    AVERAGEX(
        DISTINCT( 'Date'[Month Year] ),
        [Total Revenue]
    ),
    DATESINPERIOD( 'Date'[Date], LASTDATE( 'Date'[Date] ), -3, MONTH )
)
```

---

## 3. Running Totals and Cumulative

### Cumulative Revenue (All Time)
```dax
Cumulative Revenue =
CALCULATE(
    [Total Revenue],
    FILTER(
        ALL( 'Date' ),
        'Date'[Date] <= MAX( 'Date'[Date] )
    )
)
```

---

### YTD Cumulative with Year Reset
```dax
Cumulative Revenue YTD =
CALCULATE(
    [Total Revenue],
    FILTER(
        ALL( 'Date' ),
        'Date'[Year]         =  MAX( 'Date'[Year] ) &&
        'Date'[Day of Year]  <= MAX( 'Date'[Day of Year] )
    )
)
```

---

## 4. Ranking and Top N

### Product Rank by Revenue
```dax
Product Rank =
IF(
    HASONEVALUE( Product[Product Name] ),
    RANKX(
        ALL( Product[Product Name] ),
        [Total Revenue],
        ,
        DESC,
        DENSE
    )
)
```

---

### Is Top N Product (Dynamic)
```dax
Is Top N =
VAR SelectedN = SELECTEDVALUE( TopN[N Value], 10 )
RETURN
IF( [Product Rank] <= SelectedN, 1, 0 )
```
> Use with a disconnected TopN table containing values like 5, 10, 20 for a dynamic slicer.

---

### Top N Revenue
```dax
Top N Revenue =
CALCULATE(
    [Total Revenue],
    TOPN( 10, ALL( Product[Product Name] ), [Total Revenue] )
)
```

---

## 5. Ratio and Percentage

### % of Total Revenue
```dax
Revenue % of Total =
DIVIDE(
    [Total Revenue],
    CALCULATE( [Total Revenue], ALL( Product ) ),
    0
)
```

---

### % of Category Revenue
```dax
Revenue % of Category =
DIVIDE(
    [Total Revenue],
    CALCULATE( [Total Revenue], ALLEXCEPT( Product, Product[Category] ) ),
    0
)
```

---

### Target Achievement %
```dax
Target Achievement % =
DIVIDE( [Total Revenue], SUM( Targets[Target Amount] ), 0 )
```

---

## 6. Dynamic Titles and Labels

### Dynamic Report Title
```dax
Report Title =
VAR SelectedRegion  = SELECTEDVALUE( Region[Region Name], "All Regions" )
VAR SelectedYear    = SELECTEDVALUE( 'Date'[Year], "All Years" )
RETURN
"Sales Performance  |  " & SelectedRegion & "  |  " & SelectedYear
```

---

### KPI Status Label
```dax
KPI Status =
VAR Growth = [Revenue YoY %]
RETURN
SWITCH(
    TRUE(),
    Growth >= 0.10,  "Strong Growth",
    Growth >= 0,     "Steady",
    Growth >= -0.05, "Slight Decline",
    "Needs Attention"
)
```

---

### Arrow Indicator
```dax
Trend Arrow =
VAR Growth = [Revenue YoY %]
RETURN
IF( Growth >= 0, "▲ " & FORMAT( Growth, "0.0%" ), "▼ " & FORMAT( Growth, "0.0%" ) )
```

---

## 7. Financial KPIs

### EBITDA
```dax
EBITDA =
[Gross Profit]
    - SUM( Expenses[Operating Expenses] )
    + SUM( Expenses[Depreciation] )
    + SUM( Expenses[Amortization] )
```

---

### Net Profit Margin %
```dax
Net Profit Margin % =
DIVIDE(
    [Total Revenue] - SUM( Expenses[Total Expenses] ),
    [Total Revenue],
    0
)
```

---

### Budget Variance
```dax
Budget Variance =
[Total Revenue] - SUM( Budget[Budgeted Revenue] )
```

---

### Budget Variance %
```dax
Budget Variance % =
DIVIDE( [Budget Variance], SUM( Budget[Budgeted Revenue] ), 0 )
```

---

## 8. HR Analytics

### Headcount
```dax
Headcount =
CALCULATE(
    COUNTROWS( Employees ),
    Employees[Status] = "Active"
)
```

---

### Attrition Rate
```dax
Attrition Rate =
DIVIDE(
    CALCULATE( COUNTROWS( Employees ), Employees[Status] = "Resigned" ),
    [Headcount] + CALCULATE( COUNTROWS( Employees ), Employees[Status] = "Resigned" ),
    0
)
```

---

### Avg Tenure (Years)
```dax
Avg Tenure Years =
AVERAGEX(
    FILTER( Employees, Employees[Status] = "Active" ),
    DATEDIFF( Employees[Joining Date], TODAY(), YEAR )
)
```

---

### New Hires This Month
```dax
New Hires MTD =
CALCULATE(
    COUNTROWS( Employees ),
    DATESMTD( 'Date'[Date] ),
    Employees[Status] = "Active"
)
```

---

## 9. Advanced Patterns

### SWITCH with Measure Selector (Field Parameter Alternative)
```dax
Selected Metric =
VAR Selection = SELECTEDVALUE( MetricSelector[Metric], "Revenue" )
RETURN
SWITCH(
    Selection,
    "Revenue",       [Total Revenue],
    "Orders",        [Total Orders],
    "Avg Order",     [Avg Order Value],
    "Gross Profit",  [Gross Profit],
    BLANK()
)
```

---

### What-If Scenario (Price Increase)
```dax
Adjusted Revenue =
VAR PriceIncrease = SELECTEDVALUE( 'Price Increase %'[Value], 0 ) / 100
RETURN
[Total Revenue] * ( 1 + PriceIncrease )
```

---

### Inactive Relationship Measure
```dax
Revenue by Ship Date =
CALCULATE(
    [Total Revenue],
    USERELATIONSHIP( Sales[Ship Date], 'Date'[Date] )
)
```

---

### Last Refresh Timestamp
```dax
Last Refreshed =
"Data last updated: " & FORMAT( NOW(), "DD MMM YYYY, HH:MM AM/PM" )
```

---

*All measures written and tested by Shivendra Singh Bhadauriya (Deepak)*
*Senior Power BI Developer and BI Solutions Architect*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shivendra-bhadauriya/)
[![Email](https://img.shields.io/badge/Gmail-Contact-FF007F?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Shivendra.ssb@gmail.com)
