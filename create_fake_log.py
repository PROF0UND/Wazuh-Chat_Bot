from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "en*4XhvQRwGAoBmFRnBG"),
    verify_certs=False  # or provide ca_certs if you're validating SSL
)

log_entry = {
    "timestamp": datetime.now().isoformat(),
    "event": "User login failed",
    "user": "admin",
    "ip": "192.168.1.100",
    "threat_level": "high"
}

res = es.index(index="my-logs", document=log_entry)
print("Document ID:", res['_id'])
