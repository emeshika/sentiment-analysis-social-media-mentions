import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiments():
    # Load cleaned data 
    df = pd.read_csv('data/cleaned_reviews.csv')
    analyzer = SentimentIntensityAnalyzer()
    
    # Apply analysis 
    df['compound_score'] = df['cleaned_text'].apply(lambda x: analyzer.polarity_scores(str(x))['compound'])
    
    # Create sentiment classification column 
    df['sentiment'] = df['compound_score'].apply(
        lambda x: 'Positive' if x >= 0.05 else ('Negative' if x <= -0.05 else 'Neutral')
    )
    
    # Save results 
    df.to_csv('data/sentiment_results.csv', index=False)
    print("Step 5 & 6 Complete: Sentiment scores aggregated.")

if __name__ == "__main__":
    analyze_sentiments()