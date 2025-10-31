import json
import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "math_kb"

model = SentenceTransformer(MODEL_NAME)
client = QdrantClient(":memory:")

def initialize_kb():
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )

    with open("./data/kb.json", "r") as f:
        kb = json.load(f)

    vectors, payloads = [], []
    for idx, item in enumerate(kb):
        embedding = model.encode(item["question"]).tolist()
        vectors.append(PointStruct(id=idx, vector=embedding, payload=item))
    client.upsert(collection_name=COLLECTION_NAME, points=vectors)
    print("✅ Knowledge Base initialized with", len(kb), "entries.")

def search_kb(query: str):
    embedding = model.encode(query).tolist()
    results = client.search(
        collection_name=COLLECTION_NAME, query_vector=embedding, limit=1
    )
    if results and results[0].score > 0.75:
        return results[0].payload["answer"]
    return None
