# Information Retrieval Project

## Overview

This project focuses on preprocessing textual data for an information retrieval system. The preprocessing operations are designed to clean and standardize the text, making it easier for retrieval, especially when working with datasets that have a large number of records.

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

## Prerequisites

Before you begin, ensure you have met the following requirements:
- **Python**: Make sure Python is installed on your system. You can download it from the [official website](https://www.python.org/downloads/).
- **Dataset**: Ensure you have an SQLite database that contains a corpus. 


## Installation

To install the necessary dependencies for this project, you need to install the packages listed in `requirements.txt`. Follow these steps:

1. Clone the repository:

    ```sh
    git clone 
    ```

2. Navigate to the project directory:

    ```sh
    cd IR
    ```

3. Install the dependencies:

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

To preprocess the data, navigate to the `preprocessor` folder and run the `preprocessor.py` file.

To evaluate and create clusters, run `main.py` located in the root directory.
