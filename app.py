import gradio as gr
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import OneHotEncoder

# Load the pre-trained model
model = joblib.load("rf_model.pkl")

# Define feature names based on the training data
feature_names = [
    'Age', 'Income', 'AdSpend', 'ClickThroughRate', 'ConversionRate',
    'WebsiteVisits', 'PagesPerVisit', 'TimeOnSite', 'SocialShares',
    'EmailOpens', 'EmailClicks', 'PreviousPurchases', 'LoyaltyPoints',
    'Gender_Male', 'CampaignType_Consideration', 'CampaignType_Conversion',
    'CampaignType_Retention', 'CampaignChannel_PPC', 'CampaignChannel_Referral',
    'CampaignChannel_SEO', 'CampaignChannel_Social Media'
]

def predict_conversion(
    age, income, ad_spend, click_through_rate, conversion_rate,
    website_visits, pages_per_visit, time_on_site, social_shares,
    email_opens, email_clicks, previous_purchases, loyalty_points,
    gender, campaign_type, campaign_channel
):
    # Create a dataframe with all the input features
    input_data = pd.DataFrame({
        'Age': [age],
        'Income': [income],
        'AdSpend': [ad_spend],
        'ClickThroughRate': [click_through_rate],
        'ConversionRate': [conversion_rate],
        'WebsiteVisits': [website_visits],
        'PagesPerVisit': [pages_per_visit],
        'TimeOnSite': [time_on_site],
        'SocialShares': [social_shares],
        'EmailOpens': [email_opens],
        'EmailClicks': [email_clicks],
        'PreviousPurchases': [previous_purchases],
        'LoyaltyPoints': [loyalty_points]
    })
    
    # One-hot encode categorical variables
    # Gender encoding
    input_data['Gender_Male'] = 1.0 if gender == "Male" else 0.0
    
    # Campaign Type encoding
    input_data['CampaignType_Consideration'] = 1.0 if campaign_type == "Consideration" else 0.0
    input_data['CampaignType_Conversion'] = 1.0 if campaign_type == "Conversion" else 0.0
    input_data['CampaignType_Retention'] = 1.0 if campaign_type == "Retention" else 0.0
    # Note: Awareness is reference category
    
    # Campaign Channel encoding
    input_data['CampaignChannel_PPC'] = 1.0 if campaign_channel == "PPC" else 0.0
    input_data['CampaignChannel_Referral'] = 1.0 if campaign_channel == "Referral" else 0.0
    input_data['CampaignChannel_SEO'] = 1.0 if campaign_channel == "SEO" else 0.0
    input_data['CampaignChannel_Social Media'] = 1.0 if campaign_channel == "Social Media" else 0.0
    # Note: Email is reference category
    
    # Ensure all columns match the expected feature names and order
    input_array = input_data[feature_names].values
    
    # Make prediction
    probability = model.predict_proba(input_array)[0, 1]
    prediction = model.predict(input_array)[0]
    
    if prediction == 1:
        result = f"Customer will convert (Probability: {probability:.2%})"
    else:
        result = f"Customer will not convert (Probability: {(1-probability):.2%})"
    
    return result

# Create the Gradio interface
with gr.Blocks(title="Digital Marketing Conversion Predictor") as demo:
    gr.Markdown("# Digital Marketing Conversion Predictor")
    gr.Markdown("Enter customer and campaign information to predict conversion likelihood")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Customer Demographics")
            age = gr.Slider(18, 70, value=35, label="Age")
            gender = gr.Radio(["Male", "Female"], label="Gender")
            income = gr.Slider(10000, 150000, value=80000, step=1000, label="Income (USD)")
            
            gr.Markdown("### Marketing Campaign Details")
            campaign_type = gr.Radio(["Awareness", "Consideration", "Conversion", "Retention"], 
                                    label="Campaign Type")
            campaign_channel = gr.Radio(["Email", "Social Media", "SEO", "PPC", "Referral"], label="Campaign Channel")
            ad_spend = gr.Slider(100, 10000, value=2000, step=100, label="Ad Spend (USD)")
            
        with gr.Column():
            gr.Markdown("### Customer Engagement Metrics")
            click_through_rate = gr.Slider(0.01, 0.30, value=0.15, step=0.01, label="Click-Through Rate")
            conversion_rate = gr.Slider(0.01, 0.20, value=0.10, step=0.01, label="Conversion Rate")
            website_visits = gr.Slider(0, 50, value=20, step=1, label="Website Visits")
            pages_per_visit = gr.Slider(1, 10, value=5, step=0.5, label="Pages Per Visit")
            time_on_site = gr.Slider(1, 15, value=8, step=0.5, label="Time on Site (minutes)")
            
            gr.Markdown("### Customer History")
            social_shares = gr.Slider(0, 100, value=20, step=1, label="Social Shares")
            email_opens = gr.Slider(0, 20, value=10, step=1, label="Email Opens")
            email_clicks = gr.Slider(0, 10, value=5, step=1, label="Email Clicks")
            previous_purchases = gr.Slider(0, 10, value=3, step=1, label="Previous Purchases")
            loyalty_points = gr.Slider(0, 5000, value=1500, step=100, label="Loyalty Points")
    
    with gr.Row():
        predict_btn = gr.Button("Predict Conversion", variant="primary", scale=2)
        result = gr.Textbox(label="Prediction Result")
    
    predict_btn.click(
        fn=predict_conversion,
        inputs=[
            age, income, ad_spend, click_through_rate, conversion_rate,
            website_visits, pages_per_visit, time_on_site, social_shares,
            email_opens, email_clicks, previous_purchases, loyalty_points,
            gender, campaign_type, campaign_channel
        ],
        outputs=result
    )

# Launch the app
if __name__ == "__main__":
    demo.launch(share=True)