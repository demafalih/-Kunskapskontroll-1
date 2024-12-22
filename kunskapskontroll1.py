#flödet
import pandas as pd
import sqlite3

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def filter_horsepower(df):
    filtered_df = df[df['horsepower']> 190]
    return filtered_df

def save_to_database(df, db_path):
    con = sqlite3.connect(db_path)
    df.to_sql('AutomobileHorsepower', con, if_exists='replace', index=False)
    con.close()

#test
def compare_origin_hp(df):
    if 'horsepower' not in df.columns or 'origin' not in df.columns:
        raise ValueError("Dataframe does not contain 'horsepower' / 'origin'.")
    mean_horsepower = df.groupby('origin')['horsepower'].mean()
    
    if 'usa' in mean_horsepower.index and 'european' in mean_horsepower.index:
        if mean_horsepower['usa'] > mean_horsepower['european']:
            return "Cars of origin USA have a higher average horsepower."
        elif mean_horsepower['usa'] < mean_horsepower['european']:
            return "Cars of origin European have a higher average horsepower."
        else: 
            return "Cars of origin 'USA' and 'European' have the same average horsepower."
    else:
        raise ValueError("Error in origin data. 'USA' or 'European' not found")
