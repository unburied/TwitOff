
import basilica
import os
from dotenv import load_dotenv


sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...",
]

load_dotenv()
BASILICA_API_KEY = os.getenv("BASILICA_API_KEY", default="OOPS")

with basilica.Connection(BASILICA_API_KEY) as c:
    embeddings = list(c.embed_sentences(sentences))

print(embeddings)
