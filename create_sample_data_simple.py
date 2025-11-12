#!/usr/bin/env python3
"""
Simple data creator using only Python standard library
Creates sample Saudi procurement data without external dependencies
"""

import csv
import random
import json
from datetime import datetime, timedelta
import os

def create_sample_data():
    """Create realistic sample Saudi procurement data"""

    print("\n" + "="*70)
    print("SAUDI PROCUREMENT DATA GENERATOR".center(70))
    print("="*70 + "\n")

    # Set random seed
    random.seed(42)

    # Number of records
    n_records = 500

    # Define realistic data
    sectors = ['الصحة', 'التعليم', 'الدفاع', 'الداخلية', 'النقل', 'الإسكان', 'البلدية']
    departments = ['الصيانة', 'المشاريع', 'العمليات', 'التطوير', 'الخدمات']
    administrations = ['الرياض', 'جدة', 'الدمام', 'مكة', 'المدينة', 'الطائف', 'تبوك', 'أبها', 'القصيم', 'حائل']

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
        'شركة النهدي للتطوير',
        'مؤسسة محمد الموسى',
        'شركة المباني الحديثة'
    ]

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
        'ترميم وتجديد',
        'أعمال النظافة',
        'تشغيل وصيانة المرافق'
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

    org_types = ['مركزي', 'فرعي', 'إقليمي', 'محلي']
    cap_op = ['رأسمالي', 'تشغيلي', 'مختلط']
    durations = [3, 6, 12, 18, 24, 36, 48, 60]

    # Generate records
    records = []

    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)
    date_range = (end_date - start_date).days

    print(f"Generating {n_records} sample contract records...")

    for i in range(n_records):
        # Award date
        award_date = start_date + timedelta(days=random.randint(0, date_range))

        # Duration in months
        duration = random.choice(durations)

        # Contract end date
        end_contract_date = award_date + timedelta(days=duration * 30)

        # Contract value (realistic distribution)
        # Generate values with exponential-like distribution
        rand_val = random.random()
        if rand_val < 0.3:  # 30% small contracts
            contract_value = random.randint(50000, 500000)
        elif rand_val < 0.6:  # 30% medium contracts
            contract_value = random.randint(500000, 2000000)
        elif rand_val < 0.85:  # 25% large contracts
            contract_value = random.randint(2000000, 10000000)
        else:  # 15% very large contracts
            contract_value = random.randint(10000000, 50000000)

        # Round to nearest 10k
        contract_value = int(contract_value / 10000) * 10000

        record = {
            'القطاع': random.choice(sectors),
            'القسم': random.choice(departments),
            'الإدارة': random.choice(administrations),
            'التنظيم الإداري': random.choice(org_types),
            'اسم العقد': f"عقد رقم {2020 + i//100}-{i%100 + 1:03d}",
            'المقاول الرئيسي': random.choice(contractors),
            'اسم المشروع': random.choice(project_types),
            'التصنيف الاقتصادي': random.choice(economic_classifications),
            'رأسمالي / تشغيلي': random.choice(cap_op),
            'التصنيف الصناعي': random.choice(industrial_classifications),
            'قيمة الارتباط': contract_value,
            'المدة': duration,
            'تاريخ الترسية': award_date.strftime('%Y-%m-%d'),
            'تاريخ نهاية العقد': end_contract_date.strftime('%Y-%m-%d')
        }

        records.append(record)

    # Create output directory
    os.makedirs('data/raw', exist_ok=True)

    # Write to CSV
    output_file = 'data/raw/saudi_contracts_data.csv'
    fieldnames = list(records[0].keys())

    with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"\n✓ Dataset created successfully!")
    print(f"   File: {output_file}")
    print(f"   Records: {len(records):,}")
    print(f"   Columns: {len(fieldnames)}")

    # Calculate statistics
    total_value = sum(r['قيمة الارتباط'] for r in records)
    avg_value = total_value / len(records)
    values = sorted([r['قيمة الارتباط'] for r in records])
    median_value = values[len(values)//2]

    min_date = min(r['تاريخ الترسية'] for r in records)
    max_date = max(r['تاريخ الترسية'] for r in records)

    print(f"\n📊 DATASET STATISTICS")
    print(f"   Date range: {min_date} to {max_date}")
    print(f"   Total contract value: SAR {total_value:,.0f}")
    print(f"   Average contract value: SAR {avg_value:,.0f}")
    print(f"   Median contract value: SAR {median_value:,.0f}")
    print(f"   Min contract value: SAR {values[0]:,.0f}")
    print(f"   Max contract value: SAR {values[-1]:,.0f}")

    # Sector breakdown
    sector_counts = {}
    for r in records:
        sector = r['القطاع']
        sector_counts[sector] = sector_counts.get(sector, 0) + 1

    print(f"\n📈 SECTOR DISTRIBUTION")
    for sector, count in sorted(sector_counts.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / len(records)) * 100
        print(f"   {sector}: {count} ({percentage:.1f}%)")

    # Save summary as JSON
    summary = {
        'total_records': len(records),
        'total_columns': len(fieldnames),
        'date_range': {'min': min_date, 'max': max_date},
        'contract_values': {
            'total': total_value,
            'average': avg_value,
            'median': median_value,
            'min': values[0],
            'max': values[-1]
        },
        'sector_distribution': sector_counts,
        'columns': fieldnames
    }

    with open('data/raw/dataset_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Summary saved to: data/raw/dataset_summary.json")
    print("="*70 + "\n")

    return output_file, records

if __name__ == "__main__":
    create_sample_data()
