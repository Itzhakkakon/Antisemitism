import pandas as pd
from analysis import read_csv

a = read_csv('cleaned_data.csv')

# def Saving_the_relevant_columns_from_the_data_file(df):
#     for column in df.columns:
#         if column not in ['Text', 'Biased']:
#             return df.drop()
#         return

def delete_columns(df, columns_to_delete):
    columns_data = df.cpy()
    columns_data = columns_data.drop(columns=columns_to_delete, errors='ignore')
    return columns_data# הסרת עמודות לא רלוונטיות

def delete_unclassified(data, column_to_delete):
    delete_data = data.copy()
    delete_data = delete_data.dropna(subset=[column_to_delete])
    return delete_data #הסרת ציוצים ללא סיווג

def clean_Punctuation_marks(df, column_name):
    df[column_name] = df[column_name].str.replace(r'[^\w\s]', '', regex=True)
    return df #הסרת סימני פיסוק

def Convert_to_lowercase(df):
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    return df #המרה לאותיות קטנות
