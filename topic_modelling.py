
import os

import pandas as pd
from colorama import Fore, init
from tqdm import tqdm
from transformers import (AutoModelForSeq2SeqLM, AutoTokenizer,
                          T5ForConditionalGeneration)

# Initialize colorama
init(autoreset=True)

print(Fore.YELLOW + "Running topic_modelling.py")

# Load the tokenizer and model
print('Loading tokenizer')
tokenizer = AutoTokenizer.from_pretrained('cache_dir/transformers/mrm8488/t5-base-finetuned-news-title-classification')
print('Loading model')
model = T5ForConditionalGeneration.from_pretrained('cache_dir/transformers/mrm8488/t5-base-finetuned-news-title-classification')
print('Model and Tokenizer loaded')

def topic(text):
    input_ids = tokenizer.encode(text, return_tensors='pt')
    outputs = model.generate(input_ids=input_ids, max_new_tokens=512)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


input_file_path = r'dataset/raw/news_with_full_content_2.csv'
output_file_path = r'dataset/raw/news_with_full_content_with_topic_3.csv'

# read the input CSV file into a pandas data frame
df = pd.read_csv(input_file_path)

# add a new column for the article topic
df['topic'] = ''

for idx, row in tqdm(df.iterrows(), total=len(df), desc="Fetching article topic"):
    text = row['Title']
    topic_title = topic(text)
    df.loc[idx, 'topic'] = topic_title

# write the updated data frame to a new CSV file without row indices
df.to_csv(output_file_path, index=False)

print(Fore.GREEN + "\nAll topics have been generated, check dataset/raw/news_with_full_content_with_topic_3.csv")
