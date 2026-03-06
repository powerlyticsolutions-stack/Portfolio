"""
Power BI Portfolio — Folder Structure Generator
Author  : Shivendra Singh Bhadauriya (Deepak)
Purpose : Creates a complete, professional GitHub portfolio folder structure
          for showcasing Power BI projects to clients.
Usage   : python setup_portfolio.py
"""

import os
import shutil

# ─────────────────────────────────────────────────────────────
# CONFIGURATION — Add or remove projects as needed
# ─────────────────────────────────────────────────────────────

AUTHOR = {
    "name"       : "Shivendra Singh Bhadauriya (Deepak)",
    "title"      : "BI Solutions Architect and Senior Power BI Developer",
    "linkedin"   : "https://www.linkedin.com/in/shivendra-bhadauriya/",
    "email"      : "Shivendra.ssb@gmail.com",
    "github"     : "YOUR_GITHUB_USERNAME",
}

PROJECTS = [
    {
        "folder"      : "01-Sales-Performance-Dashboard",
        "title"       : "Sales Performance Dashboard",
        "description" : "End-to-end sales analytics covering revenue trends, regional breakdowns, and YoY comparisons.",
        "industry"    : "Retail / FMCG",
        "data_source" : "SQL Server, Excel",
        "pages"       : 5,
        "tags"        : ["Power BI", "DAX", "SQL Server", "Star Schema"],
        "live_link"   : "https://app.powerbi.com/YOUR_SALES_REPORT_LINK",
        "pbix_file"   : "SalesDashboard.pbix",
        "screenshots" : ["overview.png", "regional-breakdown.png", "yoy-comparison.png"],
    },
    {
        "folder"      : "02-Financial-PnL-Report",
        "title"       : "Financial P&L Report",
        "description" : "Dynamic Profit and Loss dashboard with drill-through capabilities and executive-level KPIs.",
        "industry"    : "Finance / Banking",
        "data_source" : "Excel, Power Query",
        "pages"       : 4,
        "tags"        : ["Power BI", "DAX Time Intelligence", "Power Query", "Excel"],
        "live_link"   : "https://app.powerbi.com/YOUR_FINANCE_REPORT_LINK",
        "pbix_file"   : "FinancialPnL.pbix",
        "screenshots" : ["overview.png", "income-statement.png", "variance-analysis.png"],
    },
    {
        "folder"      : "03-HR-Analytics-Dashboard",
        "title"       : "HR Analytics Dashboard",
        "description" : "Workforce insights including attrition analysis, headcount trends, and department performance.",
        "industry"    : "Human Resources",
        "data_source" : "SQL Server, SharePoint",
        "pages"       : 4,
        "tags"        : ["Power BI", "DAX", "SQL", "Row-Level Security"],
        "live_link"   : "https://app.powerbi.com/YOUR_HR_REPORT_LINK",
        "pbix_file"   : "HRAnalytics.pbix",
        "screenshots" : ["overview.png", "attrition.png", "headcount.png"],
    },
    {
        "folder"      : "04-Supply-Chain-Inventory-Tracker",
        "title"       : "Supply Chain and Inventory Tracker",
        "description" : "Real-time inventory monitoring with supplier performance metrics and reorder alerts.",
        "industry"    : "Supply Chain / Logistics",
        "data_source" : "SQL Server, Azure Data Factory",
        "pages"       : 5,
        "tags"        : ["Power BI", "SQL Server", "Power Query", "ETL Pipeline"],
        "live_link"   : "https://app.powerbi.com/YOUR_SUPPLY_CHAIN_REPORT_LINK",
        "pbix_file"   : "SupplyChain.pbix",
        "screenshots" : ["overview.png", "inventory.png", "supplier-performance.png"],
    },
]

ROOT = "PowerBI-Portfolio"

# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────

def make_dir(path):
    os.makedirs(path, exist_ok=True)

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Created: {path}")

def badge(label, message, color, logo="", logoColor="white", labelColor=""):
    label   = label.replace(" ", "_")
    message = message.replace(" ", "_")
    url     = f"https://img.shields.io/badge/{label}-{message}-{color}?style=for-the-badge"
    if logo:        url += f"&logo={logo}&logoColor={logoColor}"
    if labelColor:  url += f"&labelColor={labelColor}"
    return f"![{label}]({url})"

# ─────────────────────────────────────────────────────────────
# PROJECT README GENERATOR
# ─────────────────────────────────────────────────────────────

def generate_project_readme(project, author):
    title_encoded = project["title"].replace(" ", "%20").replace("&", "%26")
    tags_md       = "  ".join([f"`{t}`" for t in project["tags"]])

    screenshots_table = "\n".join([
        f"| {s.replace('.png','').replace('-',' ').title()} "
        f"| ![{s}](./screenshots/{s}) |"
        for s in project["screenshots"]
    ])

    return f"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;customColorList=12,20,24,25,30&amp;height=180&amp;section=header&amp;text={title_encoded}&amp;fontSize=30&amp;fontColor=FFFFFF&amp;fontAlignY=40&amp;desc=Power%20BI%20Project%20by%20Shivendra%20Singh%20Bhadauriya&amp;descColor=00F5FF&amp;descAlignY=62&amp;animation=fadeIn" width="100%" />

</div>

---

## Live Report

<div align="center">

[![View Live Report](https://img.shields.io/badge/Power_BI-View_Live_Report-FF6B00?style=for-the-badge&logo=powerbi&logoColor=white&labelColor=7B00FF)]({project["live_link"]})
[![Download PBIX](https://img.shields.io/badge/Download-PBIX_File-00F5FF?style=for-the-badge&logo=microsoftazure&logoColor=black&labelColor=1a003a)](./{project["pbix_file"]})

</div>

> **Tip for clients:** Click **View Live Report** to interact with the dashboard directly in your browser.

---

## Dashboard Preview

![Overview](./screenshots/overview.png)

| Page | Preview |
|:---|:---|
{screenshots_table}

---

## Business Problem and Solution

> {project["description"]}

Replace this section with the specific business challenge, stakeholders involved,
and how this dashboard delivered measurable value.

---

## Key Features

| Feature | Description |
|:---|:---|
| Dynamic KPI Cards | Core metrics with period-over-period change indicators |
| Drill-through Pages | Click-through from summary to detail views |
| Time Intelligence | MTD, QTD, YTD and YoY comparisons built-in |
| Row-Level Security | Data access controlled by user role |
| Mobile Layout | Optimized for phone and tablet screens |

---

## Data Model

![Data Model](./data-model/model-diagram.png)

Replace the image above with a screenshot of your actual data model from Power BI Desktop.

---

## Key DAX Measures

See full measures reference: [dax-measures/measures.md](./dax-measures/measures.md)

```dax
-- Example: YoY Growth %
Revenue YoY % =
VAR CurrentYear = [Total Revenue]
VAR PriorYear   = CALCULATE( [Total Revenue], SAMEPERIODLASTYEAR( 'Date'[Date] ) )
RETURN
DIVIDE( CurrentYear - PriorYear, PriorYear, 0 )
```

---

## Tech Stack

{tags_md}

---

## Project Info

| Field | Detail |
|:---|:---|
| Industry | {project["industry"]} |
| Data Source | {project["data_source"]} |
| Report Pages | {project["pages"]} |
| Live Report | [Click to View]({project["live_link"]}) |

---

## Author

**{author["name"]}**
{author["title"]}

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]({author["linkedin"]})
[![Email](https://img.shields.io/badge/Gmail-Hire_Me-FF007F?style=for-the-badge&logo=gmail&logoColor=white)](mailto:{author["email"]})

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;customColorList=12,20,24,25,30&amp;height=100&amp;section=footer" width="100%" />
"""

# ─────────────────────────────────────────────────────────────
# MAIN PORTFOLIO README
# ─────────────────────────────────────────────────────────────

def generate_portfolio_readme(projects, author):
    project_rows = "\n".join([
        f"| [{p['title']}](./{p['folder']}/README.md) "
        f"| {p['industry']} "
        f"| {', '.join(p['tags'][:2])} "
        f"| [View Live]({p['live_link']}) |"
        for p in projects
    ])

    return f"""<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;customColorList=12,20,24,25,30&amp;height=200&amp;section=header&amp;text=Power%20BI%20Portfolio&amp;fontSize=40&amp;fontColor=FFFFFF&amp;fontAlignY=38&amp;desc=by%20Shivendra%20Singh%20Bhadauriya%20(Deepak)&amp;descColor=00F5FF&amp;descAlignY=58&amp;animation=fadeIn" width="100%" />

</div>

> **{author["name"]}**
> {author["title"]}
> Power BI portfolio by a Senior BI Solutions Architect — featuring interactive dashboards,
> financial reports, HR analytics, and supply chain solutions built for enterprise clients.

---

## Projects

| Project | Industry | Stack | Live Demo |
|:---|:---|:---|:---|
{project_rows}

---

## About Me

```yaml
Name       : {author["name"]}
Role       : {author["title"]}
Speciality : Business Intelligence, Data Visualization, Analytics Engineering
Contact    : {author["email"]}
LinkedIn   : {author["linkedin"]}
```

---

## DAX Measures Reference

A full reference of advanced DAX patterns used across all projects:
[View DAX Measures Reference](./dax-measures/dax-measures.md)

---

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]({author["linkedin"]})
[![Email](https://img.shields.io/badge/Gmail-Hire_Me-FF007F?style=for-the-badge&logo=gmail&logoColor=white)](mailto:{author["email"]})

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;customColorList=12,20,24,25,30&amp;height=100&amp;section=footer" width="100%" />
"""

# ─────────────────────────────────────────────────────────────
# DAX PLACEHOLDER PER PROJECT
# ─────────────────────────────────────────────────────────────

def generate_project_dax(project):
    return f"""# DAX Measures — {project["title"]}

> Add your project-specific DAX measures here.
> For a full library of reusable patterns, see the root dax-measures folder.

---

## Core Measures

```dax
-- Total Revenue
Total Revenue =
SUMX( Sales, Sales[Quantity] * Sales[Unit Price] )
```

```dax
-- YoY Growth %
Revenue YoY % =
VAR CurrentYear = [Total Revenue]
VAR PriorYear   = CALCULATE( [Total Revenue], SAMEPERIODLASTYEAR( 'Date'[Date] ) )
RETURN
DIVIDE( CurrentYear - PriorYear, PriorYear, 0 )
```

> Replace placeholders above with your actual measures from this project.
"""

# ─────────────────────────────────────────────────────────────
# PLACEHOLDER README FOR SCREENSHOTS AND DATA MODEL
# ─────────────────────────────────────────────────────────────

def placeholder(folder_name):
    return f"""# {folder_name}

Add your files here.

- For **screenshots**: export PNG images from each report page in Power BI Desktop
  (View > Export > Export to PNG)
- For **data-model**: take a screenshot of the Model view in Power BI Desktop
"""

# ─────────────────────────────────────────────────────────────
# BUILD STRUCTURE
# ─────────────────────────────────────────────────────────────

def build_portfolio():
    print(f"\nBuilding Power BI Portfolio structure in: ./{ROOT}/\n")

    # Root folder
    make_dir(ROOT)

    # Root README
    write_file(
        os.path.join(ROOT, "README.md"),
        generate_portfolio_readme(PROJECTS, AUTHOR)
    )

    # Root DAX measures reference folder
    dax_root = os.path.join(ROOT, "dax-measures")
    make_dir(dax_root)

    # Copy dax-measures.md if it exists alongside this script
    src_dax = "dax-measures.md"
    if os.path.exists(src_dax):
        shutil.copy(src_dax, os.path.join(dax_root, "dax-measures.md"))
        print(f"  Copied: dax-measures.md -> {dax_root}/dax-measures.md")
    else:
        write_file(
            os.path.join(dax_root, "dax-measures.md"),
            "# DAX Measures Reference\n\nAdd your master DAX measures here.\n"
        )

    # Each project
    for project in PROJECTS:
        project_path = os.path.join(ROOT, project["folder"])
        make_dir(project_path)

        # Sub-folders
        for sub in ["screenshots", "data-model", "dax-measures"]:
            sub_path = os.path.join(project_path, sub)
            make_dir(sub_path)
            write_file(
                os.path.join(sub_path, "README.md"),
                placeholder(sub)
            )

        # Project README
        write_file(
            os.path.join(project_path, "README.md"),
            generate_project_readme(project, AUTHOR)
        )

        # Project DAX
        write_file(
            os.path.join(project_path, "dax-measures", "measures.md"),
            generate_project_dax(project)
        )

        print(f"  Project folder ready: {project['folder']}/")

    print(f"\nPortfolio structure created successfully!\n")
    print("Next steps:")
    print("  1. Copy your .pbix files into each project folder")
    print("  2. Add dashboard screenshots to each screenshots/ folder")
    print("  3. Screenshot your data model and add to data-model/ folder")
    print("  4. Publish reports to Power BI Service and update live_link URLs in PROJECTS config")
    print("  5. Push the entire folder to GitHub\n")
    print(f"  Folder: ./{ROOT}/")


if __name__ == "__main__":
    build_portfolio()
