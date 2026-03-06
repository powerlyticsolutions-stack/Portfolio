<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;customColorList=12,20,24,25,30&amp;height=180&amp;section=header&amp;text=Sales%20Performance%20Dashboard&amp;fontSize=32&amp;fontColor=FFFFFF&amp;fontAlignY=40&amp;desc=Power%20BI%20Project%20by%20Shivendra%20Singh%20Bhadauriya&amp;descColor=00F5FF&amp;descAlignY=62&amp;animation=fadeIn" width="100%" />

</div>

---

## Live Report

<div align="center">

[![View Live Report](https://img.shields.io/badge/Power_BI-View_Live_Report-FF6B00?style=for-the-badge&logo=powerbi&logoColor=white&labelColor=7B00FF)](https://app.powerbi.com/YOUR_REPORT_EMBED_LINK)
[![Download PBIX](https://img.shields.io/badge/Download-PBIX_File-00F5FF?style=for-the-badge&logo=microsoftazure&logoColor=black&labelColor=1a003a)](./YourReport.pbix)

</div>

> **Tip for clients:** Click **View Live Report** to interact with the dashboard directly in your browser — no login required.

---

## Dashboard Preview

<!-- Replace the image below with a real screenshot of your dashboard -->
![Dashboard Overview](./screenshots/overview.png)

| Page | Preview |
|:---|:---|
| Overview | ![Overview](./screenshots/overview.png) |
| Regional Breakdown | ![Regional](./screenshots/regional-breakdown.png) |
| YoY Comparison | ![YoY](./screenshots/yoy-comparison.png) |

---

## Business Problem

> Replace this section with the actual business challenge this dashboard solves.

This dashboard was built to address the following business need:

- The sales team had no centralized view of revenue performance across regions
- YoY comparisons were being done manually in Excel, causing delays
- Leadership lacked real-time visibility into top-performing products and territories

---

## Solution and Key Features

| Feature | Description |
|:---|:---|
| Dynamic KPI Cards | Revenue, Units Sold, Avg Order Value — all with MoM change indicators |
| Regional Drill-through | Click any region to drill into city-level performance |
| YoY Comparison | Time intelligence measures comparing current vs prior year |
| Top N Filter | Slicer to show Top 5, 10, or 20 products dynamically |
| Mobile Layout | Optimized view for phone and tablet screens |

---

## Data Model

![Data Model](./data-model/model-diagram.png)

| Table | Type | Description |
|:---|:---|:---|
| Sales | Fact | Transaction-level sales data |
| Date | Dimension | Standard date table with fiscal calendar |
| Product | Dimension | Product hierarchy and categories |
| Region | Dimension | Geography hierarchy — country, state, city |
| Targets | Fact | Monthly sales targets per region |

---

## Key DAX Measures

See the full DAX measures file here: [dax-measures/measures.md](./dax-measures/measures.md)

```dax
-- Total Revenue
Total Revenue =
SUMX( Sales, Sales[Quantity] * Sales[Unit Price] )

-- Revenue YoY Growth %
Revenue YoY % =
VAR CurrentYear = [Total Revenue]
VAR PriorYear   = CALCULATE( [Total Revenue], SAMEPERIODLASTYEAR( 'Date'[Date] ) )
RETURN
DIVIDE( CurrentYear - PriorYear, PriorYear, 0 )

-- Running Total
Running Total Revenue =
CALCULATE(
    [Total Revenue],
    FILTER(
        ALL( 'Date' ),
        'Date'[Date] <= MAX( 'Date'[Date] )
    )
)
```

---

## Tech Stack

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-Advanced-7B00FF?style=for-the-badge&logo=databricks&logoColor=white)
![Power Query](https://img.shields.io/badge/Power_Query-00C9A7?style=for-the-badge&logo=azuredataexplorer&logoColor=white)

---

## Project Info

| Field | Detail |
|:---|:---|
| Industry | Retail / FMCG |
| Data Source | SQL Server, Excel |
| Report Pages | 5 |
| Data Rows | ~2.5 million |
| Refresh Schedule | Daily at 6:00 AM |
| Row-Level Security | Yes — by region |

---

## Author

**Shivendra Singh Bhadauriya (Deepak)**
BI Solutions Architect and Senior Power BI Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shivendra-bhadauriya/)
[![Email](https://img.shields.io/badge/Gmail-Hire_Me-FF007F?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Shivendra.ssb@gmail.com)

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;customColorList=12,20,24,25,30&amp;height=100&amp;section=footer" width="100%" />
