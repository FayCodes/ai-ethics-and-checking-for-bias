import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from aif360.datasets import StandardDataset
from aif360.metrics import ClassificationMetric
import warnings
warnings.filterwarnings('ignore')

plt.style.use('default')
plt.rcParams['figure.figsize'] = (12, 8)

def load_and_explore_data():
    print("Loading COMPAS dataset...")
    df = pd.read_csv('compas-scores-two-years.csv')
    print(f"\nDataset shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nBasic statistics:")
    print(df.describe())
    print("\nMissing values:")
    print(df.isnull().sum())
    return df

def prepare_data_for_analysis(df, protected_attribute):
    print(f"\nPreparing data for bias analysis on {protected_attribute}...")
    feature_columns = []
    label_column = None
    if 'age' in df.columns:
        feature_columns.append('age')
    if 'priors_count' in df.columns:
        feature_columns.append('priors_count')
    if 'decile_score' in df.columns:
        feature_columns.append('decile_score')
    if 'two_year_recid' in df.columns:
        label_column = 'two_year_recid'
    if not feature_columns:
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        feature_columns = list(numeric_cols[:5])
    if not label_column:
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        label_column = numeric_cols[-1]
    analysis_columns = feature_columns + [protected_attribute, label_column]
    analysis_df = df[analysis_columns].copy()
    analysis_df = analysis_df.dropna()
    if analysis_df[protected_attribute].dtype == 'object':
        unique_values = analysis_df[protected_attribute].unique()
        mapping = {val: idx for idx, val in enumerate(unique_values)}
        analysis_df[protected_attribute] = analysis_df[protected_attribute].map(mapping)
        print(f"Mapping for {protected_attribute}: {mapping}")
    if analysis_df[label_column].dtype != 'int64':
        analysis_df[label_column] = (analysis_df[label_column] > analysis_df[label_column].median()).astype(int)
    print(f"\nAnalysis dataset shape: {analysis_df.shape}")
    return analysis_df, feature_columns, protected_attribute, label_column

def create_standard_dataset(df, feature_columns, protected_attribute, label_column, priv_code, unpriv_code):
    print(f"\nCreating AI Fairness 360 dataset for {protected_attribute}...")
    privileged_groups = [{protected_attribute: priv_code}]
    unprivileged_groups = [{protected_attribute: unpriv_code}]
    dataset = StandardDataset(
        df=df,
        label_name=label_column,
        favorable_classes=[0],
        protected_attribute_names=[protected_attribute],
        privileged_classes=[[priv_code]],
        features_to_drop=[]
    )
    return dataset, privileged_groups, unprivileged_groups

def analyze_bias(dataset, privileged_groups, unprivileged_groups):
    print("\nAnalyzing bias...")
    train, test = dataset.split([0.8], shuffle=True, seed=42)
    metric = ClassificationMetric(
        test, test,
        unprivileged_groups=unprivileged_groups,
        privileged_groups=privileged_groups
    )
    metrics = {
        'Statistical Parity Difference': metric.statistical_parity_difference(),
        'Equal Opportunity Difference': metric.equal_opportunity_difference(),
        'Average Odds Difference': metric.average_odds_difference(),
        'Disparate Impact': metric.disparate_impact(),
        'False Positive Rate Difference': metric.false_positive_rate_difference(),
        'False Negative Rate Difference': metric.false_negative_rate_difference()
    }
    print("\nBias Metrics:")
    for metric_name, value in metrics.items():
        print(f"{metric_name}: {value:.4f}")
    return metrics, test

def create_visualizations(df, protected_attribute, label_column, metrics, suffix):
    print(f"\nCreating visualizations for {protected_attribute}...")
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle(f'COMPAS Bias Analysis: {protected_attribute}', fontsize=16, fontweight='bold')
    ax1 = axes[0]
    df[protected_attribute].value_counts().plot(kind='bar', ax=ax1)
    ax1.set_title(f'Distribution of {protected_attribute}')
    ax1.set_xlabel(protected_attribute)
    ax1.set_ylabel('Count')
    ax2 = axes[1]
    metric_names = list(metrics.keys())
    metric_values = list(metrics.values())
    colors = ['red' if abs(v) > 0.1 else 'green' for v in metric_values]
    ax2.barh(metric_names, metric_values, color=colors)
    ax2.set_title('Bias Metrics')
    ax2.axvline(x=0, color='black', linestyle='-', alpha=0.3)
    ax2.axvline(x=0.1, color='orange', linestyle='--', alpha=0.5)
    ax2.axvline(x=-0.1, color='orange', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(f'compas_bias_analysis_{suffix}.png', dpi=300, bbox_inches='tight')
    plt.show()
    print(f"Visualizations saved as 'compas_bias_analysis_{suffix}.png'")

def main():
    print("=== COMPAS Dataset Bias Analysis ===\n")
    df = load_and_explore_data()
    # --- RACE ANALYSIS ---
    analysis_df, feature_columns, protected_attribute, label_column = prepare_data_for_analysis(df, 'race')
    # Mapping for race: {'Other': 0, 'African-American': 1, 'Caucasian': 2, 'Hispanic': 3, 'Native American': 4, 'Asian': 5}
    priv_code, unpriv_code = 2, 1  # Caucasian, African-American
    dataset, priv_groups, unpriv_groups = create_standard_dataset(
        analysis_df, feature_columns, protected_attribute, label_column, priv_code, unpriv_code)
    metrics, test_dataset = analyze_bias(dataset, priv_groups, unpriv_groups)
    create_visualizations(analysis_df, protected_attribute, label_column, metrics, 'race')
    # --- SEX ANALYSIS ---
    analysis_df, feature_columns, protected_attribute, label_column = prepare_data_for_analysis(df, 'sex')
    # Mapping for sex: {'Male': 0, 'Female': 1}
    priv_code, unpriv_code = 0, 1  # Male, Female
    dataset, priv_groups, unpriv_groups = create_standard_dataset(
        analysis_df, feature_columns, protected_attribute, label_column, priv_code, unpriv_code)
    metrics, test_dataset = analyze_bias(dataset, priv_groups, unpriv_groups)
    create_visualizations(analysis_df, protected_attribute, label_column, metrics, 'sex')
    print("\n=== Analysis Complete ===")
    print("Check 'compas_bias_analysis_race.png' and 'compas_bias_analysis_sex.png' for visualizations.")

if __name__ == "__main__":
    main() 