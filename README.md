# Customer Conversion Prediction Project

## Project Overview

This project develops a predictive machine learning model to forecast customer conversion rates for digital marketing campaigns. By leveraging advanced data analysis and machine learning techniques, the project aims to help businesses optimize their marketing strategies and improve conversion efficiency.

## Business Problem

The primary goal is to create a model that can accurately predict which customers are most likely to convert after engaging with digital marketing campaigns. This enables businesses to:

- Implement targeted advertising
- Design personalized marketing campaigns
- Segment customers effectively
- Evaluate marketing campaign performance

## Key Insights

### Correlation Analysis

#### Factors Positively Correlated with Conversion
- Ad Spend
- Click-Through Rate (CTR)
- Website Visits
- Pages Per Visit
- Time on Site

#### Factors with Weak or Negligible Correlation
- Previous Purchases
- Age
- Income
- Loyalty Points

## Model Performance

### Model Comparison

We evaluated seven different machine learning models:

| Model | Training Accuracy | Testing Accuracy |
|-------|-------------------|------------------|
| GaussianNB | 0.88109 | 0.87875 |
| DecisionTreeClassifier | 1.0 | 0.83688 |
| RandomForestClassifier | 1.0 | 0.88813 |
| LogisticRegression | 0.87656 | 0.87688 |
| AdaBoostClassifier | 0.91594 | 0.90625 |
| KNeighborsClassifier | 0.87766 | 0.87625 |
| GradientBoostingClassifier | 0.94328 | 0.91000 |

### Recommended Model: RandomForestClassifier

**Performance Metrics:**
- F1 Score: 0.9391
- Recall: 0.9957
- Precision: 0.8886

### Confusion Matrix Breakdown
- True Positives: 1,396
- False Positives: 175
- True Negatives: 23
- False Negatives: 6

## Key Visualizations

The project includes several key visualizations:
- Correlation Matrix
- ROC Curve Comparing Model Performances
- Confusion Matrix for Best-Performing Model

## Recommendations

1. Use the RandomForestClassifier for predicting customer conversions
2. Focus marketing efforts on:
   - Increasing website engagement
   - Optimizing ad spend
   - Improving click-through rates
3. Develop personalized strategies based on website interaction metrics

## Future Work

- Continuously retrain the model with new data
- Explore additional features that might improve prediction accuracy
- Implement A/B testing of marketing strategies based on model insights

## Technologies Used

- Python
- Scikit-learn
- Pandas
- Matplotlib
- Machine Learning Algorithms

## Getting Started

1. Clone the repository
2. Install required dependencies
3. Run the Jupyter notebook for detailed analysis
4. Use the trained RandomForestClassifier for predictions
