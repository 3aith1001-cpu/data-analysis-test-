#!/usr/bin/env python3
"""
Kaggle Dataset Downloader for Saudi Arabia Construction/Procurement Data
This script downloads relevant datasets from Kaggle.
"""

import os
import subprocess
import sys

def install_kaggle():
    """Install Kaggle API if not already installed"""
    try:
        import kaggle
        print("✓ Kaggle API already installed")
    except ImportError:
        print("Installing Kaggle API...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "kaggle", "-q"])
        print("✓ Kaggle API installed successfully")

def setup_kaggle_credentials():
    """
    Setup Kaggle credentials
    User needs to download kaggle.json from https://www.kaggle.com/settings
    and place it in ~/.kaggle/ directory
    """
    kaggle_dir = os.path.expanduser("~/.kaggle")
    kaggle_json = os.path.join(kaggle_dir, "kaggle.json")

    if not os.path.exists(kaggle_json):
        print("\n" + "="*70)
        print("KAGGLE CREDENTIALS REQUIRED")
        print("="*70)
        print("\nTo download datasets from Kaggle, you need to:")
        print("1. Go to https://www.kaggle.com/settings")
        print("2. Scroll to 'API' section")
        print("3. Click 'Create New API Token'")
        print("4. Save the downloaded 'kaggle.json' to:", kaggle_dir)
        print("\nOr set environment variables:")
        print("  export KAGGLE_USERNAME=your_username")
        print("  export KAGGLE_KEY=your_api_key")
        print("="*70)
        return False

    # Set proper permissions
    os.chmod(kaggle_json, 0o600)
    print(f"✓ Kaggle credentials found at {kaggle_json}")
    return True

def download_dataset(dataset_name, output_dir="data/raw"):
    """Download a specific Kaggle dataset"""
    try:
        os.makedirs(output_dir, exist_ok=True)

        print(f"\n📥 Downloading: {dataset_name}")
        print(f"   Output directory: {output_dir}")

        # Use Kaggle API to download
        subprocess.check_call([
            "kaggle", "datasets", "download",
            "-d", dataset_name,
            "-p", output_dir,
            "--unzip"
        ])

        print(f"✓ Successfully downloaded: {dataset_name}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to download {dataset_name}: {e}")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def main():
    """Main function to download all relevant Saudi datasets"""

    print("\n" + "="*70)
    print("SAUDI ARABIA CONSTRUCTION & PROCUREMENT DATA DOWNLOADER")
    print("="*70)

    # Install Kaggle API
    install_kaggle()

    # Check credentials
    if not setup_kaggle_credentials():
        print("\n⚠️  Cannot proceed without Kaggle credentials")
        print("Please set up credentials and run this script again.\n")
        return

    # List of relevant datasets to download
    datasets = [
        "mohamedramadan2040/saudi-arabia-project-data",  # Most recent (Dec 2024)
        "ghadahaltwalah/saudi-projects-dataset",          # Historical project data
        "mohdph/saudi-arabia-real-estate-dataset",        # Real estate data
    ]

    print(f"\n📋 Found {len(datasets)} datasets to download\n")

    successful = 0
    failed = 0

    for dataset in datasets:
        if download_dataset(dataset):
            successful += 1
        else:
            failed += 1

    # Summary
    print("\n" + "="*70)
    print("DOWNLOAD SUMMARY")
    print("="*70)
    print(f"✓ Successful: {successful}")
    print(f"✗ Failed: {failed}")
    print(f"📁 Data saved to: data/raw/")
    print("="*70 + "\n")

    if successful > 0:
        print("✓ You can now run the data consolidation script to merge datasets")

if __name__ == "__main__":
    main()
