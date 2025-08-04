import pandas as pd
import numpy as np

class read_csv:
    df = pd.read_csv('tweets_dataset.csv')
    df.head()
class analysis:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    def How_many_tweets_are_there_from_each_category(df: pd.DataFrame):
        return df['Biased'].value_counts()  #1 כמה ציוצים יש מכל קטגוריה

    def What_is_the_average_length_in_words_of_tweets_by_category_and_total(df: pd.DataFrame):
        df['word_counts'] = df['Text'].map(lambda x: len(x.split()))
        return df.groupby(['Biased'])['word_counts'].mean() #2 ממוצע כמות מילים בציוצים לפי קטגוריה

    def What_are_the_3_tweets_with_the_largest_amount_of_text_by_category(df: pd.DataFrame):
        df['text_length'] = df['Text'].map(lambda x: len(x.split()))
        return df.loc[df.groupby(['Biased'])['text_length'].nlargest(3).reset_index()['level_1']].sort_values(by='Biased')  #3 ציוצים עם כמות טקסט הכי גדולה בכל קטגוריה

    def What_are_the_10_most_common_words_in_all_tweets_from_all_categories(df: pd.DataFrame):
        Ten_common_words = pd.Series(' '.join(df['Text']).lower().split()).value_counts()[:10]
        return Ten_common_words  #4 10 מילים הכי נפוצות בכל הציוצים

    def How_many_words_in_capital_letters_by_category_and_total(df: pd.DataFrame):
        df['capital_words'] = df['Text'].apply(lambda x: sum(1 for word in x.split() if word.isupper()))
        df.groupby(['Biased'])['capital_words'].sum(), df['capital_words'].sum()# 5 כמה מילים באותיות גדולות בכל ציוץ לפי קטגוריה
