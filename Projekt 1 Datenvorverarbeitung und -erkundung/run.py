import pandas as pd
from netflix_data_reader import NetflixReader

netflix_reader = NetflixReader()

raw_data = netflix_reader.read_netflix_data('netflix_data.csv')
netflix_reader.preprocess()
print(raw_data)