
import os
import pandas as pd
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

print(Fore.YELLOW + "Running topic_cluster_formation.py")
# Read the CSV file
news_data = pd.read_csv(r'dataset\raw\news_with_full_content_with_topic_3.csv')

# Get a list of all unique topics
topics = news_data['topic'].unique()

# Function to create separate CSV files for each topic
def create_topic_csv(topic_name, data):
    topic_rows = data[data['topic'] == topic_name].dropna()  # Drop rows with missing values
    if not topic_rows.empty:
        folder_name = r'dataset/topics'
        os.makedirs(folder_name, exist_ok=True)  # Create directory if it doesn't exist
        filename = f'{topic_name}.csv'
        file_path = os.path.join(folder_name, filename)
        topic_rows.to_csv(file_path, index=False)

# Iterate through the topics and create separate CSV files
for topic in topics:
    create_topic_csv(topic, news_data)

print(Fore.GREEN + "\nTopic clusters have been created, check dataset/topics")