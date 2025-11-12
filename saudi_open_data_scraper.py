#!/usr/bin/env python3
"""
Saudi Open Data Portal Scraper
Scrapes construction and procurement data from od.data.gov.sa
"""

import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
import time
from datetime import datetime
import os

class SaudiOpenDataScraper:
    """Scraper for Saudi Arabia Open Data Portal"""

    def __init__(self):
        self.base_url = "https://od.data.gov.sa"
        self.api_base = "https://od.data.gov.sa/api/3/action"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def search_datasets(self, query="procurement", rows=100):
        """Search for datasets by keyword"""
        url = f"{self.api_base}/package_search"
        params = {
            'q': query,
            'rows': rows,
            'sort': 'metadata_modified desc'
        }

        try:
            print(f"🔍 Searching for datasets with query: '{query}'...")
            response = self.session.get(url, params=params, timeout=30)

            if response.status_code == 200:
                data = response.json()
                if data.get('success'):
                    results = data['result']['results']
                    print(f"✓ Found {len(results)} datasets")
                    return results

            print(f"⚠️  Search returned status code: {response.status_code}")
            return []

        except Exception as e:
            print(f"✗ Error searching datasets: {e}")
            return []

    def get_dataset_details(self, dataset_id):
        """Get detailed information about a specific dataset"""
        url = f"{self.api_base}/package_show"
        params = {'id': dataset_id}

        try:
            response = self.session.get(url, params=params, timeout=30)
            if response.status_code == 200:
                data = response.json()
                if data.get('success'):
                    return data['result']
            return None
        except Exception as e:
            print(f"✗ Error getting dataset details: {e}")
            return None

    def download_resource(self, resource_url, filename):
        """Download a specific resource file"""
        try:
            print(f"📥 Downloading: {filename}")
            response = self.session.get(resource_url, timeout=60, stream=True)

            if response.status_code == 200:
                os.makedirs('data/raw/saudi_open_data', exist_ok=True)
                filepath = f'data/raw/saudi_open_data/{filename}'

                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

                print(f"✓ Downloaded: {filepath}")
                return filepath
            else:
                print(f"✗ Download failed: HTTP {response.status_code}")
                return None

        except Exception as e:
            print(f"✗ Error downloading resource: {e}")
            return None

    def scrape_procurement_data(self):
        """Scrape procurement-related datasets"""

        print("\n" + "="*70)
        print("SAUDI OPEN DATA PORTAL SCRAPER - PROCUREMENT DATA")
        print("="*70 + "\n")

        # Search for relevant datasets
        keywords = [
            "procurement",
            "contracts",
            "tenders",
            "construction",
            "projects",
            "government contracts"
        ]

        all_datasets = []
        downloaded_files = []

        for keyword in keywords:
            datasets = self.search_datasets(keyword, rows=20)

            for dataset in datasets:
                dataset_id = dataset.get('id')
                title = dataset.get('title', 'Unknown')

                # Avoid duplicates
                if dataset_id in [d.get('id') for d in all_datasets]:
                    continue

                all_datasets.append(dataset)

                print(f"\n📦 Dataset: {title}")
                print(f"   ID: {dataset_id}")

                # Get full dataset details
                details = self.get_dataset_details(dataset_id)

                if details and 'resources' in details:
                    resources = details['resources']
                    print(f"   Resources: {len(resources)} file(s)")

                    # Download CSV/Excel files
                    for resource in resources:
                        format_type = resource.get('format', '').upper()
                        resource_url = resource.get('url')
                        resource_name = resource.get('name', 'unnamed')

                        if format_type in ['CSV', 'XLSX', 'XLS', 'JSON']:
                            filename = f"{dataset_id}_{resource.get('id', 'resource')}.{format_type.lower()}"
                            filepath = self.download_resource(resource_url, filename)

                            if filepath:
                                downloaded_files.append({
                                    'dataset_title': title,
                                    'dataset_id': dataset_id,
                                    'resource_name': resource_name,
                                    'format': format_type,
                                    'filepath': filepath,
                                    'url': resource_url
                                })

                    # Rate limiting
                    time.sleep(1)

        # Save metadata
        if downloaded_files:
            metadata_df = pd.DataFrame(downloaded_files)
            metadata_path = 'data/raw/saudi_open_data/metadata.csv'
            metadata_df.to_csv(metadata_path, index=False)
            print(f"\n✓ Saved metadata to: {metadata_path}")

        # Summary
        print("\n" + "="*70)
        print("SCRAPING SUMMARY")
        print("="*70)
        print(f"✓ Datasets found: {len(all_datasets)}")
        print(f"✓ Files downloaded: {len(downloaded_files)}")
        print(f"📁 Data saved to: data/raw/saudi_open_data/")
        print("="*70 + "\n")

        return downloaded_files

def main():
    """Main execution function"""
    scraper = SaudiOpenDataScraper()
    scraper.scrape_procurement_data()

if __name__ == "__main__":
    main()
