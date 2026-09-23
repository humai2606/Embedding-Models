# Embedding Models

## Overview

This project demonstrates how embedding models convert text into numerical vectors and how cosine similarity can be used to compare the meaning of sentences.

## Models Used

| Model                  | Embedding Dimensions |
| ---------------------- | -------------------: |
| all-MiniLM-L6-v2       |                  384 |
| BAAI/bge-large-en-v1.5 |                 1024 |
| BAAI/bge-base-en-v1.5  |                  768 |

## Example Sentences

The project uses the following sentences:

```text
I enjoy coding.
I like programming.
The weather is very hot.
```

The embeddings are generated for each sentence, and the embedding dimensions are displayed.

## Cosine Similarity

Cosine similarity is used to measure the similarity between two sentence embeddings.

The project compares:

```text
"I enjoy coding."
"I like programming."
```

Since these sentences have similar meanings, their similarity score is expected to be relatively high.

## Technologies Used

* Python
* Sentence Transformers
* Scikit-learn

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Requirements

```text
sentence-transformers
scikit-learn
```

## Run the Project

```bash
python embedding.py
```

## Project Structure

```text
Embedding-Models/
│
├── embedding.py
├── requirements.txt
└── README.md
```

## Applications

Embedding models can be used for:

* Semantic Search
* RAG
* Document Similarity
* Question Matching
* Recommendation Systems
* Clustering

## Conclusion

This project demonstrates text embedding generation using three different embedding models and compares their embedding dimensions and sentence similarity using cosine similarity.
