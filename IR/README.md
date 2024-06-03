# Information Retrieval Project

## Overview

This project focuses on preprocessing textual data for an information retrieval system. The preprocessing operations are designed to clean and standardize the text, making it easier for retrieval, especially when working with datasets that have a large number of records.
- The project consists of two main projects:
  - ir-front: React.js frontend project (simple interface for search)
  - IR: a DJANGO backend application to handle search requests through an API
  - Offline: a component related to corpus data preprocessing, matching, ranking, evaluation, ...

## Offline Architecture

It is comprised of 3 main packages:
1- Helper: static functions that aid in data (retrieval, fetching, ...) from SQLite database
2- Manual: scripts to process data (import to database, multiprocessing support, preprocessing functions tests to find most efficient packages and tools)
3- Pipeline: full IR system (indexing, preprocessing, matching and ranking, evaluation) in addition to package for Crawling and index Clustering 

## Pipeline Components

1- Index Package: Custom Wrapper class for tfidfvectorizer with suitable index related operations (load, create, search, initialize query)
2- Matching and Ranking Package: functions to find similarities between two different vectors, get top documents from Corpus based on a similarity threshold
3- Evaluation Package: functions to create run files, evaluate run files based on predefined qrels files
4- Preprocessor Package

## Preprocessing Operations

- **Clean HTML**: Removes HTML tags from the text.
- **Replace Countries**: NER operation to replace country names with their standardized names.
- **Replace Dates**: NER operation to normalizes date formats.
- **Numerize Text**: NER operation to converts numbers in text to their numeric form.
- **Lower**: Converts all text to lowercase.
- **Remove Stopwords**: Removes common stopwords from the text.
- **Replace Ordinal Numbers**: Converts ordinal numbers to their textual form.
- **Remove Punctuation**: Removes punctuation from the text.
- **Remove Long Words**: Removes words longer than a specified length.
- **Stem**: Reduces words to their root form.
- **Remove Empty Tokens**: Removes empty tokens from the text.


## Additional Features

### Clustering

This project includes methods to find the optimal number of clusters and visualize the clustered data using PCA (Principal Component Analysis). 

### Crawler

The crawler component of the project uses Scrapy and Scrapy-Redis to collect text data from websites. The crawler is designed to handle failures couple of failures and extract meaningful text data from the crawled pages.
We used Redis in order to implement distributed crawling from different nodes at the same time where Redis can synchronize the different nodes

## Prerequisites

Before you begin, ensure you have met the following requirements:
- **Python**: Make sure Python is installed on your system. You can download it from the [official website](https://www.python.org/downloads/).
- **Dataset**: Ensure you have an SQLite database that contains a corpus. 


## Installation

To install the necessary dependencies for this project, you need to install the packages listed in `requirements.txt`. Follow these steps:

1. Navigate to the project directory:

    ```sh
    cd IR
    ```

2. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Before running the project, you need to configure the `.env.example` file to fit your specific needs. Copy the `.env.example` file and rename it to `.env`. Then, modify the variables according to your requirements.

### Example Configuration

```dotenv
# .env

# Database Configuration
dataset="example.db"

# Paths for Created Model, Index, and Keys (Generated After the Indexing Process)
saved_model_name="Pipeline/index/Saved/example_model.pickle"
saved_tfidf_name="Pipeline/index/Saved/example_tfidf.pickle"
saved_keys_name="Pipeline/index/Saved/example_keys.pickle"

# Paths for Qrels, Queries, and Run File (Used in the Evaluation Process)
qrels_path="Pipeline/Evaluation/Example/qrels"
queries_path="Pipeline/Evaluation/Example/queries.csv"
run_path="Pipeline/Evaluation/Example/processed_dataset"

# Processing Configuration Based on Your Machine's Capabilities
ncores=1
nprocesses=1
ntasks=1

# Configuration for the Corpus Table in the Database and the New Table Name that the Preprocessed Data Will Be Saved inside
model='Corpus'
new_model='org_Processed_Corpus'
threshold=0.0
```
## Running The Project

To preprocess the data, navigate to the `preprocessor` folder and run the `process_records.py` script in order to insert the processed data into a new table in the same dataset database.
To create indexes, load indexes, evaluate, create clusters, search for a specific term please refer to `main.ipynb` and run the desired cells. 
