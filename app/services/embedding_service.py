from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(text_chunks):
    embeddings = model.encode(text_chunks)
    return embeddings


def embed_query(query):
    embedding = model.encode(query)
    return embedding