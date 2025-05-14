# Digital Marketing Conversion Predictor

This project develops a machine learning model to predict customer conversion likelihood in digital marketing campaigns. It includes a Jupyter Notebook for data analysis and model training, along with a Gradio-based web application for interactive predictions.

## Project Overview

The goal is to predict which customers are likely to convert based on demographic, campaign, and engagement data. The model helps optimize marketing strategies by:
- Identifying high-potential customers for targeted advertising
- Enabling personalized campaign design
- Supporting customer segmentation
- Evaluating campaign performance

The dataset, provided by Rabie El Kharoua under CC BY 4.0, includes features like age, income, ad spend, click-through rate, and more, with a binary conversion target.

## Repository Structure

- **`Predict_Conversion_in_Digital_Marketing.ipynb`**: Jupyter Notebook containing:
  - Exploratory Data Analysis (EDA)
  - Model training and evaluation using multiple algorithms (Random Forest, Gradient Boosting, etc.)
  - Model saving (`rf_model.pkl` for Random Forest)
- **`app.py`**: Python script for the Gradio web application, allowing users to input customer and campaign data to predict conversion probability.
- **`rf_model.pkl`**: Pre-trained Random Forest model (second-best performer).
- **`README.md`**: This file, providing project overview and instructions.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/digital-marketing-conversion-predictor.git
   cd digital-marketing-conversion-predictor
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Ensure you have Python 3.8+ installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is not provided, install the following:
   ```bash
   pip install gradio pandas numpy joblib scikit-learn matplotlib seaborn
   ```

4. **Download the Dataset**:
   Place the `digital_marketing_campaign_dataset.csv` file in the project directory. The dataset is available from the original source (cite Rabie El Kharoua, CC BY 4.0).

## Usage

### Running the Jupyter Notebook
1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Open `Predict_Conversion_in_Digital_Marketing.ipynb` and run the cells to:
   - Perform EDA
   - Train and evaluate models
   - Save the trained models (`rf_model.pkl` and `gb_model.pkl`)

### Running the Gradio Web App
1. Ensure `rf_model.pkl` is in the project directory.
2. Run the Gradio app:
   ```bash
   python app.py
   ```
3. Open the provided URL (e.g., `http://127.0.0.1:7860`) in your browser.
4. Input customer and campaign details via sliders and radio buttons to get conversion predictions.

## Model Details

- **Data Preprocessing**:
  - Categorical variables (Gender, CampaignType, CampaignChannel) are one-hot encoded.
  - Numerical features are used as-is.
- **Model Selection**:
  - Multiple models were evaluated (Decision Tree, Random Forest, Gradient Boosting, etc.).
  - Gradient Boosting performed best (F1 Score: 0.951), but Random Forest was chosen for the app due to its balance of performance and speed.
- **Features Used**:
  - Demographic: Age, Income, Gender
  - Campaign: AdSpend, CampaignType, CampaignChannel
  - Engagement: ClickThroughRate, ConversionRate, WebsiteVisits, PagesPerVisit, TimeOnSite, SocialShares, EmailOpens, EmailClicks
  - Historical: PreviousPurchases, LoyaltyPoints

## Results

The Random Forest model (`rf_model.pkl`) provides reliable predictions with:
- High precision and recall for identifying converters
- Probability outputs for nuanced decision-making

The Gradio app offers an intuitive interface for real-time predictions, displaying whether a customer will convert and the associated probability.

## Dataset Attribution

The dataset is provided by Rabie El Kharoua under the CC BY 4.0 license. Please cite the author when using the dataset. Duplication within Kaggle is not permitted.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. The dataset is under CC BY 4.0, requiring attribution to Rabie El Kharoua.

## Contact

For questions or feedback, please open an issue on GitHub or contact [ahmedalhofy42@gmail.com].
