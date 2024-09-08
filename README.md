# Business Problem: Customer Conversion Prediction
## Developing a Predictive Model for Customer Conversion

### Understanding the Problem
The goal is to create a model that can accurately predict which customers are most likely to convert after engaging with digital marketing campaigns. This model can help businesses optimize their marketing efforts by:

* **Targeted Advertising:** Identifying customers with a high probability of conversion allows for more efficient allocation of advertising budgets.
* **Personalized Campaigns:** Tailoring marketing messages to the specific needs and preferences of potential customers can improve conversion rates.
* **Customer Segmentation:** Grouping customers based on their likelihood of conversion can inform more effective marketing strategies.
* **Campaign Evaluation:** Assessing the performance of different marketing campaigns can help businesses identify what works and what doesn't.

## Exploratory Data Analysis (EDA):
![image](https://github.com/user-attachments/assets/4ebbcb1c-2123-4693-901d-916c671573e7)
![image](https://github.com/user-attachments/assets/4549d64b-2795-4675-a58a-daca395c6cfd)

![image](https://github.com/user-attachments/assets/0b158e10-f1d2-4a16-8aff-df3780cc7645)

## Insights from the Correlation Matrix

**Strong Positive Correlations with Conversion:**

* **AdSpend:** There is a strong positive correlation between AdSpend and Conversion, suggesting that increased advertising expenditure is associated with higher conversion rates.
* **Click-Through Rate (CTR):** A moderately strong positive correlation exists between CTR and Conversion, indicating that a higher click-through rate is linked to a higher likelihood of conversion.
* **Website Visits:** There is a moderately strong positive correlation between Website Visits and Conversion, suggesting that more website visits are associated with higher conversion rates.
* **Pages Per Visit:** A moderately strong positive correlation between Pages Per Visit and Conversion indicates that visitors who explore more pages are more likely to convert.
* **TimeOnSite:** A moderately strong positive correlation between TimeOnSite and Conversion suggests that visitors who spend more time on the website are more likely to convert.

**Strong Negative Correlations with Conversion:**

* **PreviousPurchases:** A moderately strong negative correlation between PreviousPurchases and Conversion suggests that customers who have made previous purchases may be less likely to convert again, possibly due to factors like customer satisfaction or product life cycle.

**Other Notable Correlations:**

* **Age, Income, and Conversion:** There is a weak positive correlation between Age and Conversion, while the correlation between Income and Conversion is negligible. This suggests that age may have a slight influence on conversion, but income does not seem to be a significant factor.
* **LoyaltyPoints and Conversion:** The correlation between LoyaltyPoints and Conversion is negligible, indicating that loyalty points do not have a strong impact on conversion rates.

**Overall:**

* The analysis suggests that factors related to advertising, website engagement, and customer behavior (such as time spent on site and pages visited) are more strongly correlated with conversion than demographic factors like age and income.
* Identifying and addressing the factors that influence conversion can help optimize marketing strategies and improve overall business performance.

#### Model Training and Data Splitting

A crucial step after data preparation is model training. This involves splitting the data into training and test sets. This division allows for evaluating the model's performance on unseen data during training, helping to avoid overfitting and assess the model's generalization capability.

| Model                       | Training Accuracy | Testing Accuracy |
|-----------------------------|-------------------|------------------|
| GaussianNB                  | 0.88109375        | 0.87875          |
| DecisionTreeClassifier      | 1.0               | 0.836875         |
| RandomForestClassifier      | 1.0               | 0.888125         |
| LogisticRegression          | 0.8765625         | 0.876875         |
| AdaBoostClassifier          | 0.9159375         | 0.90625          |
| KNeighborsClassifier        | 0.87765625        | 0.87625          |
| GradientBoostingClassifier  | 0.94328125        | 0.91             |

 ## ROC Curve Models
 ![image](https://github.com/user-attachments/assets/d7242648-71a1-4d3a-ba78-479e8fa443c7)


The provided ROC curve plot compares the performance of seven different classification models: GaussianNB, DecisionTreeClassifier, RandomForestClassifier, LogisticRegression, AdaBoostClassifier, KNeighborsClassifier, and GradientBoostingClassifier. 

Here are some insights from the graph:

**Model Performance:**

- **GradientBoostingClassifier** and **RandomForestClassifier** exhibit the best overall performance, with AUC scores of 0.82 and 0.81, respectively. This indicates that these models are able to discriminate between positive and negative classes effectively.
- **KNeighborsClassifier** has the worst performance with an AUC score of 0.55, suggesting it struggles to distinguish between the classes.
- **LogisticRegression** and **GaussianNB** have moderate performance, with AUC scores around 0.70.

**AUC Scores:**

- The AUC score represents the area under the ROC curve. A higher AUC score indicates better model performance.
- A perfect model would have an AUC score of 1.0, while a random model would have an AUC score of 0.5.

**Trade-offs:**

- The ROC curve shows the trade-off between sensitivity (true positive rate) and specificity (true negative rate) at different classification thresholds.
- A model that is more sensitive will correctly classify more positive instances but may also misclassify more negative instances (higher false positive rate).
- A model that is more specific will correctly classify more negative instances but may also misclassify more positive instances (higher false negative rate).

**Model Selection:**

- GradientBoostingClassifier or RandomForestClassifier might be good choices.


Based on the provided metrics, **Model 3: RandomForestClassifier** appears to be the best-performing model. Here's why:

- **F1 Score**: 0.9391 (highest among the models)
- **Recall**: 0.9957 (very close to the highest recall of 0.9986 from Model 1)
- **Precision**: 0.8886 (higher than Model 1 and comparable to others)

The confusion matrix for Model 3 also shows a good balance between true positives and false positives/negatives:

![image](https://github.com/user-attachments/assets/695ae24d-09a4-4dd7-862f-27782fa1712d)



- True Positives: 1396
- False Positives: 175
- True Negatives: 23
- False Negatives: 6

Overall, Model 3 provides a strong balance of precision and recall, making it the most reliable choice for your needs.
