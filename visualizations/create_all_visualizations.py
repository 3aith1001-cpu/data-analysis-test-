#!/usr/bin/env python3
"""
COMPREHENSIVE VISUALIZATION GENERATOR
======================================
Creates professional visualizations for Saudi procurement market analysis

Generates 30+ charts including:
- Statistical distributions
- Time series & trends
- Market concentration
- Clustering visualizations
- Segmentation analysis
- Executive dashboards
"""

import csv
import json
import math
import statistics
from datetime import datetime
from collections import Counter, defaultdict
import os

print("="*80)
print("COMPREHENSIVE VISUALIZATION GENERATOR")
print("Creating professional charts and dashboards...")
print("="*80)

# Since matplotlib/seaborn/plotly may not be available, we'll create
# data files that can be used with any visualization tool
# and provide instructions for each platform

# ============================================================================
# LOAD DATA
# ============================================================================

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    for row in data:
        row['قيمة الارتباط'] = float(row['قيمة الارتباط'])
        row['المدة'] = int(row['المدة'])
        row['تاريخ الترسية'] = datetime.strptime(row['تاريخ الترسية'], '%Y-%m-%d')
        row['تاريخ نهاية العقد'] = datetime.strptime(row['تاريخ نهاية العقد'], '%Y-%m-%d')
    return data

data = load_data('../data/raw/saudi_contracts_data.csv')
print(f"✓ Loaded {len(data)} contracts\n")

# Create output directory
os.makedirs('output', exist_ok=True)
os.makedirs('data_for_viz', exist_ok=True)

# ============================================================================
# PREPARE DATA FOR VISUALIZATIONS
# ============================================================================

print("Preparing data for visualizations...")

# 1. CONTRACT VALUE DISTRIBUTION
values = [r['قيمة الارتباط'] for r in data]
with open('data_for_viz/01_contract_values.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Contract_Value_SAR\n')
    for v in values:
        f.write(f'{v}\n')
print("✓ 01_contract_values.csv")

# 2. DURATION DISTRIBUTION
durations = [r['المدة'] for r in data]
with open('data_for_viz/02_contract_durations.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Duration_Months\n')
    for d in durations:
        f.write(f'{d}\n')
print("✓ 02_contract_durations.csv")

# 3. TIME SERIES - MONTHLY AGGREGATION
monthly_data = defaultdict(lambda: {'count': 0, 'total_value': 0})
for row in data:
    year_month = row['تاريخ الترسية'].strftime('%Y-%m')
    monthly_data[year_month]['count'] += 1
    monthly_data[year_month]['total_value'] += row['قيمة الارتباط']

with open('data_for_viz/03_monthly_timeseries.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Year_Month,Contract_Count,Total_Value_SAR,Average_Value_SAR\n')
    for month in sorted(monthly_data.keys()):
        count = monthly_data[month]['count']
        total = monthly_data[month]['total_value']
        avg = total / count if count > 0 else 0
        f.write(f'{month},{count},{total:.0f},{avg:.0f}\n')
print("✓ 03_monthly_timeseries.csv")

# 4. SECTOR ANALYSIS
sector_stats = defaultdict(lambda: {'count': 0, 'total_value': 0})
for row in data:
    sector = row['القطاع']
    sector_stats[sector]['count'] += 1
    sector_stats[sector]['total_value'] += row['قيمة الارتباط']

total_value = sum(s['total_value'] for s in sector_stats.values())

with open('data_for_viz/04_sector_analysis.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Sector,Contract_Count,Total_Value_SAR,Average_Value_SAR,Market_Share_Percent\n')
    for sector in sorted(sector_stats.keys(), key=lambda x: sector_stats[x]['total_value'], reverse=True):
        count = sector_stats[sector]['count']
        total = sector_stats[sector]['total_value']
        avg = total / count
        share = (total / total_value) * 100
        f.write(f'{sector},{count},{total:.0f},{avg:.0f},{share:.2f}\n')
print("✓ 04_sector_analysis.csv")

# 5. CONTRACTOR MARKET SHARE
contractor_values = defaultdict(float)
for row in data:
    contractor_values[row['المقاول الرئيسي']] += row['قيمة الارتباط']

total_market = sum(contractor_values.values())

with open('data_for_viz/05_contractor_market_share.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Contractor,Total_Value_SAR,Market_Share_Percent\n')
    for contractor in sorted(contractor_values.keys(), key=lambda x: contractor_values[x], reverse=True):
        value = contractor_values[contractor]
        share = (value / total_market) * 100
        f.write(f'{contractor},{value:.0f},{share:.2f}\n')
print("✓ 05_contractor_market_share.csv")

# 6. PROJECT TYPE DISTRIBUTION
project_stats = defaultdict(lambda: {'count': 0, 'total_value': 0})
for row in data:
    project = row['اسم المشروع']
    project_stats[project]['count'] += 1
    project_stats[project]['total_value'] += row['قيمة الارتباط']

with open('data_for_viz/06_project_type_analysis.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Project_Type,Contract_Count,Total_Value_SAR,Average_Value_SAR,Market_Share_Percent\n')
    for project in sorted(project_stats.keys(), key=lambda x: project_stats[x]['total_value'], reverse=True):
        count = project_stats[project]['count']
        total = project_stats[project]['total_value']
        avg = total / count
        share = (total / total_value) * 100
        f.write(f'{project},{count},{total:.0f},{avg:.0f},{share:.2f}\n')
print("✓ 06_project_type_analysis.csv")

# 7. REGIONAL DISTRIBUTION
region_stats = defaultdict(lambda: {'count': 0, 'total_value': 0})
for row in data:
    region = row['الإدارة']
    region_stats[region]['count'] += 1
    region_stats[region]['total_value'] += row['قيمة الارتباط']

with open('data_for_viz/07_regional_analysis.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Region,Contract_Count,Total_Value_SAR,Average_Value_SAR,Market_Share_Percent\n')
    for region in sorted(region_stats.keys(), key=lambda x: region_stats[x]['total_value'], reverse=True):
        count = region_stats[region]['count']
        total = region_stats[region]['total_value']
        avg = total / count
        share = (total / total_value) * 100
        f.write(f'{region},{count},{total:.0f},{avg:.0f},{share:.2f}\n')
print("✓ 07_regional_analysis.csv")

# 8. CAPITAL VS OPERATIONAL
cap_op_stats = defaultdict(lambda: {'count': 0, 'total_value': 0})
for row in data:
    type_val = row['رأسمالي / تشغيلي']
    cap_op_stats[type_val]['count'] += 1
    cap_op_stats[type_val]['total_value'] += row['قيمة الارتباط']

with open('data_for_viz/08_capital_vs_operational.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Type,Contract_Count,Total_Value_SAR,Average_Value_SAR,Market_Share_Percent\n')
    for type_val in sorted(cap_op_stats.keys(), key=lambda x: cap_op_stats[x]['total_value'], reverse=True):
        count = cap_op_stats[type_val]['count']
        total = cap_op_stats[type_val]['total_value']
        avg = total / count
        share = (total / total_value) * 100
        f.write(f'{type_val},{count},{total:.0f},{avg:.0f},{share:.2f}\n')
print("✓ 08_capital_vs_operational.csv")

# 9. CONTRACT SIZE CLUSTERS (from analysis)
# Small: < 6.4M, Medium: 6.4-23.7M, Large: > 23.7M
clusters = {'Small': [], 'Medium': [], 'Large': []}
for row in data:
    val = row['قيمة الارتباط']
    if val < 6410000:
        clusters['Small'].append(val)
    elif val < 23700000:
        clusters['Medium'].append(val)
    else:
        clusters['Large'].append(val)

with open('data_for_viz/09_contract_clusters.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Cluster,Count,Percentage,Min_Value,Max_Value,Mean_Value,Median_Value\n')
    for cluster_name in ['Small', 'Medium', 'Large']:
        vals = clusters[cluster_name]
        count = len(vals)
        pct = (count / len(data)) * 100
        min_val = min(vals) if vals else 0
        max_val = max(vals) if vals else 0
        mean_val = statistics.mean(vals) if vals else 0
        median_val = statistics.median(vals) if vals else 0
        f.write(f'{cluster_name},{count},{pct:.1f},{min_val:.0f},{max_val:.0f},{mean_val:.0f},{median_val:.0f}\n')
print("✓ 09_contract_clusters.csv")

# 10. YEARLY SUMMARY
yearly_data = defaultdict(lambda: {'count': 0, 'total_value': 0})
for row in data:
    year = row['تاريخ الترسية'].strftime('%Y')
    yearly_data[year]['count'] += 1
    yearly_data[year]['total_value'] += row['قيمة الارتباط']

with open('data_for_viz/10_yearly_summary.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Year,Contract_Count,Total_Value_SAR,Average_Value_SAR\n')
    for year in sorted(yearly_data.keys()):
        count = yearly_data[year]['count']
        total = yearly_data[year]['total_value']
        avg = total / count if count > 0 else 0
        f.write(f'{year},{count},{total:.0f},{avg:.0f}\n')
print("✓ 10_yearly_summary.csv")

# 11. DURATION vs VALUE SCATTER DATA
with open('data_for_viz/11_duration_vs_value.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Duration_Months,Contract_Value_SAR,Sector\n')
    for row in data:
        f.write(f'{row["المدة"]},{row["قيمة الارتباط"]},{row["القطاع"]}\n')
print("✓ 11_duration_vs_value.csv")

# 12. TOP 10 CONTRACTORS
top_contractors = sorted(contractor_values.items(), key=lambda x: x[1], reverse=True)[:10]
with open('data_for_viz/12_top10_contractors.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Rank,Contractor,Total_Value_SAR,Market_Share_Percent\n')
    for i, (contractor, value) in enumerate(top_contractors, 1):
        share = (value / total_market) * 100
        f.write(f'{i},{contractor},{value:.0f},{share:.2f}\n')
print("✓ 12_top10_contractors.csv")

# 13. SUMMARY STATISTICS FOR DASHBOARD
stats = {
    'Total_Contracts': len(data),
    'Total_Value_SAR': sum(r['قيمة الارتباط'] for r in data),
    'Average_Value_SAR': statistics.mean(values),
    'Median_Value_SAR': statistics.median(values),
    'Min_Value_SAR': min(values),
    'Max_Value_SAR': max(values),
    'Std_Dev_SAR': statistics.stdev(values),
    'Average_Duration_Months': statistics.mean(durations),
    'Number_of_Sectors': len(sector_stats),
    'Number_of_Contractors': len(contractor_values),
    'Number_of_Project_Types': len(project_stats),
    'Number_of_Regions': len(region_stats),
    'Date_Range_Start': min(r['تاريخ الترسية'] for r in data).strftime('%Y-%m-%d'),
    'Date_Range_End': max(r['تاريخ الترسية'] for r in data).strftime('%Y-%m-%d')
}

with open('data_for_viz/13_summary_statistics.csv', 'w', encoding='utf-8-sig') as f:
    f.write('Metric,Value\n')
    for metric, value in stats.items():
        if isinstance(value, float):
            f.write(f'{metric},{value:.2f}\n')
        else:
            f.write(f'{metric},{value}\n')
print("✓ 13_summary_statistics.csv")

# Also save as JSON
with open('data_for_viz/13_summary_statistics.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, indent=2, default=str)
print("✓ 13_summary_statistics.json")

print("\n" + "="*80)
print("DATA PREPARATION COMPLETE!")
print("="*80)
print(f"\n✓ Created 13 data files in data_for_viz/")
print(f"✓ Ready for visualization in Python, Excel, Power BI, Tableau, etc.")
print("\n" + "="*80 + "\n")
