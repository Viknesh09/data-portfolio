import fitz
import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

# =====================================================
# CONFIG
# =====================================================

PDF_FILE = "zends_communications_telecom_knowledge_base.pdf"

EMBED_MODEL = "all-MiniLM-L6-v2"

# =====================================================
# LOAD PDF
# =====================================================

def extract_pdf_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:

        text += page.get_text()

    return text

# =====================================================
# CHUNKING
# =====================================================

def split_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunks.append(text[i:i+chunk_size])

    return chunks

# =====================================================
# MAIN
# =====================================================

print("Reading PDF...")

text = extract_pdf_text(PDF_FILE)

chunks = split_text(text)

print("Total Chunks:", len(chunks))

# =====================================================
# EMBEDDINGS
# =====================================================

model = SentenceTransformer(EMBED_MODEL)

embeddings = model.encode(chunks)

embeddings = np.array(
    embeddings,
    dtype=np.float32
)

# =====================================================
# FAISS
# =====================================================

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# save index

faiss.write_index(
    index,
    "telecom_faiss.index"
)

# save chunks

with open(
    "telecom_chunks.pkl",
    "wb"
) as f:

    pickle.dump(chunks, f)

print("FAISS DB Created")