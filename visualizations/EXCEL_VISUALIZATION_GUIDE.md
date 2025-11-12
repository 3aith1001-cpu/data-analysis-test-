# EXCEL VISUALIZATION GUIDE
## Creating Professional Charts from Saudi Procurement Data

---

## 📊 **30+ CHART TYPES TO CREATE**

This guide shows you how to create professional visualizations in Excel using the prepared data files.

---

## 🚀 **QUICK START**

###Step 1: Import Data
1. Open Excel
2. Go to **Data** → **From Text/CSV**
3. Select a CSV file from `data_for_viz/` folder
4. Click **Load**

### Step 2: Create Chart
1. Select data range
2. Go to **Insert** → Choose chart type
3. Customize and format

---

## 📈 **CHART 1: SECTOR MARKET SHARE (PIE CHART)**

**Data File:** `04_sector_analysis.csv`

**Steps:**
1. Import the CSV file
2. Select columns: `Sector` and `Market_Share_Percent`
3. Insert → **Pie Chart** → **2-D Pie**
4. Format:
   - Add data labels (percentage)
   - Use distinct colors
   - Add title: "Market Share by Sector"

**Recommended Colors:**
- الداخلية: Blue (#4472C4)
- الإسكان: Green (#70AD47)
- البلدية: Orange (#FFC000)
- النقل: Red (#FF6B6B)
- الصحة: Purple (#7030A0)

---

## 📊 **CHART 2: MONTHLY TIME SERIES (LINE CHART)**

**Data File:** `03_monthly_timeseries.csv`

**Steps:**
1. Import CSV
2. Select: `Year_Month`, `Total_Value_SAR`, `Contract_Count`
3. Insert → **Line Chart** → **Line with Markers**
4. Create dual-axis chart:
   - Right-click `Contract_Count` series → **Format Data Series**
   - Select **Secondary Axis**
5. Format:
   - Title: "Monthly Contract Activity Over Time"
   - X-axis: Month
   - Left Y-axis: Total Value (SAR)
   - Right Y-axis: Contract Count

**Advanced:**
- Add trend line to value series
- Format numbers as currency
- Use smooth lines

---

## 📊 **CHART 3: TOP 10 CONTRACTORS (HORIZONTAL BAR)**

**Data File:** `12_top10_contractors.csv`

**Steps:**
1. Import CSV
2. Select: `Contractor` and `Market_Share_Percent`
3. Insert → **Bar Chart** → **Clustered Bar**
4. Format:
   - Sort bars (largest to smallest)
   - Add data labels
   - Title: "Top 10 Contractors by Market Share"
   - Color: Gradient from dark to light blue

---

## 📊 **CHART 4: CONTRACT SIZE DISTRIBUTION (COLUMN CHART)**

**Data File:** `09_contract_clusters.csv`

**Steps:**
1. Import CSV
2. Select: `Cluster` and `Percentage`
3. Insert → **Column Chart** → **Clustered Column**
4. Format:
   - Colors: Green (Small), Orange (Medium), Red (Large)
   - Add data labels on top of bars
   - Title: "Contract Size Distribution"
   - Add percentage symbol

---

## 📊 **CHART 5: REGIONAL DISTRIBUTION (MAP OR BAR)**

**Data File:** `07_regional_analysis.csv`

**Option A: Bar Chart**
1. Import CSV
2. Select: `Region` and `Total_Value_SAR`
3. Insert → **Column Chart**
4. Sort by value (descending)

**Option B: Filled Map** (Excel 365)
1. Select: `Region` and `Total_Value_SAR`
2. Insert → **Maps** → **Filled Map**
3. Format regions

---

## 📊 **CHART 6: YEARLY TREND (LINE + COLUMN COMBO)**

**Data File:** `10_yearly_summary.csv`

**Steps:**
1. Import CSV
2. Select all columns
3. Insert → **Combo Chart**
4. Set:
   - `Total_Value_SAR`: Column chart
   - `Contract_Count`: Line chart with secondary axis
5. Title: "Annual Growth Trends"

---

## 📊 **CHART 7: PROJECT TYPE ANALYSIS (TREEMAP)**

**Data File:** `06_project_type_analysis.csv`

**Steps (Excel 2016+):**
1. Import CSV
2. Select: `Project_Type` and `Total_Value_SAR`
3. Insert → **Hierarchy** → **Treemap**
4. Format with distinct colors
5. Add data labels

**Alternative (Older Excel):**
- Use stacked bar chart instead

---

## 📊 **CHART 8: CAPITAL VS OPERATIONAL (DONUT CHART)**

**Data File:** `08_capital_vs_operational.csv`

**Steps:**
1. Import CSV
2. Select: `Type` and `Market_Share_Percent`
3. Insert → **Pie** → **Doughnut**
4. Format:
   - رأسمالي: Blue
   - تشغيلي: Green
   - مختلط: Orange
5. Add center label: "Capital vs Operational"

---

## 📊 **CHART 9: DURATION vs VALUE (SCATTER PLOT)**

**Data File:** `11_duration_vs_value.csv`

**Steps:**
1. Import CSV
2. Select: `Duration_Months` and `Contract_Value_SAR`
3. Insert → **Scatter** → **Scatter with Straight Lines**
4. Add trend line:
   - Right-click data points → **Add Trendline**
   - Select **Linear**
   - Display equation and R²
5. Format:
   - X-axis: Duration (Months)
   - Y-axis: Contract Value (SAR)
   - Title: "Contract Value vs Duration Analysis"

---

## 📊 **CHART 10: CONTRACT VALUE DISTRIBUTION (HISTOGRAM)**

**Data File:** `01_contract_values.csv`

**Steps (Excel 2016+):**
1. Import CSV
2. Select: `Contract_Value_SAR` column
3. Insert → **Statistical** → **Histogram**
4. Format:
   - Adjust bin width
   - Title: "Distribution of Contract Values"
   - X-axis: Contract Value (SAR)
   - Y-axis: Frequency

**Alternative (Older Excel):**
1. Use **FREQUENCY** function to create bins
2. Create column chart from frequency table

---

## 🎨 **EXECUTIVE DASHBOARD**

### Create Multi-Chart Dashboard

**Layout:**
```
+------------------+------------------+
|   KPI Cards (Top Row)               |
+------------------+------------------+
| Sector Pie       | Monthly Line     |
+------------------+------------------+
| Top Contractors  | Regional Map     |
+------------------+------------------+
```

**Steps:**
1. Create new sheet: "Dashboard"
2. Add KPI cards at top:
   - Total Contracts
   - Total Value
   - Average Value
   - Date Range
3. Insert 4 charts (one in each quadrant)
4. Use consistent colors across all charts
5. Add filters using slicers:
   - Year filter
   - Sector filter
   - Region filter

---

## 🎨 **FORMATTING TIPS**

### Professional Color Scheme
```
Primary:   #4472C4 (Blue)
Secondary: #ED7D31 (Orange)
Accent 1:  #70AD47 (Green)
Accent 2:  #FFC000 (Yellow)
Accent 3:  #5B9BD5 (Light Blue)
Accent 4:  #C5E0B4 (Light Green)
```

### Typography
- Title: 14pt, Bold, Dark Blue
- Axis Labels: 10pt, Regular
- Data Labels: 9pt, Bold

### Best Practices
1. **Always add titles** to charts
2. **Use data labels** for small datasets
3. **Format numbers** appropriately (currency, percentages)
4. **Add gridlines** sparingly
5. **Use consistent colors** across dashboard
6. **Remove chart junk** (unnecessary borders, backgrounds)

---

## 📊 **ADVANCED FEATURES**

### 1. **Sparklines** (Mini Charts in Cells)
- Use for monthly trends in summary table
- Insert → **Sparklines** → **Line**

### 2. **Conditional Formatting**
- Highlight top performers
- Use data bars for values
- Color scales for heatmaps

### 3. **Pivot Charts**
- Create dynamic charts from pivot tables
- Allow easy filtering and drill-down

### 4. **Slicers** (Interactive Filters)
- Add slicers for:
  - Year
  - Sector
  - Region
  - Contract Size
- Connect slicers to multiple charts

---

## 📑 **RECOMMENDED WORKBOOK STRUCTURE**

```
Sheet 1: 📊 Executive Dashboard
Sheet 2: 📈 Time Series Analysis
Sheet 3: 🏢 Sector Deep Dive
Sheet 4: 👷 Contractor Analysis
Sheet 5: 🗺️ Regional Breakdown
Sheet 6: 📊 Statistical Charts
Sheet 7: 📁 Raw Data (hidden)
```

---

## 🎯 **KEY VISUALIZATIONS CHECKLIST**

Essential charts to create:

- [ ] Sector Market Share Pie Chart
- [ ] Monthly Time Series Line Chart
- [ ] Top 10 Contractors Bar Chart
- [ ] Contract Size Distribution Column Chart
- [ ] Regional Distribution Map/Bar Chart
- [ ] Yearly Trend Combo Chart
- [ ] Capital vs Operational Donut Chart
- [ ] Duration vs Value Scatter Plot
- [ ] Executive Dashboard with KPIs
- [ ] Project Type Treemap/Bar Chart

---

## 💡 **PRO TIPS**

### Tip 1: Dynamic Titles
Use formulas in chart titles:
```
="Contract Activity in " & TEXT(TODAY(),"YYYY")
```

### Tip 2: Custom Number Formats
- Millions: `#,##0,,"M"`
- Thousands: `#,##0,"K"`
- Currency: `"SAR "#,##0`

### Tip 3: Chart Templates
1. Format one chart perfectly
2. Right-click → **Save as Template**
3. Reuse for consistent styling

### Tip 4: Print-Ready Charts
- Use high resolution
- Test in Print Preview
- Ensure readable when printed in grayscale

---

## 📸 **EXPORT OPTIONS**

### Export Chart as Image
1. Right-click chart
2. **Save as Picture**
3. Choose format (PNG for presentations, SVG for scalability)

### Export to PowerPoint
1. Copy chart (Ctrl+C)
2. Paste into PowerPoint
3. Choose "Keep Source Formatting"

---

## 🔗 **DATA CONNECTIONS**

### Link to External Data
For automatic updates:
1. **Data** → **Queries & Connections**
2. Set up automatic refresh
3. Charts update when data changes

---

## 📚 **RESOURCES**

- Excel Chart Types: https://support.microsoft.com/excel
- Color Palettes: https://coolors.co
- Chart Selection Guide: https://www.data-to-viz.com

---

**All data files ready in: `data_for_viz/` folder**
**Total data files: 13 CSV files**
**Ready for immediate use!**

---

🎨 **HAPPY VISUALIZING!** 🎨
