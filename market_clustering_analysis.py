#!/usr/bin/env python3
"""
PART 5-6: MARKET CONCENTRATION & CLUSTER ANALYSIS
==================================================
Market structure analysis and segmentation
"""

import csv
import json
import math
import statistics
from datetime import datetime
from collections import Counter, defaultdict
import os

print("\n" + "="*80)
print("PART 5: MARKET CONCENTRATION ANALYSIS")
print("="*80)

# Load data
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

data = load_data('data/raw/saudi_contracts_data.csv')

# ============================================================================
# HERFINDAHL-HIRSCHMAN INDEX (HHI)
# ============================================================================

def calculate_hhi(market_shares):
    """
    Herfindahl-Hirschman Index

    THEORY:
    Measures market concentration

    Formula: HHI = Σ(sᵢ²) × 10,000

    where:
    - sᵢ = market share of firm i (as percentage, 0-100)
    - Sum over all firms in market

    Interpretation (US DOJ/FTC guidelines):
    - HHI < 1,500: Competitive market (unconcentrated)
    - 1,500 ≤ HHI < 2,500: Moderately concentrated
    - HHI ≥ 2,500: Highly concentrated

    Properties:
    - Minimum: Approaches 0 (many small firms)
    - Maximum: 10,000 (monopoly, one firm with 100% share)
    - Gives more weight to larger firms (squaring effect)

    Example:
    - 4 firms with 25% each: HHI = 4 × (25²) = 2,500
    - 1 firm with 100%: HHI = 100² = 10,000
    - 100 firms with 1% each: HHI = 100 × (1²) = 100
    """
    hhi = sum(share ** 2 for share in market_shares)

    if hhi < 1500:
        classification = "Competitive (Unconcentrated)"
    elif hhi < 2500:
        classification = "Moderately Concentrated"
    else:
        classification = "Highly Concentrated"

    return hhi, classification

# Calculate contractor market shares
contractor_values = defaultdict(float)
total_market_value = sum(r['قيمة الارتباط'] for r in data)

for row in data:
    contractor_values[row['المقاول الرئيسي']] += row['قيمة الارتباط']

# Convert to market shares (as percentages)
market_shares = [(value / total_market_value) * 100
                 for value in contractor_values.values()]

hhi, hhi_classification = calculate_hhi(market_shares)

print(f"\n📊 HERFINDAHL-HIRSCHMAN INDEX (HHI)")
print(f"   HHI = {hhi:.0f}")
print(f"   Classification: {hhi_classification}")
print(f"   Number of contractors: {len(contractor_values)}")
print(f"   Market structure: {'Fragmented' if hhi < 1500 else 'Concentrated'}")

# ============================================================================
# CONCENTRATION RATIOS (CR4, CR8)
# ============================================================================

def calculate_concentration_ratios(market_shares_dict):
    """
    Concentration Ratios

    THEORY:
    Sum of market shares of top N firms

    CR4 = Market share of top 4 firms
    CR8 = Market share of top 8 firms

    Interpretation:
    - CR4 < 40%: Low concentration
    - 40% ≤ CR4 < 60%: Moderate concentration
    - CR4 ≥ 60%: High concentration (oligopoly)

    Difference from HHI:
    - CR only considers top firms
    - HHI considers all firms with squared weights
    - Both measure concentration but different aspects
    """
    # Sort by market share descending
    sorted_shares = sorted(market_shares_dict.items(),
                          key=lambda x: x[1], reverse=True)

    cr4 = sum(share for _, share in sorted_shares[:4])
    cr8 = sum(share for _, share in sorted_shares[:8])

    top_4_firms = [name for name, _ in sorted_shares[:4]]
    top_8_firms = [name for name, _ in sorted_shares[:8]]

    if cr4 < 40:
        cr4_classification = "Low Concentration"
    elif cr4 < 60:
        cr4_classification = "Moderate Concentration"
    else:
        cr4_classification = "High Concentration (Oligopoly)"

    return {
        'cr4': cr4,
        'cr8': cr8,
        'cr4_classification': cr4_classification,
        'top_4': top_4_firms,
        'top_8': top_8_firms
    }

shares_dict = {contractor: (value / total_market_value) * 100
               for contractor, value in contractor_values.items()}

cr_results = calculate_concentration_ratios(shares_dict)

print(f"\n📊 CONCENTRATION RATIOS")
print(f"   CR4 = {cr_results['cr4']:.2f}%")
print(f"   CR8 = {cr_results['cr8']:.2f}%")
print(f"   Classification: {cr_results['cr4_classification']}")
print(f"\n   Top 4 Contractors:")
for i, contractor in enumerate(cr_results['top_4'], 1):
    print(f"      {i}. {contractor}: {shares_dict[contractor]:.2f}%")

# ============================================================================
# GINI COEFFICIENT
# ============================================================================

def calculate_gini(values):
    """
    Gini Coefficient

    THEORY:
    Measures inequality in distribution

    Formula: G = (Σᵢ Σⱼ |xᵢ - xⱼ|) / (2n² × μ)

    Alternative formula:
    G = (2 × Σᵢ i × xᵢ) / (n × Σᵢ xᵢ) - (n + 1) / n

    where values are sorted in ascending order

    Interpretation:
    - G = 0: Perfect equality (all firms equal size)
    - G = 1: Perfect inequality (one firm has everything)
    - Typically: 0 < G < 1

    Applications:
    - Income inequality (original use)
    - Market share inequality
    - Resource distribution

    Lorenz Curve:
    - Gini = Area between Lorenz curve and equality line
    - Lorenz curve plots cumulative % of firms vs cumulative % of market
    """
    if not values or sum(values) == 0:
        return 0

    sorted_values = sorted(values)
    n = len(sorted_values)
    total = sum(sorted_values)

    # Calculate using alternative formula
    numerator = sum((i + 1) * val for i, val in enumerate(sorted_values))
    gini = (2 * numerator) / (n * total) - (n + 1) / n

    if gini < 0.3:
        interpretation = "Low inequality (competitive)"
    elif gini < 0.6:
        interpretation = "Moderate inequality"
    else:
        interpretation = "High inequality (concentrated)"

    return gini, interpretation

contractor_value_list = list(contractor_values.values())
gini, gini_interpretation = calculate_gini(contractor_value_list)

print(f"\n📊 GINI COEFFICIENT")
print(f"   Gini = {gini:.4f}")
print(f"   Interpretation: {gini_interpretation}")

# ============================================================================
# PART 6: CLUSTER ANALYSIS (K-MEANS SIMPLIFIED)
# ============================================================================

print("\n" + "="*80)
print("PART 6: CLUSTER ANALYSIS & SEGMENTATION")
print("="*80)

def kmeans_1d(values, k=3, max_iterations=100):
    """
    K-Means Clustering (1-Dimensional Simplified)

    THEORY:
    Partitions data into k clusters by minimizing within-cluster variance

    Objective: Minimize Σⱼ Σᵢ ||xᵢ - μⱼ||²

    where:
    - j = cluster index
    - i = data point index
    - μⱼ = centroid of cluster j

    Algorithm:
    1. Initialize k centroids randomly
    2. Assign each point to nearest centroid
    3. Recalculate centroids as mean of assigned points
    4. Repeat 2-3 until convergence or max iterations

    Convergence: When centroids don't change significantly
    """
    # Initialize centroids (evenly spaced quantiles)
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    centroids = [sorted_vals[int(i * n / k)] for i in range(k)]

    for iteration in range(max_iterations):
        # Assign to nearest centroid
        clusters = [[] for _ in range(k)]

        for val in values:
            distances = [abs(val - c) for c in centroids]
            nearest = distances.index(min(distances))
            clusters[nearest].append(val)

        # Recalculate centroids
        new_centroids = []
        for cluster in clusters:
            if cluster:
                new_centroids.append(statistics.mean(cluster))
            else:
                new_centroids.append(centroids[len(new_centroids)])

        # Check convergence
        if new_centroids == centroids:
            break

        centroids = new_centroids

    # Calculate cluster statistics
    cluster_stats = []
    for i, cluster in enumerate(clusters):
        if cluster:
            cluster_stats.append({
                'cluster_id': i,
                'size': len(cluster),
                'mean': statistics.mean(cluster),
                'min': min(cluster),
                'max': max(cluster),
                'std': statistics.stdev(cluster) if len(cluster) > 1 else 0
            })

    return cluster_stats, centroids

# Cluster contracts by value
contract_values = [r['قيمة الارتباط'] for r in data]
value_clusters, centroids = kmeans_1d(contract_values, k=3)

# Assign labels
labels = ["Small Contracts", "Medium Contracts", "Large Contracts"]
for i, cluster in enumerate(sorted(value_clusters, key=lambda x: x['mean'])):
    cluster['label'] = labels[i]

print(f"\n📊 K-MEANS CLUSTERING (Contract Values)")
print(f"   Number of clusters: 3")
print(f"   Total contracts: {len(contract_values)}")

for cluster in sorted(value_clusters, key=lambda x: x['mean']):
    print(f"\n   {cluster['label']}:")
    print(f"      Count: {cluster['size']} ({cluster['size']/len(contract_values)*100:.1f}%)")
    print(f"      Mean: SAR {cluster['mean']:,.0f}")
    print(f"      Range: SAR {cluster['min']:,.0f} - {cluster['max']:,.0f}")

# ============================================================================
# SEGMENTATION ANALYSIS
# ============================================================================

def segment_analysis(data, segment_field, value_field):
    """
    Market Segmentation Analysis

    THEORY:
    Breaks down market by different dimensions:
    - By sector, region, contractor, project type, etc.
    - Calculates size, share, and growth for each segment
    - Identifies high-value segments for targeting

    Metrics:
    - Segment size (count and value)
    - Market share
    - Average transaction size
    - Growth rate (if time dimension available)
    """
    segments = defaultdict(lambda: {'count': 0, 'total_value': 0})

    for row in data:
        segment = row[segment_field]
        value = row[value_field]
        segments[segment]['count'] += 1
        segments[segment]['total_value'] += value

    total_value = sum(s['total_value'] for s in segments.values())

    segment_stats = []
    for segment_name, stats in segments.items():
        segment_stats.append({
            'segment': segment_name,
            'count': stats['count'],
            'total_value': stats['total_value'],
            'avg_value': stats['total_value'] / stats['count'],
            'market_share': (stats['total_value'] / total_value) * 100
        })

    return sorted(segment_stats, key=lambda x: x['total_value'], reverse=True)

# Segment by sector
sector_segments = segment_analysis(data, 'القطاع', 'قيمة الارتباط')

print(f"\n📊 MARKET SEGMENTATION BY SECTOR")
print(f"   Total sectors: {len(sector_segments)}")

for segment in sector_segments[:5]:  # Top 5
    print(f"\n   {segment['segment']}:")
    print(f"      Contracts: {segment['count']}")
    print(f"      Total value: SAR {segment['total_value']:,.0f}")
    print(f"      Market share: {segment['market_share']:.2f}%")
    print(f"      Avg contract: SAR {segment['avg_value']:,.0f}")

# Segment by project type
project_segments = segment_analysis(data, 'اسم المشروع', 'قيمة الارتباط')

print(f"\n📊 MARKET SEGMENTATION BY PROJECT TYPE")
print(f"   Total project types: {len(project_segments)}")

for segment in project_segments[:5]:  # Top 5
    print(f"\n   {segment['segment']}:")
    print(f"      Contracts: {segment['count']}")
    print(f"      Market share: {segment['market_share']:.2f}%")

# ============================================================================
# SAVE RESULTS
# ============================================================================

results = {
    'market_concentration': {
        'hhi': {
            'value': hhi,
            'classification': hhi_classification,
            'n_contractors': len(contractor_values)
        },
        'concentration_ratios': {
            'cr4': cr_results['cr4'],
            'cr8': cr_results['cr8'],
            'classification': cr_results['cr4_classification'],
            'top_4_contractors': cr_results['top_4']
        },
        'gini': {
            'coefficient': gini,
            'interpretation': gini_interpretation
        }
    },
    'clustering': {
        'value_clusters': value_clusters
    },
    'segmentation': {
        'by_sector': sector_segments,
        'by_project_type': project_segments[:10]  # Top 10
    }
}

os.makedirs('results', exist_ok=True)
with open('results/03_market_clustering.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2, default=str)

print("\n✓ Part 5-6 Complete: Market concentration & clustering analysis saved")
