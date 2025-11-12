#!/usr/bin/env python3
"""
Validate if a dataset matches required Saudi procurement columns
Usage: python validate_dataset.py <csv_file>
"""
import pandas as pd
import sys

REQUIRED_COLUMNS = [
    'القطاع',
    'القسم',
    'الإدارة',
    'التنظيم الإداري',
    'اسم العقد',
    'المقاول الرئيسي',
    'اسم المشروع',
    'التصنيف الاقتصادي',
    'رأسمالي / تشغيلي',
    'التصنيف الصناعي',
    'قيمة الارتباط',
    'المدة',
    'تاريخ الترسية',
    'تاريخ نهاية العقد'
]

def validate_dataset(file_path):
    """Validate dataset against requirements"""
    print(f"\nValidating: {file_path}\n")
    print("="*70)

    try:
        df = pd.read_csv(file_path)

        print(f"✓ File loaded successfully")
        print(f"  Records: {len(df):,}")
        print(f"  Columns: {len(df.columns)}")
        print()

        # Check each required column
        matches = 0
        print("Column Match Analysis:")
        print("-"*70)

        for req_col in REQUIRED_COLUMNS:
            if req_col in df.columns:
                print(f"✓ {req_col}")
                matches += 1
            else:
                print(f"✗ {req_col} - MISSING")

        print("-"*70)
        print(f"\nMatch Score: {matches}/{len(REQUIRED_COLUMNS)} ({matches/len(REQUIRED_COLUMNS)*100:.1f}%)")

        if matches == len(REQUIRED_COLUMNS):
            print("\n🎉 PERFECT MATCH! This dataset has all required columns.")
        elif matches >= 10:
            print("\n⚠️  GOOD MATCH. Most columns present, minor mapping needed.")
        elif matches >= 5:
            print("\n⚠️  PARTIAL MATCH. Significant mapping required.")
        else:
            print("\n❌ POOR MATCH. This dataset has a different structure.")

        print("\nActual columns in dataset:")
        for col in df.columns:
            print(f"  - {col}")

        # Show sample data
        print("\nSample data (first 3 rows):")
        print(df.head(3).to_string())

        # Show data quality stats
        if matches == len(REQUIRED_COLUMNS):
            print("\n\nData Quality Analysis:")
            print("-"*70)
            print(f"Date range: {df['تاريخ الترسية'].min()} to {df['تاريخ الترسية'].max()}")

            if 'قيمة الارتباط' in df.columns:
                print(f"Contract values:")
                print(f"  Min: SAR {df['قيمة الارتباط'].min():,.0f}")
                print(f"  Max: SAR {df['قيمة الارتباط'].max():,.0f}")
                print(f"  Mean: SAR {df['قيمة الارتباط'].mean():,.0f}")
                print(f"  Median: SAR {df['قيمة الارتباط'].median():,.0f}")
                print(f"  Total: SAR {df['قيمة الارتباط'].sum():,.0f}")

            print(f"\nMissing values:")
            missing = df.isnull().sum()
            if missing.sum() == 0:
                print("  ✓ No missing values!")
            else:
                for col, count in missing[missing > 0].items():
                    print(f"  {col}: {count} ({count/len(df)*100:.1f}%)")

        print("\n" + "="*70)

    except Exception as e:
        print(f"✗ Error loading file: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_dataset.py <csv_file>")
        print("\nExample:")
        print("  python validate_dataset.py data/raw/saudi_contracts_data.csv")
        sys.exit(1)

    validate_dataset(sys.argv[1])
