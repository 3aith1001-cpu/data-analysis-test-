#!/usr/bin/env python3
"""
Main Data Collection Orchestrator
Attempts to collect Saudi Arabia construction/procurement data from multiple sources
"""

import os
import sys
import subprocess
import pandas as pd
from datetime import datetime

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*70)
    print(text.center(70))
    print("="*70 + "\n")

def install_requirements():
    """Install required packages"""
    print_header("INSTALLING REQUIREMENTS")

    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install",
            "-r", "requirements.txt", "-q"
        ])
        print("✓ All requirements installed successfully\n")
        return True
    except Exception as e:
        print(f"⚠️  Error installing requirements: {e}")
        print("   Continuing anyway...\n")
        return False

def try_kaggle_download():
    """Attempt to download data from Kaggle"""
    print_header("METHOD 1: KAGGLE DATASETS")

    try:
        print("Attempting Kaggle download...")
        result = subprocess.run(
            [sys.executable, "kaggle_downloader.py"],
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode == 0:
            print("✓ Kaggle download completed")
            return True
        else:
            print("⚠️  Kaggle download failed or incomplete")
            print("   (This is normal if you haven't set up Kaggle API credentials)")
            return False

    except Exception as e:
        print(f"⚠️  Kaggle method not available: {e}")
        return False

def try_saudi_open_data():
    """Attempt to scrape Saudi Open Data Portal"""
    print_header("METHOD 2: SAUDI OPEN DATA PORTAL")

    try:
        print("Attempting Saudi Open Data Portal scraping...")
        result = subprocess.run(
            [sys.executable, "saudi_open_data_scraper.py"],
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode == 0:
            print("✓ Saudi Open Data scraping completed")
            return True
        else:
            print("⚠️  Saudi Open Data scraping failed or incomplete")
            return False

    except Exception as e:
        print(f"⚠️  Saudi Open Data method not available: {e}")
        return False

def create_sample_realistic_data():
    """
    Create sample realistic data based on typical Saudi procurement contracts
    This is a fallback when real data sources are not accessible
    """
    print_header("METHOD 3: CREATING REALISTIC SAMPLE DATA")

    print("📝 Creating realistic sample dataset based on typical Saudi procurement patterns...")
    print("   (This will be replaced with real data once sources are accessible)\n")

    import numpy as np
    from datetime import timedelta

    # Set random seed for reproducibility
    np.random.seed(42)

    # Number of sample records
    n_records = 500

    # Define realistic Saudi sectors and departments
    sectors = ['الصحة', 'التعليم', 'الدفاع', 'الداخلية', 'النقل', 'الإسكان', 'البلدية']
    departments = ['الصيانة', 'المشاريع', 'العمليات', 'التطوير', 'الخدمات']
    administrations = ['الرياض', 'جدة', 'الدمام', 'مكة', 'المدينة', 'الطائف', 'تبوك']

    # Contractors (mix of real and fictional Saudi companies)
    contractors = [
        'شركة بن لادن السعودية',
        'مجموعة السعودي الفرنسي',
        'شركة الراجحي للمقاولات',
        'مجموعة العليان',
        'شركة عبدالله عبدالمحسن الخضري',
        'شركة أرامكو للخدمات',
        'مجموعة صافولا',
        'شركة الفطيم للمقاولات',
        'مجموعة الزامل',
        'شركة النهدي للتطوير'
    ]

    # Project types
    project_types = [
        'صيانة المباني',
        'تطوير البنية التحتية',
        'إنشاءات جديدة',
        'صيانة الطرق',
        'أنظمة التكييف',
        'الخدمات الكهربائية',
        'أعمال السباكة',
        'تطوير المرافق',
        'صيانة دورية',
        'ترميم وتجديد'
    ]

    economic_classifications = [
        'مشاريع البنية التحتية',
        'الخدمات العامة',
        'التطوير والصيانة',
        'المشاريع الاستراتيجية',
        'الصيانة الدورية'
    ]

    industrial_classifications = [
        'إنشاءات',
        'صيانة',
        'خدمات فنية',
        'مقاولات عامة',
        'خدمات متخصصة'
    ]

    # Generate data
    data = {
        'القطاع': np.random.choice(sectors, n_records),
        'القسم': np.random.choice(departments, n_records),
        'الإدارة': np.random.choice(administrations, n_records),
        'التنظيم الإداري': np.random.choice(
            ['مركزي', 'فرعي', 'إقليمي', 'محلي'],
            n_records
        ),
        'اسم العقد': [
            f"عقد رقم {2020+i//100}-{i%100+1:03d}"
            for i in range(n_records)
        ],
        'المقاول الرئيسي': np.random.choice(contractors, n_records),
        'اسم المشروع': np.random.choice(project_types, n_records),
        'التصنيف الاقتصادي': np.random.choice(economic_classifications, n_records),
        'رأسمالي / تشغيلي': np.random.choice(
            ['رأسمالي', 'تشغيلي', 'مختلط'],
            n_records,
            p=[0.4, 0.5, 0.1]
        ),
        'التصنيف الصناعي': np.random.choice(industrial_classifications, n_records),
    }

    # Generate realistic contract values (in SAR)
    # Using log-normal distribution for realistic spread
    contract_values = np.random.lognormal(mean=14, sigma=1.5, size=n_records)
    contract_values = np.round(contract_values / 10000) * 10000  # Round to nearest 10k
    data['قيمة الارتباط'] = contract_values

    # Generate durations (in months)
    durations = np.random.choice(
        [3, 6, 12, 18, 24, 36, 48],
        n_records,
        p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.05, 0.05]
    )
    data['المدة'] = durations

    # Generate award dates (2020-2024)
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)
    date_range = (end_date - start_date).days

    award_dates = [
        start_date + timedelta(days=np.random.randint(0, date_range))
        for _ in range(n_records)
    ]
    data['تاريخ الترسية'] = [d.strftime('%Y-%m-%d') for d in award_dates]

    # Generate contract end dates based on award date + duration
    end_dates = [
        award_dates[i] + timedelta(days=durations[i] * 30)
        for i in range(n_records)
    ]
    data['تاريخ نهاية العقد'] = [d.strftime('%Y-%m-%d') for d in end_dates]

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    os.makedirs('data/raw', exist_ok=True)
    output_path = 'data/raw/saudi_contracts_sample.csv'
    df.to_csv(output_path, index=False, encoding='utf-8-sig')

    print(f"✓ Created sample dataset: {output_path}")
    print(f"   Records: {len(df):,}")
    print(f"   Columns: {len(df.columns)}")
    print(f"   Date range: {df['تاريخ الترسية'].min()} to {df['تاريخ الترسية'].max()}")
    print(f"   Total contract value: SAR {df['قيمة الارتباط'].sum():,.0f}")
    print(f"   Average contract value: SAR {df['قيمة الارتباط'].mean():,.0f}")
    print(f"   Median contract value: SAR {df['قيمة الارتباط'].median():,.0f}\n")

    return output_path

def consolidate_data():
    """Consolidate data from all successful collection methods"""
    print_header("DATA CONSOLIDATION")

    data_files = []

    # Check for Kaggle data
    kaggle_dir = 'data/raw'
    if os.path.exists(kaggle_dir):
        for file in os.listdir(kaggle_dir):
            if file.endswith(('.csv', '.xlsx', '.xls')) and 'metadata' not in file.lower():
                data_files.append(os.path.join(kaggle_dir, file))

    if data_files:
        print(f"✓ Found {len(data_files)} data file(s)")
        for f in data_files:
            print(f"   - {f}")
    else:
        print("ℹ️  No additional data files found from external sources")

    print()
    return data_files

def main():
    """Main orchestrator"""
    print_header("SAUDI ARABIA PROCUREMENT DATA COLLECTOR")
    print("This script attempts multiple methods to collect real data:\n")
    print("1. Kaggle datasets (requires API credentials)")
    print("2. Saudi Open Data Portal (requires network access)")
    print("3. Sample realistic data (fallback)\n")

    # Install requirements
    install_requirements()

    # Try each method
    success_kaggle = try_kaggle_download()
    success_open_data = try_saudi_open_data()

    # Always create sample data as baseline
    sample_path = create_sample_realistic_data()

    # Consolidate
    all_files = consolidate_data()

    # Final summary
    print_header("COLLECTION COMPLETE")

    if success_kaggle or success_open_data:
        print("✓ Real data collected successfully")
        print(f"✓ Sample data also available at: {sample_path}")
    else:
        print("ℹ️  Real data sources not accessible at this time")
        print(f"✓ Sample realistic data created at: {sample_path}")
        print("\nTo get real data:")
        print("  1. Set up Kaggle API: https://www.kaggle.com/docs/api")
        print("  2. Ensure network access to od.data.gov.sa")
        print("  3. Or manually download datasets from:")
        print("     - https://www.kaggle.com/datasets/mohamedramadan2040/saudi-arabia-project-data")
        print("     - https://od.data.gov.sa/en/government-procurement")

    print("\n" + "="*70)
    print("NEXT STEP: Review the data and run the analysis script")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
