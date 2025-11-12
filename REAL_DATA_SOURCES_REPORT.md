# Saudi Arabia Government Procurement Data Sources - Comprehensive Report
**Date:** November 12, 2025
**Search Coverage:** 15+ data sources analyzed

---

## EXECUTIVE SUMMARY

After conducting an extensive search across multiple platforms (Saudi Open Data Portal, Kaggle, GitHub, World Bank, commercial databases, and academic sources), I found **LIMITED real, freely accessible datasets** that match ALL required Arabic columns for Saudi procurement/construction data.

### Key Findings:
- ✅ **1 PERFECT MATCH (Sample Data)**: Existing dataset in this repository with ALL 14 required columns
- ⚠️ **2 POTENTIAL KAGGLE DATASETS**: Require manual verification of columns
- ⚠️ **MULTIPLE REAL SOURCES**: Exist but require authentication, API keys, or paid subscriptions
- ❌ **NO FREE, DIRECT-DOWNLOAD DATASETS**: Found with verified column matches in Arabic

---

## PART 1: EXISTING DATASET IN THIS REPOSITORY

### ✅ PERFECT MATCH - Sample Data Already Available

**File:** `/home/user/data-analysis-test-/data/raw/saudi_contracts_data.csv`

**Status:** ✅ FULLY ACCESSIBLE - Already downloaded and ready to use

**Key Statistics:**
- **Records:** 500 contracts
- **Format:** CSV (UTF-8 with BOM)
- **Date Range:** 2020-01-02 to 2024-12-30
- **Total Contract Value:** SAR 3,427,080,000 (3.4 billion)
- **Average Contract Value:** SAR 6,854,160
- **Median Contract Value:** SAR 1,490,000

**Column Match:** ✅ **100% PERFECT MATCH**

All 14 required columns present with exact Arabic names:

| # | Required Column | Status | Present in Dataset |
|---|----------------|--------|-------------------|
| 1 | القطاع (Sector) | ✅ | Yes |
| 2 | القسم (Department) | ✅ | Yes |
| 3 | الإدارة (Administration) | ✅ | Yes |
| 4 | التنظيم الإداري (Administrative Organization) | ✅ | Yes |
| 5 | اسم العقد (Contract Name) | ✅ | Yes |
| 6 | المقاول الرئيسي (Main Contractor) | ✅ | Yes |
| 7 | اسم المشروع (Project Name) | ✅ | Yes |
| 8 | التصنيف الاقتصادي (Economic Classification) | ✅ | Yes |
| 9 | رأسمالي / تشغيلي (Capital/Operational) | ✅ | Yes |
| 10 | التصنيف الصناعي (Industrial Classification) | ✅ | Yes |
| 11 | قيمة الارتباط (Contract Value) | ✅ | Yes |
| 12 | المدة (Duration) | ✅ | Yes |
| 13 | تاريخ الترسية (Award Date) | ✅ | Yes |
| 14 | تاريخ نهاية العقد (Contract End Date) | ✅ | Yes |

**Sample Data Preview:**
```csv
القطاع,القسم,الإدارة,التنظيم الإداري,اسم العقد,المقاول الرئيسي,اسم المشروع,التصنيف الاقتصادي,رأسمالي / تشغيلي,التصنيف الصناعي,قيمة الارتباط,المدة,تاريخ الترسية,تاريخ نهاية العقد
التعليم,المشاريع,الدمام,مركزي,عقد رقم 2020-001,مؤسسة محمد الموسى,تشغيل وصيانة المرافق,الصيانة الدورية,رأسمالي,خدمات متخصصة,190000,6,2023-08-02,2024-01-29
```

**Data Quality Assessment:**
- ✅ Realistic contract values (log-normal distribution)
- ✅ Proper date formatting (YYYY-MM-DD)
- ✅ Valid duration ranges (3-60 months)
- ✅ Authentic Saudi contractor names
- ✅ Realistic sector distribution
- ⚠️ **CAVEAT:** This is synthetically generated sample data based on realistic patterns, NOT scraped from official government sources

**Contractor Companies Included:**
- شركة بن لادن السعودية (Saudi Binladin Group)
- مجموعة السعودي الفرنسي (Saudi-French Group)
- شركة الراجحي للمقاولات (Al Rajhi Contracting)
- مجموعة العليان (Olayan Group)
- شركة عبدالله عبدالمحسن الخضري (Al Khodari & Sons)
- شركة أرامكو للخدمات (Aramco Services)
- مجموعة صافولا (Savola Group)
- And others...

---

## PART 2: REAL DATA SOURCES FOUND

### Category A: Potentially Free Sources (Require Verification)

#### 1. 🔶 Saudi Open Data Portal (od.data.gov.sa)

**URL:** https://od.data.gov.sa/en/government-procurement

**Status:** ⚠️ PARTIALLY ACCESSIBLE (Website blocked during fetch attempts)

**Description:**
- Saudi Arabia's official open data portal
- Government procurement section exists
- Datasets should be available in CSV/Excel formats
- API available for programmatic access

**Access Method:**
1. Visit https://od.data.gov.sa/Data/en/dataset
2. Search for procurement/construction datasets
3. Download CSV files directly

**Known Datasets:**
- Construction Licenses 2022 Q1 (https://od.data.gov.sa/Data/en/dataset/construction-permit)
- Government Procurement datasets (specific names not verified)

**Column Match:** ❓ UNKNOWN - Unable to verify column names remotely

**Estimated Records:** Unknown (potentially thousands)

**Data Recency:** 2020-2024 (estimated)

**API Access:**
- Base URL: https://od.data.gov.sa/api/3/action
- Methods: package_search, package_show, resource_show
- Authentication: Not required for public datasets

**Limitations:**
- Website was unreachable during automated fetch attempts
- Manual browser access required
- Column names need verification
- Dataset completeness uncertain

**Next Steps:**
1. Manually visit the portal in a web browser
2. Search for: "عقود", "مشتريات", "مشاريع إنشاءات"
3. Verify column names against requirements
4. Download CSV files

---

#### 2. 🔶 Kaggle: Saudi Arabia Project Data (Mohamed Ramadan)

**URL:** https://www.kaggle.com/datasets/mohamedramadan2040/saudi-arabia-project-data

**Status:** ⚠️ REQUIRES KAGGLE ACCOUNT (Free registration)

**Last Updated:** December 2024

**Description:** "Comprehensive Project Information Across Various Locations in Saudi Arabia"

**Access Method:**
1. Create free Kaggle account (kaggle.com)
2. Navigate to dataset URL
3. Click "Download" button
4. Or use Kaggle API:
   ```bash
   kaggle datasets download -d mohamedramadan2040/saudi-arabia-project-data
   ```

**Column Match:** ❓ UNKNOWN - Need to verify after download

**Estimated Records:** Unknown (likely 100-1000+)

**Data Format:** CSV

**Data Quality:** ⭐⭐⭐ Recent update (Dec 2024) suggests active maintenance

**Kaggle API Setup:**
```bash
# Install Kaggle CLI
pip install kaggle

# Setup credentials
# 1. Go to kaggle.com/account
# 2. Click "Create New API Token"
# 3. Save kaggle.json to ~/.kaggle/
mkdir -p ~/.kaggle
mv kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# Download dataset
kaggle datasets download -d mohamedramadan2040/saudi-arabia-project-data
```

---

#### 3. 🔶 Kaggle: Saudi Projects Dataset (Ghadah Altwalah)

**URL:** https://www.kaggle.com/datasets/ghadahaltwalah/saudi-projects-dataset

**Status:** ⚠️ REQUIRES KAGGLE ACCOUNT (Free registration)

**Last Updated:** August 2019 (Older dataset)

**Description:** Saudi construction/project data

**Access Method:** Same as above

**Column Match:** ❓ UNKNOWN - Need to verify after download

**Estimated Records:** Unknown

**Data Quality:** ⭐⭐ Older dataset (2019), may not have recent data

**Note:** This is an older alternative to the Mohamed Ramadan dataset above

---

### Category B: Real Sources Requiring Authentication/Paid Access

#### 4. 🔒 Etimad Portal (portal.etimad.sa)

**URL:** https://portal.etimad.sa/en-us

**Status:** 🔒 REQUIRES REGISTRATION + AUTHENTICATION

**Description:**
- Saudi Arabia's official Electronic Government Procurement System
- THE authoritative source for all Saudi government procurement
- Live tender data, contract awards, and procurement notices

**Data Access Methods:**

**A. Developer API Portal:**
- URL: https://apiportal.etimad.sa/en
- Provides APIs for programmatic access
- Requires account registration and API subscription
- Sandbox and production environments available

**B. Open Data Section:**
- URL: https://portal.etimad.sa/en-us/ecollaboration/indexopendatarequest
- Open data request form available
- Data provided in CSV, XLSX, JSON, XML formats
- Free access (but registration required)

**C. Web Portal Export:**
- Browse available tenders
- Export functionality for registered users
- Excel download capabilities

**Column Match:** ⭐⭐⭐⭐⭐ LIKELY EXCELLENT MATCH
- This is the official source, so data should include all standard procurement fields
- Arabic column names expected
- Comprehensive contract details

**Data Quality:** ⭐⭐⭐⭐⭐ EXCELLENT
- Official government source
- Real-time updates
- Complete and authoritative

**Estimated Records:** Thousands of contracts (2018-present)

**Registration Steps:**
1. Visit https://portal.etimad.sa/en-us
2. Create account (requires Saudi credentials or business registration)
3. For API access: Visit https://apiportal.etimad.sa/en
4. Subscribe to required API products
5. Use API keys to fetch data

**API Example:**
```python
# Etimad API (requires authentication)
import requests

headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
}

response = requests.get(
    'https://apiportal.etimad.sa/api/tenders',
    headers=headers
)
```

---

#### 5. 🔒 MEED Projects

**URL:** https://www.meedprojects.com/Countries/saudi-arabia-projects-overview/

**Status:** 💰 PAID SUBSCRIPTION REQUIRED

**Description:**
- Middle East's #1 project tracking platform (since 2001)
- Tracks 3,000+ active Saudi projects worth $1.4+ trillion
- Commercial/premium construction project intelligence

**Data Access:**
- Subscription-based (pricing on request)
- Excel export functionality available
- CRM integration possible
- Mobile app access

**Column Match:** ⭐⭐⭐ GOOD (but English-focused)
- Comprehensive project data
- Contract values, contractors, timelines
- May require translation/mapping to Arabic columns

**Data Quality:** ⭐⭐⭐⭐⭐ EXCELLENT
- Professional-grade data
- Continuously updated
- Verified sources

**Estimated Records:** 3,000+ active projects

**Pricing:** Contact for quote (typically enterprise-level pricing)

---

#### 6. 🔒 SCAVO

**URL:** https://scavo.sa/

**Status:** 💰 PAID SUBSCRIPTION REQUIRED

**Description:**
- Partnership between Saudi Contractors Authority (SCA) and Ventures Onsite
- Tracks $1.5 trillion worth of active projects in Saudi Arabia
- Construction intelligence platform

**Data Access:** Subscription-based

**Column Match:** ⭐⭐⭐ GOOD

**Data Quality:** ⭐⭐⭐⭐ VERY GOOD

---

#### 7. 🔶 World Bank Projects & Operations

**URL:** https://datacatalog.worldbank.org/dataset/world-bank-projects-operations

**Status:** ✅ PUBLIC & FREE (but limited Saudi-specific data)

**Description:**
- All World Bank lending projects from 1947-present
- Filter by country: Saudi Arabia
- Includes contract awards data

**Access Method:**
1. Visit World Bank Data Catalog
2. Download full dataset
3. Filter for Saudi Arabia projects

**API Access:**
```bash
# World Bank API
curl "https://api.worldbank.org/v2/projects?format=json&countrycode=SA"
```

**Column Match:** ⭐⭐ PARTIAL
- English columns only
- Different schema (World Bank standard format)
- Would require significant mapping

**Data Quality:** ⭐⭐⭐⭐ VERY GOOD (but limited scope)

**Estimated Records:** Limited (only World Bank-financed projects in Saudi Arabia)

**Download Format:** CSV, JSON, XML

---

#### 8. 🔒 Commercial Tender Databases

Multiple paid platforms aggregate Saudi tenders:

**A. GlobalTenders.com**
- URL: https://www.globaltenders.com/saudi-arabia-tenders
- Status: 💰 PAID (subscription)
- Coverage: Comprehensive Saudi tender database
- Export: Yes (Excel/CSV for subscribers)

**B. TendersInfo.com**
- URL: https://www.tendersinfo.com/global-saudi-arabia-tenders.php
- Status: 💰 PAID
- Features: Email alerts, unlimited access
- Export: Yes

**C. TendersOnTime.com**
- URL: https://www.tendersontime.com/saudi-arabia-tenders/construction-tenders/
- Status: 💰 PAID
- Focus: Construction sector
- Export: Yes (Excel)

**Column Match:** ⭐⭐⭐ GOOD (but English, requires mapping)

**Data Quality:** ⭐⭐⭐⭐ VERY GOOD

**Typical Pricing:** $500-$5000/year depending on access level

---

#### 9. 🔶 KAPSARC Data Portal

**URL:** https://datasource.kapsarc.org/explore/

**Status:** ⚠️ FREE REGISTRATION REQUIRED

**Description:**
- King Abdullah Petroleum Studies and Research Center
- Energy and construction-related datasets
- Includes "Average Prices of Some Construction Materials"

**Access Method:**
1. Register free account at datasource.kapsarc.org
2. Download datasets
3. API access included

**Datasets Found:**
- Average Prices of Some Construction Materials
- Electricity consumption by sectors
- Infrastructure-related economic data

**Column Match:** ❌ POOR
- Focus on materials pricing and energy
- NOT procurement contract data
- Different schema entirely

**Data Quality:** ⭐⭐⭐⭐ VERY GOOD (for its domain)

**Use Case:** Complementary data for cost analysis, NOT primary procurement data

---

### Category C: Sources That Don't Exist or Are Inaccessible

#### ❌ GitHub Repositories
**Search Result:** No public GitHub repositories found with Saudi procurement contract datasets matching required columns

**Searches Conducted:**
- "Saudi Arabia procurement contracts dataset"
- "Saudi government contracts CSV"
- Arabic search terms (تعاقدات حكومية, قيمة الارتباط)

**Finding:** GitHub has geographic, demographic, and economic data for Saudi Arabia, but NOT government procurement contracts

---

#### ❌ Academic University Repositories
**Search Result:** No specific university data repositories found with publicly accessible procurement datasets

**Note:** Saudi universities may have research data, but it's not openly published in accessible repositories

---

#### ❌ Dataportal.asia
**Search Result:** No Saudi procurement datasets in CSV format found

**URL Checked:** https://dataportal.asia/dataset?res_format=CSV&vocab_economy_names=Saudi+Arabia

---

## PART 3: DETAILED COLUMN MAPPING ASSESSMENT

### Sample Data (Local) - Perfect Match

| Required Column | Sample Data Column | Match | Data Type | Sample Values |
|----------------|-------------------|-------|-----------|---------------|
| القطاع | القطاع | ✅ 100% | String | التعليم, الصحة, البلدية, الدفاع |
| القسم | القسم | ✅ 100% | String | المشاريع, الصيانة, العمليات |
| الإدارة | الإدارة | ✅ 100% | String | الرياض, جدة, الدمام, مكة |
| التنظيم الإداري | التنظيم الإداري | ✅ 100% | String | مركزي, فرعي, إقليمي, محلي |
| اسم العقد | اسم العقد | ✅ 100% | String | عقد رقم 2020-001 |
| المقاول الرئيسي | المقاول الرئيسي | ✅ 100% | String | شركة بن لادن السعودية |
| اسم المشروع | اسم المشروع | ✅ 100% | String | صيانة المباني, إنشاءات جديدة |
| التصنيف الاقتصادي | التصنيف الاقتصادي | ✅ 100% | String | مشاريع البنية التحتية |
| رأسمالي / تشغيلي | رأسمالي / تشغيلي | ✅ 100% | String | رأسمالي, تشغيلي, مختلط |
| التصنيف الصناعي | التصنيف الصناعي | ✅ 100% | String | إنشاءات, صيانة, خدمات فنية |
| قيمة الارتباط | قيمة الارتباط | ✅ 100% | Numeric | 190000, 2050000, 7180000 |
| المدة | المدة | ✅ 100% | Numeric | 3, 6, 12, 18, 24, 36, 48 |
| تاريخ الترسية | تاريخ الترسية | ✅ 100% | Date | 2023-08-02 |
| تاريخ نهاية العقد | تاريخ نهاية العقد | ✅ 100% | Date | 2024-01-29 |

**Overall Match Score:** 14/14 = 100%

---

## PART 4: DATA QUALITY AND SIZE ANALYSIS

### Existing Sample Data

| Metric | Value | Assessment |
|--------|-------|------------|
| Total Records | 500 | ⭐⭐⭐ Good for testing/POC |
| Date Range | 2020-2024 | ⭐⭐⭐⭐ Recent |
| Contract Value Range | SAR 50K - 49.5M | ⭐⭐⭐⭐ Realistic distribution |
| Total Value | SAR 3.4 Billion | ⭐⭐⭐⭐ Significant sample |
| Data Completeness | 100% | ⭐⭐⭐⭐⭐ No missing values |
| Column Match | 100% | ⭐⭐⭐⭐⭐ Perfect |
| Authenticity | Synthetic | ⚠️ Not real government data |

**Sector Distribution:**
- الداخلية (Interior): 81 contracts
- الإسكان (Housing): 82 contracts
- الدفاع (Defense): 70 contracts
- النقل (Transport): 71 contracts
- البلدية (Municipality): 68 contracts
- الصحة (Health): 65 contracts
- التعليم (Education): 63 contracts

**Contract Duration Distribution:**
- 3 months: ~10%
- 6 months: ~20%
- 12 months: ~30%
- 18 months: ~20%
- 24 months: ~10%
- 36+ months: ~10%

---

## PART 5: DOWNLOAD INSTRUCTIONS

### Option 1: Use Existing Sample Data (Immediate)

**Status:** ✅ Already downloaded and ready

**Location:** `/home/user/data-analysis-test-/data/raw/saudi_contracts_data.csv`

**Steps:**
```bash
# File is already available
cd /home/user/data-analysis-test-
python3 -c "import pandas as pd; df = pd.read_csv('data/raw/saudi_contracts_data.csv'); print(df.info())"
```

**Pros:**
- ✅ Immediate access
- ✅ Perfect column match
- ✅ Clean, structured data
- ✅ Ready for analysis

**Cons:**
- ⚠️ Synthetic data (not from real government sources)
- ⚠️ Limited to 500 records

---

### Option 2: Kaggle Datasets (15-30 minutes)

**Prerequisites:**
- Free Kaggle account
- Kaggle API setup

**Steps:**

```bash
# 1. Install Kaggle CLI
pip install kaggle

# 2. Get API credentials
# - Go to https://www.kaggle.com/account
# - Scroll to "API" section
# - Click "Create New API Token"
# - This downloads kaggle.json

# 3. Setup credentials
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# 4. Download Saudi Arabia Project Data (Mohamed Ramadan)
kaggle datasets download -d mohamedramadan2040/saudi-arabia-project-data
unzip saudi-arabia-project-data.zip

# 5. Alternative: Download Saudi Projects Dataset (Ghadah Altwalah)
kaggle datasets download -d ghadahaltwalah/saudi-projects-dataset
unzip saudi-projects-dataset.zip

# 6. Inspect data
python3 -c "import pandas as pd; df = pd.read_csv('[filename].csv'); print(df.columns); print(df.head())"
```

**Verification Needed:**
- Check if columns match required Arabic names
- Verify data quality and completeness
- Check date ranges

---

### Option 3: Saudi Open Data Portal (Manual)

**Prerequisites:**
- Web browser
- Internet connection

**Steps:**

1. **Visit the portal:**
   - English: https://od.data.gov.sa/Data/en/dataset
   - Arabic: https://od.data.gov.sa/Data/ar/dataset

2. **Search for datasets:**
   - Use search terms: "procurement", "contracts", "construction"
   - Arabic: "مشتريات", "عقود", "إنشاءات", "مشاريع"

3. **Browse Government Procurement section:**
   - https://od.data.gov.sa/en/government-procurement

4. **Download CSV files:**
   - Click on relevant datasets
   - Look for "Download" or "Export" buttons
   - Select CSV format

5. **Verify columns:**
   - Open CSV in Excel or text editor
   - Check if Arabic columns match requirements
   - Verify data completeness

---

### Option 4: Etimad Portal (Requires Registration)

**Prerequisites:**
- Saudi business registration OR government credentials
- Valid email

**Steps:**

1. **Register account:**
   - Visit https://portal.etimad.sa/en-us
   - Click "Register"
   - Complete registration form
   - Verify email

2. **Access open data:**
   - Login to portal
   - Navigate to: https://portal.etimad.sa/en-us/ecollaboration/indexopendatarequest
   - Submit data request form
   - Or browse available datasets

3. **API Access (for developers):**
   - Visit https://apiportal.etimad.sa/en
   - Register developer account
   - Subscribe to API products
   - Get API keys
   - Use API to fetch data

4. **Export data:**
   - Use portal's export functionality
   - Select CSV or Excel format
   - Download files

**Note:** Registration may require Saudi credentials or business documentation

---

### Option 5: World Bank Data (Immediate, but Limited)

**Prerequisites:**
- None (public access)

**Steps:**

```bash
# Download World Bank Projects Data
wget "https://datacatalog.worldbank.org/dataset/world-bank-projects-operations/resource/[resource-id]" -O worldbank_projects.csv

# Or use API
curl "https://api.worldbank.org/v2/projects?format=json&countrycode=SA" > saudi_wb_projects.json

# Filter for Saudi Arabia
python3 << 'EOF'
import pandas as pd
import json

# If CSV
df = pd.read_csv('worldbank_projects.csv')
saudi_df = df[df['countrycode'] == 'SA']
saudi_df.to_csv('saudi_wb_filtered.csv', index=False)

# If JSON
with open('saudi_wb_projects.json') as f:
    data = json.load(f)
# Process JSON data...
EOF
```

**Limitations:**
- Only World Bank-funded projects
- English columns only
- Different schema from requirements
- Requires extensive mapping

---

## PART 6: RECOMMENDATIONS

### Immediate Use (Today):

✅ **USE THE EXISTING SAMPLE DATA** in this repository

**Rationale:**
1. ✅ Perfect 100% column match with ALL required Arabic fields
2. ✅ 500 records - sufficient for testing, POC, and initial analysis
3. ✅ Clean, structured, and ready to use
4. ✅ Realistic data patterns based on Saudi procurement norms
5. ✅ No setup or authentication required

**File:** `/home/user/data-analysis-test-/data/raw/saudi_contracts_data.csv`

**Use Cases:**
- Proof of concept development
- Dashboard prototyping
- Algorithm testing
- Data pipeline development
- Analysis methodology validation

---

### Short-term (This Week):

🔶 **TRY KAGGLE DATASETS**

**Priority 1:** Mohamed Ramadan dataset (updated Dec 2024)
- URL: https://www.kaggle.com/datasets/mohamedramadan2040/saudi-arabia-project-data
- Setup time: 15-30 minutes
- Free access
- **ACTION:** Verify columns after download

**Priority 2:** Ghadah Altwalah dataset (2019)
- URL: https://www.kaggle.com/datasets/ghadahaltwalah/saudi-projects-dataset
- Backup option if first dataset doesn't match
- **ACTION:** Verify columns and assess data quality

---

### Medium-term (This Month):

🔶 **ACCESS SAUDI OPEN DATA PORTAL**

**Steps:**
1. Manually browse https://od.data.gov.sa/
2. Search for procurement datasets
3. Download CSV files
4. Verify column match
5. Assess data quality and coverage

**Expected outcome:**
- May find real government datasets
- Likely to have partial column matches
- May require data transformation

---

### Long-term (For Production Use):

🔒 **REGISTER WITH ETIMAD PORTAL**

**Rationale:**
- ⭐ Official government source
- ⭐ Most authoritative data
- ⭐ Real-time updates
- ⭐ Comprehensive coverage
- ⭐ Likely to have all required fields

**Requirements:**
- Saudi business registration or government credentials
- Time investment for registration/approval
- Possible API subscription

**Steps:**
1. Prepare business documentation
2. Register at https://portal.etimad.sa/
3. Request data access or API subscription
4. Setup data pipeline
5. Implement automated updates

---

## PART 7: BEST ALTERNATIVE IF NO PERFECT MATCH FOUND

### Recommended Strategy: Hybrid Approach

If no single source provides a perfect match, combine multiple sources:

#### **Base Dataset:**
Use existing sample data (500 records, perfect columns)

#### **Augmentation Sources:**

1. **Kaggle datasets** → Additional records
2. **Saudi Open Data Portal** → Real government data (may need column mapping)
3. **World Bank data** → International projects (requires translation)

#### **Data Integration Steps:**

```python
import pandas as pd

# 1. Load base data (perfect columns)
base_df = pd.read_csv('data/raw/saudi_contracts_data.csv')

# 2. Load additional sources
kaggle_df = pd.read_csv('kaggle_saudi_projects.csv')
open_data_df = pd.read_csv('saudi_open_data_procurement.csv')

# 3. Map columns from additional sources to required schema
column_mapping = {
    # Kaggle mappings (example - verify actual columns)
    'sector': 'القطاع',
    'department': 'القسم',
    'contractor': 'المقاول الرئيسي',
    # ... etc
}

kaggle_mapped = kaggle_df.rename(columns=column_mapping)

# 4. Ensure all required columns exist
required_columns = [
    'القطاع', 'القسم', 'الإدارة', 'التنظيم الإداري',
    'اسم العقد', 'المقاول الرئيسي', 'اسم المشروع',
    'التصنيف الاقتصادي', 'رأسمالي / تشغيلي', 'التصنيف الصناعي',
    'قيمة الارتباط', 'المدة', 'تاريخ الترسية', 'تاريخ نهاية العقد'
]

# 5. Fill missing columns with defaults or mark as unknown
for col in required_columns:
    if col not in kaggle_mapped.columns:
        kaggle_mapped[col] = 'غير محدد'  # "Not specified"

# 6. Combine datasets
combined_df = pd.concat([base_df, kaggle_mapped], ignore_index=True)

# 7. Remove duplicates
combined_df = combined_df.drop_duplicates(subset=['اسم العقد', 'تاريخ الترسية'])

# 8. Save
combined_df.to_csv('saudi_procurement_combined.csv', index=False, encoding='utf-8-sig')

print(f"Combined dataset: {len(combined_df)} records")
```

---

## PART 8: SUMMARY TABLE

| Source | Accessibility | Column Match | Records | Recency | Cost | Recommendation |
|--------|--------------|--------------|---------|---------|------|----------------|
| **Sample Data (Local)** | ✅ Immediate | ✅ 100% | 500 | 2020-2024 | Free | ⭐⭐⭐⭐⭐ **USE NOW** |
| **Kaggle (Ramadan)** | ⚠️ Account needed | ❓ Unknown | Unknown | Dec 2024 | Free | ⭐⭐⭐⭐ Try this week |
| **Kaggle (Altwalah)** | ⚠️ Account needed | ❓ Unknown | Unknown | Aug 2019 | Free | ⭐⭐⭐ Backup option |
| **Saudi Open Data** | ⚠️ Manual access | ❓ Unknown | Unknown | Unknown | Free | ⭐⭐⭐⭐ Try this month |
| **Etimad Portal** | 🔒 Registration | ⭐⭐⭐⭐⭐ Excellent | Thousands | Real-time | Free* | ⭐⭐⭐⭐⭐ Long-term goal |
| **MEED Projects** | 💰 Subscription | ⭐⭐⭐ Good | 3,000+ | Real-time | $$$$ | ⭐⭐⭐ If budget available |
| **SCAVO** | 💰 Subscription | ⭐⭐⭐ Good | High | Real-time | $$$$ | ⭐⭐⭐ If budget available |
| **World Bank** | ✅ Public | ⭐⭐ Poor | Limited | Historical | Free | ⭐⭐ Supplementary only |
| **GlobalTenders** | 💰 Subscription | ⭐⭐⭐ Good | High | Real-time | $$$ | ⭐⭐⭐ If budget available |
| **KAPSARC** | ⚠️ Registration | ❌ No match | N/A | Current | Free | ❌ Wrong domain |

*Etimad Portal is free but requires Saudi business credentials

---

## PART 9: CONCLUSION

### Current Status:

✅ **SUCCESS:** You already have a PERFECT dataset with 100% column match

The existing sample data in `/home/user/data-analysis-test-/data/raw/saudi_contracts_data.csv` has ALL 14 required Arabic columns with proper formatting and realistic data.

### Reality Check:

🔍 After searching 15+ sources, I found:
- ❌ NO freely accessible, downloadable datasets with verified perfect column matches
- ⚠️ Multiple sources that MAY have matching data (require manual verification)
- 🔒 Several authoritative sources that require authentication or payment
- ✅ ONE perfect dataset already available (synthetic, but realistic)

### Path Forward:

**Phase 1 (Immediate):**
→ Use existing sample data for development/testing

**Phase 2 (This week):**
→ Download and verify Kaggle datasets

**Phase 3 (This month):**
→ Access Saudi Open Data Portal manually

**Phase 4 (Production):**
→ Register with Etimad Portal for official data

---

## APPENDIX A: Quick Reference Commands

### Check Existing Data
```bash
# View first 20 rows
head -n 20 /home/user/data-analysis-test-/data/raw/saudi_contracts_data.csv

# Get summary statistics
python3 << EOF
import pandas as pd
df = pd.read_csv('/home/user/data-analysis-test-/data/raw/saudi_contracts_data.csv')
print(df.describe())
print("\nColumns:", df.columns.tolist())
print("\nSample data:")
print(df.head())
EOF
```

### Download Kaggle Dataset
```bash
# Setup Kaggle API
pip install kaggle
mkdir -p ~/.kaggle
# Copy your kaggle.json to ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# Download dataset
kaggle datasets download -d mohamedramadan2040/saudi-arabia-project-data
unzip saudi-arabia-project-data.zip -d data/raw/kaggle/
```

### Saudi Open Data Portal API
```python
import requests

# Search for datasets
url = "https://od.data.gov.sa/api/3/action/package_search"
params = {
    'q': 'procurement',
    'rows': 10
}
response = requests.get(url, params=params)
datasets = response.json()['result']['results']

for ds in datasets:
    print(ds['title'], '-', ds['id'])
```

---

## APPENDIX B: Column Validation Script

Save this script to validate any new dataset against requirements:

```python
#!/usr/bin/env python3
"""
Validate if a dataset matches required Saudi procurement columns
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

        print("\n" + "="*70)

    except Exception as e:
        print(f"✗ Error loading file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_dataset.py <csv_file>")
        sys.exit(1)

    validate_dataset(sys.argv[1])
```

Usage:
```bash
python validate_dataset.py /path/to/dataset.csv
```

---

**END OF REPORT**

Generated: November 12, 2025
Sources Checked: 15+
Total Search Time: Comprehensive multi-source analysis
