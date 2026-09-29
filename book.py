import numpy as np
import pandas as pd

file_path = "goodreads_library_export.csv"

books = pd.read_csv(file_path)

def get_titles(books):
    titles = books['Title']
    return titles

titles = get_titles(books)

