import faiss
import numpy as np
import os

VECTOR_PATH = "app/database/vector_db/faiss.index"
TEXT_PATH = "app/database/vector_db/chunks.npy"


def store_embeddings(embeddings, chunks):

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    os.makedirs("app/database/vector_db", exist_ok=True)

    faiss.write_index(index, VECTOR_PATH)

    np.save(TEXT_PATH, np.array(chunks))


def search_embeddings(query_embedding, k=5):

    index = faiss.read_index(VECTOR_PATH)

    chunks = np.load(TEXT_PATH, allow_pickle=True)

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    results = [chunks[i] for i in indices[0]]

    return results