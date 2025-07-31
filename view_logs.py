from elasticsearch import Elasticsearch

es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "en*4XhvQRwGAoBmFRnBG"),
    verify_certs=False
)

response = es.search(index="my-logs", size=10, query={"match_all": {}})
for hit in response["hits"]["hits"]:
    print(hit["_source"])
