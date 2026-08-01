import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

try: df = pd.read_csv('imdb_top_100_movies.csv')
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_100_movies.csv' was not found.")
    exit()

genres =  sorted({g.strip() for xs in df ['Genre'].dropna().str.split(",") for g in xs})

def dots():
    for _ in range(3): print(Fore.YELLOW + ".", end="", flush=True); time.sleep(0.5)

def senti(p): return "Positive" if p > 0 else "Negative" if p < 0 else "Neutral"

def recommend_movies(genre= None, sentiment= None, ):
