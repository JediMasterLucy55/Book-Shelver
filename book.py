import numpy as np
import pandas as pd

file_path = "goodreads_library_export.csv"

def get_books(file_path):
    df = pd.read_csv(file_path)
    return df

books = get_books(file_path)

def get_titles(books):
    

titles = get_titles(books)