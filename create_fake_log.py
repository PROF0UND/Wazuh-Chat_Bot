"""
Creates a new fake log in the "my-logs" index
To make the chatbot run on this log, change the index param in load_logs_from_days to "my-logs"
"""


from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "<YOUR_ELASTIC_PASSWORD>"),
    verify_certs=False  # or provide ca_certs if you're validating SSL
)

log_entry = {
  "timestamp": "2025-07-29T17:38:27.370625",
  "rule": {
    "level": 10,
    "description": "Multiple failed login attempts"
  },
  "agent": {
    "id": "001",
    "name": "ubuntu-server"
  },
  "manager": {
    "name": "wazuh-manager"
  },
  "id": "1698765432.123456",
  "full_log": "sshd[1234]: Failed password for invalid user root from 192.168.1.100 port 22 ssh2",
  "input": {
    "type": "log"
  },
  "decoder": {
    "name": "sshd"
  },
  "data": {
    "srcip": "192.168.1.100",
    "username": "root"
  }
}


res = es.index(index="my-logs", document=log_entry)
print("Document ID:", res['_id'])
