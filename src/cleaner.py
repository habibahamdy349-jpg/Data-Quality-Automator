import pandas as pd
import matplotlib.pyplot as plt

def automate_data_cleaning(file_path):
    print("🔄 Loading raw dataset...")
    df = pd.read_csv(file_path)
    
    initial_rows = len(df)
    
    # 1. Remove duplicate rows
    df.drop_duplicates(inplace=True)
    duplicates_removed = initial_rows - len(df)
    
    # 2. Handle missing values (fill numerical with 0, text with 'Unknown')
    missing_count = df.isnull().sum().sum()
    df.fillna({'amount': 0, 'status': 'Unknown', 'category': 'General'}, inplace=True)
    df.fillna(method='ffill', inplace=True)
    
    # 3. Standardize text columns (strip spaces & title case)
    text_cols = ['customer_name', 'status', 'category']
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title()
            
    print(f"✅ Cleaning complete! Removed {duplicates_removed} duplicates and handled {missing_count} missing values.")
    
    # Save cleaned output
    output_file = "data/cleaned_output_data.csv"
    df.to_csv(output_file, index=False)
    print(f"📁 Cleaned data saved successfully to {output_file}")
    
    return df, duplicates_removed, missing_count

if __name__ == "__main__":
    # Test with sample data
    automate_data_cleaning("data/sample_raw_data.csv")
