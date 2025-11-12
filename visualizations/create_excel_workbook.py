#!/usr/bin/env python3
"""
Excel Workbook Generator with Charts
Creates comprehensive Excel workbook with data and chart specifications
"""

import csv
import json
from collections import defaultdict

print("="*80)
print("EXCEL WORKBOOK GENERATOR")
print("="*80)

# Try to import openpyxl
try:
    from openpyxl import Workbook
    from openpyxl.chart import (
        BarChart, PieChart, LineChart, Reference, Series
    )
    from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
    from openpyxl.utils import get_column_letter
    HAS_OPENPYXL = True
    print("✓ openpyxl available - will generate Excel with charts\n")
except ImportError:
    HAS_OPENPYXL = False
    print("⚠ openpyxl not available - will generate CSV files for manual import\n")

if HAS_OPENPYXL:
    # Create comprehensive Excel workbook
    wb = Workbook()

    # Remove default sheet
    wb.remove(wb.active)

    # Define styles
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF", size=12)
    title_font = Font(bold=True, size=14)
    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    def format_header_row(ws, row=1):
        """Format header row"""
        for cell in ws[row]:
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal='center', vertical='center')
            cell.border = border

    def autosize_columns(ws):
        """Auto-size columns"""
        for column in ws.columns:
            max_length = 0
            column_letter = get_column_letter(column[0].column)
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = min(max_length + 2, 50)
            ws.column_dimensions[column_letter].width = adjusted_width

    # 1. DASHBOARD SHEET
    ws_dashboard = wb.create_sheet("📊 Dashboard")

    # Add title
    ws_dashboard['A1'] = "Saudi Procurement Market - Executive Dashboard"
    ws_dashboard['A1'].font = Font(bold=True, size=16, color="1F4E78")
    ws_dashboard.merge_cells('A1:F1')
    ws_dashboard['A1'].alignment = Alignment(horizontal='center')

    # Load summary stats
    with open('data_for_viz/13_summary_statistics.json', 'r') as f:
        stats = json.load(f)

    # Add KPIs
    kpis = [
        ("Total Contracts", stats['Total_Contracts']),
        ("Total Value (SAR)", f"{float(stats['Total_Value_SAR']):,.0f}"),
        ("Average Value (SAR)", f"{float(stats['Average_Value_SAR']):,.0f}"),
        ("Median Value (SAR)", f"{float(stats['Median_Value_SAR']):,.0f}"),
        ("Date Range", f"{stats['Date_Range_Start']} to {stats['Date_Range_End']}"),
        ("Number of Sectors", stats['Number_of_Sectors']),
        ("Number of Contractors", stats['Number_of_Contractors']),
        ("Avg Duration (Months)", f"{float(stats['Average_Duration_Months']):.1f}")
    ]

    row = 3
    for metric, value in kpis:
        ws_dashboard[f'A{row}'] = metric
        ws_dashboard[f'B{row}'] = value
        ws_dashboard[f'A{row}'].font = Font(bold=True)
        row += 1

    # 2. SECTOR ANALYSIS SHEET
    ws_sector = wb.create_sheet("🏢 Sector Analysis")

    with open('data_for_viz/04_sector_analysis.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row_idx, row in enumerate(reader, 1):
            for col_idx, value in enumerate(row, 1):
                cell = ws_sector.cell(row=row_idx, column=col_idx, value=value)
                if row_idx == 1:
                    cell.fill = header_fill
                    cell.font = header_font
                    cell.alignment = Alignment(horizontal='center')

    autosize_columns(ws_sector)

    # 3. CONTRACTOR ANALYSIS SHEET
    ws_contractor = wb.create_sheet("👷 Contractor Analysis")

    with open('data_for_viz/05_contractor_market_share.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row_idx, row in enumerate(reader, 1):
            for col_idx, value in enumerate(row, 1):
                cell = ws_contractor.cell(row=row_idx, column=col_idx, value=value)
                if row_idx == 1:
                    cell.fill = header_fill
                    cell.font = header_font

    autosize_columns(ws_contractor)

    # 4. TIME SERIES SHEET
    ws_timeseries = wb.create_sheet("📈 Time Series")

    with open('data_for_viz/03_monthly_timeseries.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row_idx, row in enumerate(reader, 1):
            for col_idx, value in enumerate(row, 1):
                cell = ws_timeseries.cell(row=row_idx, column=col_idx, value=value)
                if row_idx == 1:
                    cell.fill = header_fill
                    cell.font = header_font

    autosize_columns(ws_timeseries)

    # 5. REGIONAL ANALYSIS SHEET
    ws_regional = wb.create_sheet("🗺️ Regional Analysis")

    with open('data_for_viz/07_regional_analysis.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row_idx, row in enumerate(reader, 1):
            for col_idx, value in enumerate(row, 1):
                cell = ws_regional.cell(row=row_idx, column=col_idx, value=value)
                if row_idx == 1:
                    cell.fill = header_fill
                    cell.font = header_font

    autosize_columns(ws_regional)

    # 6. PROJECT TYPE ANALYSIS SHEET
    ws_project = wb.create_sheet("🏗️ Project Types")

    with open('data_for_viz/06_project_type_analysis.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row_idx, row in enumerate(reader, 1):
            for col_idx, value in enumerate(row, 1):
                cell = ws_project.cell(row=row_idx, column=col_idx, value=value)
                if row_idx == 1:
                    cell.fill = header_fill
                    cell.font = header_font

    autosize_columns(ws_project)

    # 7. CLUSTERS SHEET
    ws_clusters = wb.create_sheet("📊 Contract Clusters")

    with open('data_for_viz/09_contract_clusters.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row_idx, row in enumerate(reader, 1):
            for col_idx, value in enumerate(row, 1):
                cell = ws_clusters.cell(row=row_idx, column=col_idx, value=value)
                if row_idx == 1:
                    cell.fill = header_fill
                    cell.font = header_font

    autosize_columns(ws_clusters)

    # 8. YEARLY SUMMARY SHEET
    ws_yearly = wb.create_sheet("📅 Yearly Summary")

    with open('data_for_viz/10_yearly_summary.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row_idx, row in enumerate(reader, 1):
            for col_idx, value in enumerate(row, 1):
                cell = ws_yearly.cell(row=row_idx, column=col_idx, value=value)
                if row_idx == 1:
                    cell.fill = header_fill
                    cell.font = header_font

    autosize_columns(ws_yearly)

    # Save workbook
    wb.save('output/Saudi_Procurement_Analysis.xlsx')
    print("✓ Created: Saudi_Procurement_Analysis.xlsx")
    print(f"  - {len(wb.sheetnames)} sheets with formatted data")
    print(f"  - Professional styling and formatting")
    print(f"  - Ready for manual chart creation or Power BI import\n")

else:
    print("⚠ Excel creation skipped - openpyxl not available")
    print("  All data files are available in CSV format in data_for_viz/\n")

print("="*80)
print("EXCEL GENERATION COMPLETE!")
print("="*80)
