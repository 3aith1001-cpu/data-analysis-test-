# POWER BI VISUALIZATION GUIDE
## Creating Interactive Dashboards from Saudi Procurement Data

---

## 🚀 **QUICK START - 5 MINUTES TO DASHBOARD**

### Step 1: Launch Power BI Desktop
Download from: https://powerbi.microsoft.com/desktop

### Step 2: Import Data
1. **Get Data** → **Text/CSV**
2. Navigate to `data_for_viz/` folder
3. Select and load CSV files

### Step 3: Create Relationships (if using multiple tables)
1. Go to **Model** view
2. Drag to create relationships between tables

### Step 4: Build Visuals
1. Go to **Report** view
2. Drag fields to canvas
3. Choose visual types

---

## 📊 **30+ PROFESSIONAL VISUALS TO CREATE**

---

## 🎯 **DASHBOARD 1: EXECUTIVE OVERVIEW**

### **Page Layout:**
```
┌──────────────────────────────────────────────┐
│  KPI CARDS (4 across top)                    │
├───────────────┬──────────────┬───────────────┤
│ Sector Pie    │ Monthly Line │ Top Contractors│
├───────────────┴──────────────┴───────────────┤
│  Regional Map (Full width)                   │
└──────────────────────────────────────────────┘
```

### **Visual 1: KPI Cards** ⭐
**Data**: `13_summary_statistics.csv`

1. Add **Card** visual
2. Field: `Total_Contracts`
3. Format:
   - Data label: Large font (48pt)
   - Category label: "Total Contracts"
   - Background: Light blue
4. Repeat for:
   - Total Value (format as currency)
   - Average Value
   - Date Range

---

### **Visual 2: Sector Market Share (Donut Chart)** ⭐
**Data**: `04_sector_analysis.csv`

1. Add **Donut Chart**
2. **Legend**: `Sector`
3. **Values**: `Market_Share_Percent`
4. Format:
   - Detail labels: Show percentage
   - Legend position: Right
   - Colors: Apply custom theme
5. Title: "Market Share by Sector"

**DAX Measure** (optional):
```DAX
Market Share % =
DIVIDE(
    SUM('Sector'[Total_Value_SAR]),
    CALCULATE(SUM('Sector'[Total_Value_SAR]), ALL('Sector'))
) * 100
```

---

### **Visual 3: Monthly Trend (Line + Column Chart)** ⭐
**Data**: `03_monthly_timeseries.csv`

1. Add **Line and Clustered Column Chart**
2. **Axis**: `Year_Month`
3. **Column values**: `Total_Value_SAR`
4. **Line values**: `Contract_Count`
5. Format:
   - Use secondary axis for count
   - Add data labels
   - Smooth lines
   - Add forecast (3 months)
6. Title: "Contract Activity Over Time"

**Advanced**: Add trend line
- Analytics pane → **Trend line** → Linear

---

### **Visual 4: Top 10 Contractors (Bar Chart)** ⭐
**Data**: `12_top10_contractors.csv`

1. Add **Clustered Bar Chart**
2. **Axis**: `Contractor`
3. **Values**: `Market_Share_Percent`
4. Format:
   - Sort descending
   - Data labels: Show values
   - Conditional formatting by value
5. Title: "Top 10 Contractors"

**Conditional Formatting**:
- Rules → If value > 15%, color dark blue
- If value 10-15%, color medium blue
- If value < 10%, color light blue

---

### **Visual 5: Regional Distribution (Filled Map)** ⭐
**Data**: `07_regional_analysis.csv`

1. Add **Map** visual
2. **Location**: `Region`
3. **Size**: `Total_Value_SAR`
4. **Color saturation**: `Market_Share_Percent`
5. Format:
   - Style: Dark
   - Zoom: Auto
   - Add data labels
6. Title: "Geographic Distribution"

**Note**: For Saudi Arabia, use coordinates if map doesn't recognize Arabic names:
- Add latitude/longitude columns
- Use **Filled Map** instead

---

## 📊 **DASHBOARD 2: TIME SERIES ANALYSIS**

### **Visual 6: Yearly Growth Waterfall Chart** ⭐
**Data**: `10_yearly_summary.csv`

1. Add **Waterfall Chart**
2. **Category**: `Year`
3. **Y-axis**: `Total_Value_SAR`
4. Shows year-over-year growth
5. Title: "Annual Value Growth"

---

### **Visual 7: Monthly Decomposition (Area Chart)**
**Data**: `03_monthly_timeseries.csv`

1. Add **Area Chart**
2. **Axis**: `Year_Month`
3. **Values**: `Total_Value_SAR`
4. Format:
   - Fill: Gradient
   - Transparency: 30%
   - Add moving average (MA-3)
5. Title: "Monthly Value Trend"

---

### **Visual 8: Seasonal Pattern (Line Chart)**
**Create calculated column first:**
```DAX
Month = FORMAT('Monthly'[Year_Month], "MMM")
```

1. Add **Line Chart**
2. **Axis**: `Month`
3. **Values**: `Average_Value_SAR` by month
4. Shows seasonal patterns
5. Add average line

---

## 📊 **DASHBOARD 3: MARKET STRUCTURE**

### **Visual 9: Contract Size Distribution (Column Chart)** ⭐
**Data**: `09_contract_clusters.csv`

1. Add **Clustered Column Chart**
2. **Axis**: `Cluster`
3. **Values**: `Percentage`
4. Format:
   - Colors: Green (Small), Orange (Medium), Red (Large)
   - Data labels on bars
5. Title: "Contract Size Distribution"

---

### **Visual 10: HHI Market Concentration (Gauge)**
**Create measure:**
```DAX
HHI =
SUMX(
    VALUES('Contractor'[Contractor]),
    POWER(
        DIVIDE(
            CALCULATE(SUM('Contracts'[Value])),
            CALCULATE(SUM('Contracts'[Value]), ALL('Contractor'))
        ) * 100,
        2
    )
)
```

1. Add **Gauge** visual
2. **Value**: `HHI`
3. **Target**: 1500 (competitive threshold)
4. **Maximum**: 2500
5. Color coding:
   - < 1500: Green (Competitive)
   - 1500-2500: Yellow (Moderate)
   - > 2500: Red (Concentrated)

---

### **Visual 11: Market Share Treemap** ⭐
**Data**: `05_contractor_market_share.csv`

1. Add **Treemap**
2. **Group**: `Contractor`
3. **Values**: `Total_Value_SAR`
4. Format:
   - Show data labels
   - Adjust size based on value
5. Title: "Contractor Market Share (Treemap)"

---

## 📊 **DASHBOARD 4: COMPARATIVE ANALYSIS**

### **Visual 12: Sector vs Region Matrix (Heat Map)** ⭐

**Create matrix:**
1. Add **Matrix** visual
2. **Rows**: `Sector`
3. **Columns**: `Region`
4. **Values**: `SUM(Value)`
5. Format:
   - Background color: Conditional formatting
   - Gradient: Light to dark blue
   - Show totals

---

### **Visual 13: Scatter Plot - Duration vs Value** ⭐
**Data**: `11_duration_vs_value.csv`

1. Add **Scatter Chart**
2. **X-axis**: `Duration_Months`
3. **Y-axis**: `Contract_Value_SAR`
4. **Legend**: `Sector` (shows as different colors)
5. **Size**: Constant or by count
6. Add:
   - Trend line
   - Median lines
   - Quadrant markers

**Advanced**: Add play axis for year-by-year animation

---

### **Visual 14: Capital vs Operational Comparison**
**Data**: `08_capital_vs_operational.csv`

1. Add **Stacked Bar Chart**
2. **Axis**: `Type`
3. **Values**: `Total_Value_SAR`
4. Format with contrasting colors
5. Add data labels

---

## 🎨 **ADVANCED FEATURES**

### **1. Drill-Through Pages**

Create detail page:
1. New page: "Contract Details"
2. Add drill-through filter
3. Add detailed visuals
4. Users can right-click and drill through

### **2. Bookmarks for Navigation**

1. Create multiple views
2. **View** → **Bookmarks**
3. Save different states
4. Add buttons for navigation

### **3. Tooltips (Custom)**

1. Create tooltip page
2. Set page type to "Tooltip"
3. Add relevant visuals
4. Enable in main visual properties

### **4. Slicers for Filtering** ⭐

Add slicers for:
- **Year** (dropdown or slider)
- **Sector** (list with search)
- **Region** (tiles)
- **Contract Size** (range slider)

Format slicers:
- Responsive layout
- Visual hierarchy
- Clear "Clear All" button

---

## 📊 **DAX MEASURES TO CREATE**

### Essential Calculations:

**1. Total Contracts**
```DAX
Total Contracts = COUNTROWS('Contracts')
```

**2. Average Value**
```DAX
Average Value = AVERAGE('Contracts'[Value])
```

**3. YoY Growth**
```DAX
YoY Growth % =
VAR CurrentYear = SUM('Contracts'[Value])
VAR PreviousYear =
    CALCULATE(
        SUM('Contracts'[Value]),
        DATEADD('Date'[Date], -1, YEAR)
    )
RETURN
DIVIDE(CurrentYear - PreviousYear, PreviousYear) * 100
```

**4. Running Total**
```DAX
Running Total =
CALCULATE(
    SUM('Contracts'[Value]),
    FILTER(
        ALL('Date'),
        'Date'[Date] <= MAX('Date'[Date])
    )
)
```

**5. Market Share**
```DAX
Market Share % =
DIVIDE(
    SUM('Contracts'[Value]),
    CALCULATE(SUM('Contracts'[Value]), ALL('Contractor'))
) * 100
```

**6. Top N Filter**
```DAX
Top 10 Contractors =
IF(
    RANKX(
        ALL('Contractor'[Name]),
        SUM('Contracts'[Value]),
        ,
        DESC,
        DENSE
    ) <= 10,
    1,
    0
)
```

---

## 🎨 **THEME & STYLING**

### Custom Theme JSON:

```json
{
  "name": "Saudi Procurement Theme",
  "dataColors": [
    "#4472C4", "#ED7D31", "#70AD47", "#FFC000",
    "#5B9BD5", "#C5E0B4", "#255E91", "#9E480E"
  ],
  "background": "#FFFFFF",
  "foreground": "#252423",
  "tableAccent": "#4472C4"
}
```

Save as `theme.json` and import:
**View** → **Themes** → **Browse for themes**

---

## 📱 **MOBILE LAYOUT**

1. **View** → **Mobile Layout**
2. Drag visuals to mobile canvas
3. Prioritize:
   - KPI cards at top
   - Most important chart
   - Filters
4. Test on phone

---

## 🔄 **REFRESH & PUBLISH**

### Schedule Refresh:
1. Publish to Power BI Service
2. **Settings** → **Scheduled refresh**
3. Connect to data source
4. Set frequency (daily/weekly)

### Share Dashboard:
1. **File** → **Publish to Power BI**
2. Choose workspace
3. Share link with stakeholders
4. Set permissions

---

## 📊 **INTERACTIVE FEATURES**

### **Cross-Filtering**
- Click any visual to filter others
- Ctrl+Click for multi-select
- Configure interactions

### **Drill-Down**
Create hierarchy:
```
Year → Quarter → Month → Week
Sector → Department → Project
```

### **Q&A Feature**
1. Add **Q&A** visual
2. Users can ask:
   - "What is total value by sector?"
   - "Show top contractors"
   - "Compare 2023 to 2024"

---

## 🎯 **RECOMMENDED DASHBOARDS**

### Dashboard 1: Executive Overview
- KPIs
- Sector breakdown
- Monthly trend
- Top contractors

### Dashboard 2: Deep Dive Analysis
- Detailed time series
- Regional analysis
- Project type breakdown
- Scatter plots

### Dashboard 3: Contractor Analysis
- Market share treemap
- Performance metrics
- Growth trends
- Competitive landscape

### Dashboard 4: Predictive Analytics
- Forecasts
- Trend lines
- Anomaly detection
- What-if parameters

---

## 💡 **BEST PRACTICES**

1. **Keep it Simple**: 5-7 visuals per page maximum
2. **Consistent Colors**: Use theme throughout
3. **Clear Titles**: Every visual needs descriptive title
4. **Add Context**: Use text boxes for insights
5. **Test Performance**: Optimize DAX queries
6. **Mobile First**: Design for mobile viewing
7. **Tell a Story**: Logical flow between pages
8. **Add Filters**: Easy data exploration
9. **Update Regularly**: Schedule automatic refresh
10. **Get Feedback**: Iterate based on user input

---

## 📚 **POWER BI RESOURCES**

- Official Docs: https://docs.microsoft.com/power-bi
- DAX Guide: https://dax.guide
- Community: https://community.powerbi.com
- Templates: https://app.powerbi.com/templates
- Training: https://docs.microsoft.com/learn/power-bi

---

## 🎬 **VIDEO TUTORIALS**

Search YouTube for:
- "Power BI Dashboard Tutorial"
- "Power BI DAX Basics"
- "Power BI Best Practices"
- "Power BI Mobile Reports"

---

**All data files ready in: `data_for_viz/` folder**
**13 CSV files ready to import**
**Start building your interactive dashboard now!**

---

🚀 **POWER BI = POWER TO INSIGHTS!** 🚀
