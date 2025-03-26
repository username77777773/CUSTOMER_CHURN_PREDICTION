import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_plots(filepath, output_folder):
    df = pd.read_csv(filepath)
    
    # Visualization 1: Churn Count
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x="Churn", palette="coolwarm")
    plt.title("Customer Churn Distribution")
    plt.savefig(os.path.join(output_folder, "churn_distribution.png"))
    
    # Visualization 2: Monthly Charges vs Total Charges
    plt.figure(figsize=(6, 4))
    sns.scatterplot(data=df, x="MonthlyCharges", y="TotalCharges", hue="Churn")
    plt.title("Monthly Charges vs Total Charges")
    plt.savefig(os.path.join(output_folder, "charges_correlation.png"))
    
    plt.close("all")  # Close plots to avoid memory issues
