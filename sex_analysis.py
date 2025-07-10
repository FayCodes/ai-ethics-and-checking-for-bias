import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from aif360.datasets import StandardDataset
from aif360.metrics import ClassificationMetric
import warnings
warnings.filterwarnings('ignore')

plt.style.use('default')
plt.rcParams['figure.figsize'] = (12, 8)

def analyze_sex_bias():
    print("=== COMPAS Sex Bias Analysis ===\n")
    
    # Load data
    df = pd.read_csv('compas-scores-two-years.csv')
    
    # Prepare data for sex analysis
    feature_columns = ['age', 'priors_count', 'decile_score']
    protected_attribute = 'sex'
    label_column = 'two_year_recid'
    
    analysis_columns = feature_columns + [protected_attribute, label_column]
    analysis_df = df[analysis_columns].copy()
    analysis_df = analysis_df.dropna()
    
    # Convert sex to numeric
    sex_mapping = {'Male': 0, 'Female': 1}
    analysis_df[protected_attribute] = analysis_df[protected_attribute].map(sex_mapping)
    print(f"Sex mapping: {sex_mapping}")
    print(f"Analysis dataset shape: {analysis_df.shape}")
    
    # Create dataset (Male=privileged, Female=unprivileged)
    privileged_groups = [{'sex': 0}]  # Male
    unprivileged_groups = [{'sex': 1}]  # Female
    
    dataset = StandardDataset(
        df=analysis_df,
        label_name=label_column,
        favorable_classes=[0],
        protected_attribute_names=[protected_attribute],
        privileged_classes=[[0]],  # Male is privileged
        features_to_drop=[]
    )
    
    # Analyze bias
    print("\nAnalyzing sex bias...")
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
    
    print("\nSex Bias Metrics:")
    for metric_name, value in metrics.items():
        print(f"{metric_name}: {value:.4f}")
    
    # Create visualization
    print("\nCreating sex bias visualization...")
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('COMPAS Bias Analysis: Sex', fontsize=16, fontweight='bold')
    
    # Distribution of sex
    ax1 = axes[0]
    analysis_df[protected_attribute].value_counts().plot(kind='bar', ax=ax1)
    ax1.set_title('Distribution of Sex')
    ax1.set_xlabel('Sex (0=Male, 1=Female)')
    ax1.set_ylabel('Count')
    
    # Bias metrics
    ax2 = axes[1]
    metric_names = list(metrics.keys())
    metric_values = list(metrics.values())
    colors = ['red' if abs(v) > 0.1 else 'green' for v in metric_values]
    ax2.barh(metric_names, metric_values, color=colors)
    ax2.set_title('Sex Bias Metrics')
    ax2.axvline(x=0, color='black', linestyle='-', alpha=0.3)
    ax2.axvline(x=0.1, color='orange', linestyle='--', alpha=0.5)
    ax2.axvline(x=-0.1, color='orange', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('compas_bias_analysis_sex.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Sex bias visualization saved as 'compas_bias_analysis_sex.png'")
    
    return metrics

if __name__ == "__main__":
    analyze_sex_bias() 