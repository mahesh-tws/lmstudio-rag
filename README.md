# A simple RAG example using LM Studio Server #

Start LM Studio server running on port 1234.

This repo performs 3 functions:

1. Scrapes a website and follows links under the same path up to a maximum depth and outputs the scraped data to the data directory. 

2. Runs an embedding model to embed the text into a Chroma vector database using disk storage (chroma_db directory)

3. Runs a Chat Bot that uses the embeddings to answer questions about the website.

main.py runs all 3 functions. Once the scraper and embeddings have been completed, they do not need to be run again for same website. You can simply run the chatbot.py file.

Prerequisite: Run an LM Studio Server
