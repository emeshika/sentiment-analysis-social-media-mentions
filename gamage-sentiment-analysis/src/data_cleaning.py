import pandas as pd
import re

def clean_text(text):
    text = text.lower() # Normalize text 
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE) # Remove URLs 
    text = re.sub(r'[^\w\s]', '', text) # Remove special characters 
    return text

def process_data(input_file):
    df = pd.read_csv(input_file)
    df['cleaned_text'] = df['review_text'].apply(clean_text)
    df.to_csv('data/cleaned_reviews.csv', index=False)
    print("Step 4 Complete: Data cleaned and saved.")

if __name__ == "__main__":
    process_data('data/raw_reviews.csv')