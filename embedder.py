import langchain_community.embeddings
from langchain.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from torch import cuda
import sys

path = "./content"
embedding_directory = "./content/chroma_db"

embedding_db = None;

def embed():

    print("\nCalculating Embeddings\n")

    # Load the text from the path
    text_loader_kwargs = {'autodetect_encoding': True}
    loader=DirectoryLoader(path,
                        glob="./*.txt",
                        loader_cls=TextLoader,  loader_kwargs=text_loader_kwargs)

    documents=loader.load()

    # Split the data into chunks
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,
                                                chunk_overlap=50)

    chunks = text_splitter.split_documents(documents)

    # Load the huggingface embedding model
    model_name = "BAAI/bge-base-en"
    encode_kwargs = {'normalize_embeddings': True} # set True to compute cosine similarity

    device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'
    embedding_model = langchain_community.embeddings.HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs={'device': device},
        encode_kwargs=encode_kwargs
    )

    embedding_db = Chroma.from_documents(chunks, embedding_model, persist_directory=embedding_directory)

    print("Embeddings completed")
