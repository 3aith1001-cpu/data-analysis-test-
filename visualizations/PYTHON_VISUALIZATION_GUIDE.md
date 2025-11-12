# PYTHON VISUALIZATION GUIDE
## Creating Stunning Charts with Matplotlib, Seaborn & Plotly

---

## 🐍 **PYTHON VISUALIZATION LIBRARIES**

### **Matplotlib** - Foundation library
### **Seaborn** - Statistical visualizations
### **Plotly** - Interactive dashboards
### **Pandas** - Data manipulation + plotting

---

## 🚀 **SETUP**

### Install Libraries:
```bash
pip install matplotlib seaborn plotly pandas numpy
```

### Import in your script:
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
```

---

## 📊 **CHART 1: CONTRACT VALUE DISTRIBUTION (HISTOGRAM)**

### **Matplotlib Version:**
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data_for_viz/01_contract_values.csv')

# Create figure
plt.figure(figsize=(12, 6))
plt.hist(df['Contract_Value_SAR'] / 1_000_000, bins=50,
         edgecolor='black', color='steelblue', alpha=0.7)
plt.xlabel('Contract Value (Million SAR)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Contract Values', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('output/value_distribution.png', dpi=300, bbox_inches='tight')
plt.show()
```

### **Seaborn Version:**
```python
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='Contract_Value_SAR', bins=50, kde=True, color='steelblue')
plt.xlabel('Contract Value (SAR)', fontsize=12)
plt.title('Distribution of Contract Values (with KDE)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('output/value_distribution_seaborn.png', dpi=300)
plt.show()
```

### **Plotly Version (Interactive):**
```python
import plotly.express as px

fig = px.histogram(df, x='Contract_Value_SAR', nbins=50,
                   title='Distribution of Contract Values',
                   labels={'Contract_Value_SAR': 'Contract Value (SAR)'},
                   color_discrete_sequence=['steelblue'])
fig.update_layout(showlegend=False)
fig.write_html('output/value_distribution_interactive.html')
fig.show()
```

---

## 📊 **CHART 2: SECTOR MARKET SHARE (PIE CHART)**

### **Matplotlib:**
```python
# Load sector data
df_sector = pd.read_csv('data_for_viz/04_sector_analysis.csv')

plt.figure(figsize=(10, 8))
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F', '#BB8FCE']
explode = (0.05, 0, 0, 0, 0, 0, 0)  # Explode first slice

plt.pie(df_sector['Market_Share_Percent'],
        labels=df_sector['Sector'],
        autopct='%1.1f%%',
        colors=colors,
        explode=explode,
        startangle=90,
        shadow=True)
plt.title('Market Share by Sector', fontsize=14, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.savefig('output/sector_pie.png', dpi=300)
plt.show()
```

### **Plotly (Interactive Pie):**
```python
fig = px.pie(df_sector, values='Market_Share_Percent', names='Sector',
             title='Market Share by Sector',
             hole=0.3)  # Donut chart
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.write_html('output/sector_pie_interactive.html')
fig.show()
```

---

## 📊 **CHART 3: MONTHLY TIME SERIES (LINE CHART)**

### **Matplotlib (Dual Axis):**
```python
# Load time series data
df_ts = pd.read_csv('data_for_viz/03_monthly_timeseries.csv')

fig, ax1 = plt.subplots(figsize=(14, 6))

# Plot value on left axis
color = 'tab:blue'
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Total Value (Million SAR)', fontsize=12, color=color)
ax1.plot(df_ts.index, df_ts['Total_Value_SAR'] / 1_000_000,
         color=color, linewidth=2, marker='o', label='Total Value')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, alpha=0.3)

# Plot count on right axis
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Number of Contracts', fontsize=12, color=color)
ax2.plot(df_ts.index, df_ts['Contract_Count'],
         color=color, linewidth=2, marker='s', linestyle='--', label='Count')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Monthly Contract Activity Over Time', fontsize=14, fontweight='bold')
fig.tight_layout()
plt.savefig('output/monthly_timeseries.png', dpi=300)
plt.show()
```

### **Plotly (Interactive Multi-Line):**
```python
fig = go.Figure()

# Add value trace
fig.add_trace(go.Scatter(
    x=df_ts['Year_Month'],
    y=df_ts['Total_Value_SAR'] / 1_000_000,
    name='Total Value (M SAR)',
    mode='lines+markers',
    line=dict(color='blue', width=2)
))

# Add count trace (secondary y-axis)
fig.add_trace(go.Scatter(
    x=df_ts['Year_Month'],
    y=df_ts['Contract_Count'],
    name='Contract Count',
    mode='lines+markers',
    yaxis='y2',
    line=dict(color='red', width=2, dash='dash')
))

# Layout
fig.update_layout(
    title='Monthly Contract Activity',
    xaxis_title='Month',
    yaxis_title='Total Value (Million SAR)',
    yaxis2=dict(title='Contract Count', overlaying='y', side='right'),
    hovermode='x unified'
)

fig.write_html('output/monthly_timeseries_interactive.html')
fig.show()
```

---

## 📊 **CHART 4: TOP 10 CONTRACTORS (BAR CHART)**

### **Matplotlib (Horizontal Bars):**
```python
df_contractors = pd.read_csv('data_for_viz/12_top10_contractors.csv')

plt.figure(figsize=(12, 8))
plt.barh(df_contractors['Contractor'],
         df_contractors['Market_Share_Percent'],
         color='steelblue', edgecolor='black')
plt.xlabel('Market Share (%)', fontsize=12)
plt.ylabel('Contractor', fontsize=12)
plt.title('Top 10 Contractors by Market Share', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('output/top_contractors.png', dpi=300)
plt.show()
```

### **Seaborn (with gradient):**
```python
plt.figure(figsize=(12, 8))
sns.barplot(data=df_contractors, x='Market_Share_Percent', y='Contractor',
            palette='Blues_r', edgecolor='black')
plt.xlabel('Market Share (%)', fontsize=12)
plt.ylabel('Contractor', fontsize=12)
plt.title('Top 10 Contractors', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('output/top_contractors_seaborn.png', dpi=300)
plt.show()
```

---

## 📊 **CHART 5: SCATTER PLOT (DURATION VS VALUE)**

### **Matplotlib with Regression Line:**
```python
import numpy as np
from scipy import stats

df_scatter = pd.read_csv('data_for_viz/11_duration_vs_value.csv')

plt.figure(figsize=(12, 8))

# Scatter plot by sector (different colors)
sectors = df_scatter['Sector'].unique()
colors = plt.cm.Set3(np.linspace(0, 1, len(sectors)))

for sector, color in zip(sectors, colors):
    mask = df_scatter['Sector'] == sector
    plt.scatter(df_scatter[mask]['Duration_Months'],
                df_scatter[mask]['Contract_Value_SAR'] / 1_000_000,
                label=sector, alpha=0.6, s=50, color=color, edgecolor='black')

# Add regression line
slope, intercept, r_value, p_value, std_err = stats.linregress(
    df_scatter['Duration_Months'],
    df_scatter['Contract_Value_SAR'] / 1_000_000
)
line = slope * df_scatter['Duration_Months'] + intercept
plt.plot(df_scatter['Duration_Months'], line, 'r--', linewidth=2,
         label=f'Trend (R²={r_value**2:.3f})')

plt.xlabel('Duration (Months)', fontsize=12)
plt.ylabel('Contract Value (Million SAR)', fontsize=12)
plt.title('Contract Value vs Duration', fontsize=14, fontweight='bold')
plt.legend(loc='best', fontsize=9)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('output/scatter_duration_value.png', dpi=300)
plt.show()
```

### **Plotly (Interactive with Hover):**
```python
fig = px.scatter(df_scatter, x='Duration_Months', y='Contract_Value_SAR',
                 color='Sector',
                 size='Contract_Value_SAR',
                 hover_data=['Duration_Months', 'Contract_Value_SAR'],
                 title='Contract Value vs Duration (by Sector)',
                 labels={'Duration_Months': 'Duration (Months)',
                        'Contract_Value_SAR': 'Contract Value (SAR)'},
                 trendline='ols')  # Add trend line
fig.write_html('output/scatter_interactive.html')
fig.show()
```

---

## 📊 **CHART 6: HEATMAP (CORRELATION MATRIX)**

### **Seaborn Heatmap:**
```python
# Create correlation matrix from numerical columns
df_all = pd.read_csv('../data/raw/saudi_contracts_data.csv', encoding='utf-8-sig')

# Select numerical columns
numerical_cols = df_all.select_dtypes(include=[np.number]).columns
corr_matrix = df_all[numerical_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('output/correlation_heatmap.png', dpi=300)
plt.show()
```

---

## 📊 **CHART 7: BOX PLOT (VALUE DISTRIBUTION BY SECTOR)**

### **Seaborn Box Plot:**
```python
df_all = pd.read_csv('../data/raw/saudi_contracts_data.csv', encoding='utf-8-sig')

plt.figure(figsize=(12, 6))
sns.boxplot(data=df_all, x='القطاع', y='قيمة الارتباط', palette='Set2')
plt.xlabel('Sector', fontsize=12)
plt.ylabel('Contract Value (SAR)', fontsize=12)
plt.title('Contract Value Distribution by Sector', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('output/boxplot_by_sector.png', dpi=300)
plt.show()
```

---

## 📊 **CHART 8: VIOLIN PLOT (ADVANCED DISTRIBUTION)**

### **Seaborn Violin Plot:**
```python
plt.figure(figsize=(14, 6))
sns.violinplot(data=df_all, x='القطاع', y='قيمة الارتباط', palette='muted')
plt.xlabel('Sector', fontsize=12)
plt.ylabel('Contract Value (SAR)', fontsize=12)
plt.title('Contract Value Distribution (Violin Plot)', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('output/violin_plot.png', dpi=300)
plt.show()
```

---

## 📊 **CHART 9: TREEMAP (HIERARCHICAL)**

### **Plotly Treemap:**
```python
df_project = pd.read_csv('data_for_viz/06_project_type_analysis.csv')

fig = px.treemap(df_project, path=['Project_Type'], values='Total_Value_SAR',
                 title='Project Type Distribution (Treemap)',
                 color='Total_Value_SAR',
                 color_continuous_scale='Blues')
fig.write_html('output/treemap_interactive.html')
fig.show()
```

---

## 📊 **CHART 10: SUNBURST CHART (MULTI-LEVEL HIERARCHY)**

### **Plotly Sunburst:**
```python
# Create hierarchical data (Sector → Project Type → Value)
# This requires preprocessing to create proper hierarchy

fig = px.sunburst(df, path=['Sector', 'Project_Type'], values='Value',
                  title='Multi-Level Hierarchy',
                  color='Value',
                  color_continuous_scale='RdYlGn')
fig.write_html('output/sunburst_interactive.html')
fig.show()
```

---

## 🎨 **EXECUTIVE DASHBOARD (ALL IN ONE)**

### **Multi-Panel Dashboard:**
```python
import matplotlib.gridspec as gridspec

# Load all data
df_sector = pd.read_csv('data_for_viz/04_sector_analysis.csv')
df_ts = pd.read_csv('data_for_viz/03_monthly_timeseries.csv')
df_contractors = pd.read_csv('data_for_viz/12_top10_contractors.csv')
df_clusters = pd.read_csv('data_for_viz/09_contract_clusters.csv')

# Create figure with custom layout
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# Title
fig.suptitle('Saudi Procurement Market - Executive Dashboard',
             fontsize=18, fontweight='bold', y=0.98)

# 1. Sector Pie (top left)
ax1 = fig.add_subplot(gs[0, 0])
ax1.pie(df_sector['Market_Share_Percent'][:5], labels=df_sector['Sector'][:5],
        autopct='%1.1f%%', startangle=90)
ax1.set_title('Top 5 Sectors', fontweight='bold')

# 2. Monthly Trend (top right)
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(df_ts['Total_Value_SAR'] / 1_000_000, linewidth=2, color='blue')
ax2.set_title('Monthly Value Trend', fontweight='bold')
ax2.set_ylabel('Million SAR')
ax2.grid(alpha=0.3)

# 3. Clusters (middle left)
ax3 = fig.add_subplot(gs[1, 0])
colors_cluster = ['green', 'orange', 'red']
ax3.bar(df_clusters['Cluster'], df_clusters['Percentage'],
        color=colors_cluster, edgecolor='black')
ax3.set_title('Contract Size Distribution', fontweight='bold')
ax3.set_ylabel('Percentage (%)')

# 4. Top Contractors (middle-right, spanning 2 rows)
ax4 = fig.add_subplot(gs[1:, 1])
ax4.barh(df_contractors['Contractor'][:8],
         df_contractors['Market_Share_Percent'][:8],
         color='steelblue')
ax4.set_title('Top Contractors', fontweight='bold')
ax4.set_xlabel('Market Share (%)')
ax4.invert_yaxis()

# 5. KPIs (bottom left)
ax5 = fig.add_subplot(gs[2, 0])
ax5.axis('off')
kpi_text = """
Total Contracts: 500
Total Value: SAR 3.43B
Avg Value: SAR 6.85M
Growth (CAGR): 33.95%
"""
ax5.text(0.5, 0.5, kpi_text, ha='center', va='center', fontsize=12,
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

plt.savefig('output/executive_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

## 🎨 **STYLING & CUSTOMIZATION**

### **Custom Color Palette:**
```python
# Define custom colors
COLORS = {
    'primary': '#4472C4',
    'secondary': '#ED7D31',
    'success': '#70AD47',
    'danger': '#FF6B6B',
    'warning': '#FFC000',
    'info': '#5B9BD5'
}

# Use in plots
plt.bar(x, y, color=COLORS['primary'])
```

### **Style Sheets:**
```python
# Use built-in styles
plt.style.use('seaborn-v0_8-darkgrid')
# or
plt.style.use('ggplot')
# or
plt.style.use('fivethirtyeight')
```

### **Custom RC Parameters:**
```python
import matplotlib as mpl

mpl.rcParams['font.size'] = 11
mpl.rcParams['axes.labelsize'] = 12
mpl.rcParams['axes.titlesize'] = 14
mpl.rcParams['xtick.labelsize'] = 10
mpl.rcParams['ytick.labelsize'] = 10
mpl.rcParams['legend.fontsize'] = 10
mpl.rcParams['figure.titlesize'] = 16
```

---

## 📱 **PLOTLY DASHBOARD (FULLY INTERACTIVE)**

### **Dash App:**
```python
from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

# Load data
df_sector = pd.read_csv('data_for_viz/04_sector_analysis.csv')
df_ts = pd.read_csv('data_for_viz/03_monthly_timeseries.csv')

# Create figures
fig1 = px.pie(df_sector, values='Market_Share_Percent', names='Sector')
fig2 = px.line(df_ts, x='Year_Month', y='Total_Value_SAR')

# Layout
app.layout = html.Div([
    html.H1('Saudi Procurement Dashboard'),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2)
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

---

## 💾 **SAVING OPTIONS**

### **Save as PNG/JPG:**
```python
plt.savefig('output/chart.png', dpi=300, bbox_inches='tight')
plt.savefig('output/chart.jpg', dpi=300, quality=95)
```

### **Save as SVG (Vector):**
```python
plt.savefig('output/chart.svg', format='svg', bbox_inches='tight')
```

### **Save as PDF:**
```python
plt.savefig('output/chart.pdf', format='pdf', bbox_inches='tight')
```

### **Save Plotly as HTML:**
```python
fig.write_html('output/interactive_chart.html')
```

### **Save Multiple Plots as PDF:**
```python
from matplotlib.backends.backend_pdf import PdfPages

with PdfPages('output/all_charts.pdf') as pdf:
    # Create multiple figures
    fig1 = plt.figure()
    plt.plot([1, 2, 3])
    pdf.savefig(fig1)

    fig2 = plt.figure()
    plt.bar([1, 2, 3], [4, 5, 6])
    pdf.savefig(fig2)
```

---

## 🎯 **COMPLETE SCRIPT TEMPLATE**

```python
#!/usr/bin/env python3
"""
Complete visualization script for Saudi Procurement Data
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

def create_all_visualizations():
    """Generate all charts"""

    # 1. Value Distribution
    df_values = pd.read_csv('data_for_viz/01_contract_values.csv')
    plt.figure()
    plt.hist(df_values['Contract_Value_SAR'] / 1_000_000, bins=50)
    plt.title('Contract Value Distribution')
    plt.xlabel('Value (Million SAR)')
    plt.ylabel('Frequency')
    plt.savefig('output/01_distribution.png', dpi=300)
    plt.close()
    print("✓ 01_distribution.png")

    # 2. Sector Pie
    df_sector = pd.read_csv('data_for_viz/04_sector_analysis.csv')
    plt.figure()
    plt.pie(df_sector['Market_Share_Percent'], labels=df_sector['Sector'],
            autopct='%1.1f%%')
    plt.title('Market Share by Sector')
    plt.savefig('output/02_sector_pie.png', dpi=300)
    plt.close()
    print("✓ 02_sector_pie.png")

    # Add more charts...

    print("\n✓✓✓ All visualizations created! ✓✓✓")

if __name__ == '__main__':
    create_all_visualizations()
```

---

## 📚 **RESOURCES**

- Matplotlib Gallery: https://matplotlib.org/stable/gallery
- Seaborn Tutorial: https://seaborn.pydata.org/tutorial.html
- Plotly Documentation: https://plotly.com/python/
- Python Graph Gallery: https://www.python-graph-gallery.com

---

**All data files ready in: `data_for_viz/` folder**
**13 CSV files ready to visualize**
**Start coding your visualizations now!**

---

🐍 **PYTHON + DATA = BEAUTIFUL VISUALIZATIONS!** 🐍
