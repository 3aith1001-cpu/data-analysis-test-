#!/usr/bin/env python3
"""
PART 3-4: REGRESSION & TIME SERIES ANALYSIS
===========================================
Comprehensive regression and forecasting techniques
"""

import csv
import json
import math
import statistics
from datetime import datetime, timedelta
from collections import defaultdict
import os

print("\n" + "="*80)
print("PART 3: CORRELATION & REGRESSION ANALYSIS")
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
# CORRELATION ANALYSIS
# ============================================================================

def pearson_correlation(x, y):
    """
    Pearson Correlation Coefficient

    THEORY:
    Measures linear relationship between two variables

    Formula: r = Σ((xᵢ - x̄)(yᵢ - ȳ)) / √(Σ(xᵢ - x̄)² × Σ(yᵢ - ȳ)²)

    where:
    - r ∈ [-1, 1]
    - r = 1: perfect positive correlation
    - r = 0: no linear correlation
    - r = -1: perfect negative correlation

    Interpretation:
    - |r| < 0.3: weak correlation
    - 0.3 ≤ |r| < 0.7: moderate correlation
    - |r| ≥ 0.7: strong correlation
    """
    n = len(x)
    mean_x = statistics.mean(x)
    mean_y = statistics.mean(y)

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = math.sqrt(sum((x[i] - mean_x)**2 for i in range(n)) *
                            sum((y[i] - mean_y)**2 for i in range(n)))

    r = numerator / denominator if denominator != 0 else 0

    if abs(r) < 0.3:
        strength = "weak"
    elif abs(r) < 0.7:
        strength = "moderate"
    else:
        strength = "strong"

    return r, strength

# Correlation: Contract Value vs Duration
values = [r['قيمة الارتباط'] for r in data]
durations = [r['المدة'] for r in data]

r_value_duration, strength = pearson_correlation(values, durations)

print(f"\n📊 PEARSON CORRELATION")
print(f"   Contract Value vs Duration")
print(f"   r = {r_value_duration:.4f}")
print(f"   Strength: {strength}")
print(f"   Interpretation: {'Positive' if r_value_duration > 0 else 'Negative'} {strength} linear relationship")

# ============================================================================
# LINEAR REGRESSION
# ============================================================================

def simple_linear_regression(x, y):
    """
    Simple Linear Regression

    THEORY:
    Fits a line: Y = β₀ + β₁X + ε

    where:
    - β₁ (slope) = Σ((xᵢ - x̄)(yᵢ - ȳ)) / Σ(xᵢ - x̄)²
    - β₀ (intercept) = ȳ - β₁ × x̄

    R² (Coefficient of Determination):
    R² = 1 - (SS_residual / SS_total)

    where:
    - SS_residual = Σ(yᵢ - ŷᵢ)²
    - SS_total = Σ(yᵢ - ȳ)²

    Interpretation of R²:
    - R² = proportion of variance in Y explained by X
    - R² ∈ [0, 1]
    - R² = 1: perfect fit
    - R² = 0: model explains no variance
    """
    n = len(x)
    mean_x = statistics.mean(x)
    mean_y = statistics.mean(y)

    # Calculate slope (β₁)
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = sum((x[i] - mean_x)**2 for i in range(n))
    slope = numerator / denominator if denominator != 0 else 0

    # Calculate intercept (β₀)
    intercept = mean_y - slope * mean_x

    # Calculate R²
    y_pred = [intercept + slope * x[i] for i in range(n)]
    ss_residual = sum((y[i] - y_pred[i])**2 for i in range(n))
    ss_total = sum((y[i] - mean_y)**2 for i in range(n))
    r_squared = 1 - (ss_residual / ss_total) if ss_total != 0 else 0

    # Root Mean Squared Error (RMSE)
    rmse = math.sqrt(ss_residual / n)

    return {
        'slope': slope,
        'intercept': intercept,
        'r_squared': r_squared,
        'rmse': rmse,
        'equation': f"Y = {intercept:.2f} + {slope:.4f}X"
    }

# Regression: Duration predicts Value
regression_duration_value = simple_linear_regression(durations, values)

print(f"\n📊 LINEAR REGRESSION: Duration → Contract Value")
print(f"   Equation: {regression_duration_value['equation']}")
print(f"   R² = {regression_duration_value['r_squared']:.4f}")
print(f"   RMSE = SAR {regression_duration_value['rmse']:,.0f}")
print(f"   Interpretation: Duration explains {regression_duration_value['r_squared']*100:.2f}% of contract value variance")

# ============================================================================
# POLYNOMIAL REGRESSION
# ============================================================================

def polynomial_regression(x, y, degree=2):
    """
    Polynomial Regression

    THEORY:
    Fits polynomial: Y = β₀ + β₁X + β₂X² + β₃X³ + ... + βₙXⁿ

    For degree=2 (quadratic):
    Y = β₀ + β₁X + β₂X²

    This is useful when relationship is non-linear
    Higher degree polynomial can fit complex patterns but risks overfitting
    """
    # Simplified implementation for degree 2
    n = len(x)

    # Create design matrix for polynomial features
    # X, X², mean values
    mean_x = statistics.mean(x)
    mean_x2 = statistics.mean([xi**2 for xi in x])
    mean_y = statistics.mean(y)

    # For full implementation, would use matrix operations
    # Here we'll use a simplified approach

    # Use the correlation-based method for quadratic fit
    # This is approximate but demonstrates the concept

    return {
        'degree': degree,
        'note': 'Polynomial fitting requires matrix operations (numpy)'
    }

print(f"\n📊 POLYNOMIAL REGRESSION")
print(f"   Note: Full polynomial regression requires matrix libraries")
print(f"   Can be implemented with numpy/scipy for production use")

# ============================================================================
# PART 4: TIME SERIES ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("PART 4: TIME SERIES ANALYSIS")
print("="*80)

# Aggregate contracts by month
monthly_data = defaultdict(lambda: {'count': 0, 'total_value': 0})

for row in data:
    year_month = row['تاريخ الترسية'].strftime('%Y-%m')
    monthly_data[year_month]['count'] += 1
    monthly_data[year_month]['total_value'] += row['قيمة الارتباط']

# Sort by date
sorted_months = sorted(monthly_data.keys())
monthly_values = [monthly_data[m]['total_value'] for m in sorted_months]
monthly_counts = [monthly_data[m]['count'] for m in sorted_months]

print(f"\n📊 TIME SERIES DATA")
print(f"   Time points: {len(sorted_months)} months")
print(f"   Date range: {sorted_months[0]} to {sorted_months[-1]}")

# ============================================================================
# MOVING AVERAGE
# ============================================================================

def moving_average(series, window=3):
    """
    Moving Average (Simple)

    THEORY:
    Smooths time series by averaging over a sliding window

    Formula: MA_t = (1/k) × Σ(Y_{t-k+1} to Y_t)

    where:
    - k = window size
    - Larger k = smoother curve but more lag

    Purpose:
    - Remove noise and reveal trends
    - Used for forecasting (Naïve method: forecast = last MA value)
    """
    ma = []
    for i in range(len(series)):
        if i < window - 1:
            ma.append(None)
        else:
            window_vals = series[i-window+1:i+1]
            ma.append(sum(window_vals) / window)
    return ma

ma_3month = moving_average(monthly_values, window=3)
ma_6month = moving_average(monthly_values, window=6)

print(f"\n📊 MOVING AVERAGES")
print(f"   3-month MA calculated: {len([x for x in ma_3month if x])} points")
print(f"   6-month MA calculated: {len([x for x in ma_6month if x])} points")

# ============================================================================
# EXPONENTIAL SMOOTHING
# ============================================================================

def exponential_smoothing(series, alpha=0.3):
    """
    Exponential Smoothing (Simple)

    THEORY:
    Weighted average giving more weight to recent observations

    Formula: S_t = α × Y_t + (1-α) × S_{t-1}

    where:
    - α ∈ [0, 1] is the smoothing parameter
    - α = 0: all weight on past (no smoothing)
    - α = 1: only current observation
    - Typical: α ∈ [0.1, 0.3]

    Initial value: S_0 = Y_0

    Purpose:
    - Short-term forecasting
    - Adapts to level changes more quickly than MA
    """
    smoothed = [series[0]]  # S_0 = Y_0

    for t in range(1, len(series)):
        s_t = alpha * series[t] + (1 - alpha) * smoothed[t-1]
        smoothed.append(s_t)

    return smoothed

es_values = exponential_smoothing(monthly_values, alpha=0.3)

print(f"\n📊 EXPONENTIAL SMOOTHING (α=0.3)")
print(f"   Smoothed series length: {len(es_values)}")
print(f"   Last smoothed value: SAR {es_values[-1]:,.0f}")

# ============================================================================
# TREND ANALYSIS
# ============================================================================

def calculate_trend(series):
    """
    Linear Trend Analysis

    THEORY:
    Fits trend line to time series: Y_t = β₀ + β₁t

    where:
    - t = time index (1, 2, 3, ...)
    - β₁ = slope (trend direction and magnitude)
    - β₁ > 0: upward trend
    - β₁ < 0: downward trend

    Detrended series: Y_t - Ŷ_t (useful for seasonal analysis)
    """
    t = list(range(1, len(series) + 1))
    trend_model = simple_linear_regression(t, series)

    # Calculate trend line values
    trend_line = [trend_model['intercept'] + trend_model['slope'] * ti for ti in t]

    # Detrended values
    detrended = [series[i] - trend_line[i] for i in range(len(series))]

    return {
        'slope': trend_model['slope'],
        'intercept': trend_model['intercept'],
        'r_squared': trend_model['r_squared'],
        'trend_line': trend_line,
        'detrended': detrended
    }

trend_analysis = calculate_trend(monthly_values)

print(f"\n📊 TREND ANALYSIS")
print(f"   Trend slope: {trend_analysis['slope']:,.0f} SAR/month")
print(f"   R² = {trend_analysis['r_squared']:.4f}")
print(f"   Trend direction: {'Upward' if trend_analysis['slope'] > 0 else 'Downward'}")

# ============================================================================
# GROWTH RATE CALCULATION
# ============================================================================

def calculate_growth_rates(series):
    """
    Growth Rate Analysis

    THEORY:
    Period-over-period growth rate

    Formula: g_t = (Y_t - Y_{t-1}) / Y_{t-1} × 100%

    Compound Annual Growth Rate (CAGR):
    CAGR = (V_final / V_initial)^(1/n) - 1

    where n = number of periods
    """
    growth_rates = []
    for i in range(1, len(series)):
        if series[i-1] != 0:
            gr = ((series[i] - series[i-1]) / series[i-1]) * 100
            growth_rates.append(gr)
        else:
            growth_rates.append(0)

    avg_growth = statistics.mean(growth_rates) if growth_rates else 0

    # CAGR calculation (annual basis)
    if len(series) > 1 and series[0] > 0:
        n_years = len(series) / 12  # assuming monthly data
        cagr = ((series[-1] / series[0]) ** (1/n_years) - 1) * 100
    else:
        cagr = 0

    return {
        'growth_rates': growth_rates,
        'average_growth': avg_growth,
        'cagr': cagr
    }

growth_analysis = calculate_growth_rates(monthly_values)

print(f"\n📊 GROWTH RATE ANALYSIS")
print(f"   Average monthly growth: {growth_analysis['average_growth']:.2f}%")
print(f"   CAGR: {growth_analysis['cagr']:.2f}%")

# ============================================================================
# SAVE RESULTS
# ============================================================================

results = {
    'correlation_analysis': {
        'value_vs_duration': {
            'pearson_r': r_value_duration,
            'strength': strength
        }
    },
    'linear_regression': regression_duration_value,
    'time_series': {
        'n_months': len(sorted_months),
        'trend': {
            'slope': trend_analysis['slope'],
            'r_squared': trend_analysis['r_squared']
        },
        'growth': {
            'avg_monthly_growth': growth_analysis['average_growth'],
            'cagr': growth_analysis['cagr']
        }
    }
}

os.makedirs('results', exist_ok=True)
with open('results/02_regression_timeseries.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2, default=str)

print("\n✓ Part 3-4 Complete: Regression & time series analysis saved")
