#!/usr/bin/env python3
"""
Python Chart Generator using ASCII/Text-based charts
Since matplotlib may not be available, we create text-based visualizations
and detailed instructions for creating charts
"""

import csv
import statistics
from collections import defaultdict

print("="*80)
print("PYTHON VISUALIZATION GENERATOR")
print("="*80)

# Try to import plotting libraries
try:
    import matplotlib
    matplotlib.use('Agg')  # Use non-interactive backend
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    HAS_MATPLOTLIB = True
    print("✓ matplotlib available - will generate PNG charts")
except ImportError:
    HAS_MATPLOTLIB = False
    print("⚠ matplotlib not available - will generate text-based charts and instructions")

print("="*80 + "\n")

# Load summary statistics
stats = {}
with open('data_for_viz/13_summary_statistics.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        stats[row['Metric']] = row['Value']

if HAS_MATPLOTLIB:
    # Create charts with matplotlib
    print("Creating matplotlib charts...")

    # Load data
    import pandas as pd

    # 1. Contract Value Distribution - Histogram
    values_df = pd.read_csv('data_for_viz/01_contract_values.csv')

    plt.figure(figsize=(12, 6))
    plt.hist(values_df['Contract_Value_SAR'] / 1000000, bins=50, edgecolor='black', alpha=0.7)
    plt.xlabel('Contract Value (Million SAR)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title('Distribution of Contract Values', fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('output/01_value_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 01_value_distribution.png")

    # 2. Sector Market Share - Pie Chart
    sector_df = pd.read_csv('data_for_viz/04_sector_analysis.csv')

    plt.figure(figsize=(10, 8))
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F', '#BB8FCE']
    plt.pie(sector_df['Market_Share_Percent'], labels=sector_df['Sector'], autopct='%1.1f%%',
            colors=colors, startangle=90)
    plt.title('Market Share by Sector', fontsize=14, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('output/02_sector_pie.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 02_sector_pie.png")

    # 3. Monthly Time Series
    monthly_df = pd.read_csv('data_for_viz/03_monthly_timeseries.csv')

    fig, ax1 = plt.subplots(figsize=(14, 6))

    ax1.plot(range(len(monthly_df)), monthly_df['Total_Value_SAR'] / 1000000,
             'b-', linewidth=2, label='Total Value')
    ax1.set_xlabel('Month', fontsize=12)
    ax1.set_ylabel('Total Value (Million SAR)', fontsize=12, color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.grid(alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(range(len(monthly_df)), monthly_df['Contract_Count'],
             'r--', linewidth=2, label='Count')
    ax2.set_ylabel('Number of Contracts', fontsize=12, color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    plt.title('Monthly Contract Activity Over Time', fontsize=14, fontweight='bold')
    fig.tight_layout()
    plt.savefig('output/03_monthly_timeseries.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 03_monthly_timeseries.png")

    # 4. Top 10 Contractors - Bar Chart
    contractors_df = pd.read_csv('data_for_viz/12_top10_contractors.csv')

    plt.figure(figsize=(12, 8))
    plt.barh(contractors_df['Contractor'], contractors_df['Market_Share_Percent'],
             color='steelblue', edgecolor='black')
    plt.xlabel('Market Share (%)', fontsize=12)
    plt.ylabel('Contractor', fontsize=12)
    plt.title('Top 10 Contractors by Market Share', fontsize=14, fontweight='bold')
    plt.grid(axis='x', alpha=0.3)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('output/04_top_contractors.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 04_top_contractors.png")

    # 5. Contract Clusters - Stacked Bar
    clusters_df = pd.read_csv('data_for_viz/09_contract_clusters.csv')

    plt.figure(figsize=(10, 6))
    colors_cluster = ['#95E1D3', '#F38181', '#AA96DA']
    plt.bar(clusters_df['Cluster'], clusters_df['Percentage'],
            color=colors_cluster, edgecolor='black', linewidth=2)
    plt.ylabel('Percentage of Contracts (%)', fontsize=12)
    plt.title('Contract Size Distribution', fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for i, (cluster, pct) in enumerate(zip(clusters_df['Cluster'], clusters_df['Percentage'])):
        plt.text(i, pct + 1, f'{pct:.1f}%', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.savefig('output/05_contract_clusters.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 05_contract_clusters.png")

    # 6. Regional Distribution
    regional_df = pd.read_csv('data_for_viz/07_regional_analysis.csv')

    plt.figure(figsize=(12, 6))
    x_pos = range(len(regional_df))
    plt.bar(x_pos, regional_df['Total_Value_SAR'] / 1000000,
            color='coral', edgecolor='black', alpha=0.8)
    plt.xlabel('Region', fontsize=12)
    plt.ylabel('Total Value (Million SAR)', fontsize=12)
    plt.title('Contract Value by Region', fontsize=14, fontweight='bold')
    plt.xticks(x_pos, regional_df['Region'], rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('output/06_regional_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 06_regional_distribution.png")

    # 7. Yearly Trend
    yearly_df = pd.read_csv('data_for_viz/10_yearly_summary.csv')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Value trend
    ax1.plot(yearly_df['Year'], yearly_df['Total_Value_SAR'] / 1000000,
             'o-', linewidth=3, markersize=10, color='green')
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Total Value (Million SAR)', fontsize=12)
    ax1.set_title('Annual Contract Value Trend', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # Count trend
    ax2.plot(yearly_df['Year'], yearly_df['Contract_Count'],
             's-', linewidth=3, markersize=10, color='purple')
    ax2.set_xlabel('Year', fontsize=12)
    ax2.set_ylabel('Number of Contracts', fontsize=12)
    ax2.set_title('Annual Contract Count Trend', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('output/07_yearly_trends.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 07_yearly_trends.png")

    # 8. Executive Dashboard
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

    # Title
    fig.suptitle('Saudi Procurement Market - Executive Dashboard',
                 fontsize=18, fontweight='bold', y=0.98)

    # KPIs
    ax_kpi = fig.add_subplot(gs[0, :])
    ax_kpi.axis('off')

    kpi_text = f"""
    Total Contracts: {stats['Total_Contracts']}  |  Total Value: SAR {float(stats['Total_Value_SAR'])/1e9:.2f}B  |  Avg Value: SAR {float(stats['Average_Value_SAR'])/1e6:.1f}M  |  Period: {stats['Date_Range_Start']} to {stats['Date_Range_End']}
    """
    ax_kpi.text(0.5, 0.5, kpi_text, ha='center', va='center',
                fontsize=14, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

    # Chart 1: Sector pie
    ax1 = fig.add_subplot(gs[1, 0])
    ax1.pie(sector_df['Market_Share_Percent'][:5], labels=sector_df['Sector'][:5],
            autopct='%1.1f%%', startangle=90)
    ax1.set_title('Top 5 Sectors', fontweight='bold')

    # Chart 2: Monthly trend
    ax2 = fig.add_subplot(gs[1, 1:])
    ax2.plot(monthly_df['Total_Value_SAR'] / 1000000, linewidth=2)
    ax2.set_title('Monthly Contract Value Trend', fontweight='bold')
    ax2.set_ylabel('Million SAR')
    ax2.grid(alpha=0.3)

    # Chart 3: Clusters
    ax3 = fig.add_subplot(gs[2, 0])
    ax3.bar(clusters_df['Cluster'], clusters_df['Percentage'],
            color=['green', 'orange', 'red'], edgecolor='black')
    ax3.set_title('Contract Size Distribution', fontweight='bold')
    ax3.set_ylabel('Percentage (%)')

    # Chart 4: Top contractors
    ax4 = fig.add_subplot(gs[2, 1:])
    ax4.barh(contractors_df['Contractor'][:5], contractors_df['Market_Share_Percent'][:5],
             color='steelblue')
    ax4.set_title('Top 5 Contractors', fontweight='bold')
    ax4.set_xlabel('Market Share (%)')
    ax4.invert_yaxis()

    plt.savefig('output/08_executive_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ 08_executive_dashboard.png")

    print("\n✓✓✓ All matplotlib charts created successfully! ✓✓✓\n")

else:
    # Create text-based visualizations
    print("Creating text-based visualizations...\n")

    # ASCII Bar Chart for Top Contractors
    with open('output/text_visualizations.txt', 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("SAUDI PROCUREMENT MARKET - TEXT VISUALIZATIONS\n")
        f.write("="*80 + "\n\n")

        f.write("TOP 10 CONTRACTORS BY MARKET SHARE\n")
        f.write("-" * 80 + "\n")

        with open('data_for_viz/12_top10_contractors.csv', 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contractor = row['Contractor'][:30]  # Truncate long names
                share = float(row['Market_Share_Percent'])
                bar_length = int(share * 3)  # Scale for display
                bar = '█' * bar_length
                f.write(f"{contractor:30} {bar} {share:.2f}%\n")

        f.write("\n" + "="*80 + "\n\n")

        f.write("SECTOR DISTRIBUTION\n")
        f.write("-" * 80 + "\n")

        with open('data_for_viz/04_sector_analysis.csv', 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sector = row['Sector']
                share = float(row['Market_Share_Percent'])
                bar_length = int(share * 3)
                bar = '█' * bar_length
                f.write(f"{sector:20} {bar} {share:.2f}%\n")

        f.write("\n" + "="*80 + "\n")

    print("✓ text_visualizations.txt created\n")

print("="*80)
print("PYTHON VISUALIZATION COMPLETE!")
print("="*80)
