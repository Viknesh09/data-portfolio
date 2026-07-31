import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Load FAISS index
index = faiss.read_index(
    "telecom_faiss.index"
)

# Load chunks
with open(
    "telecom_chunks.pkl",
    "rb"
) as f:

    chunks = pickle.load(f)

# RAG Retrieval
def retrieve_context(query):

    query_embedding = model.encode(
        [query]
    )

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        1
    )

    idx = indices[0][0]

    if idx < len(chunks):

        return chunks[idx][:500]

    return "No relevant information found."