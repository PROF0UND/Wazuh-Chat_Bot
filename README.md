# Wazuh-MCP-Server

## Requirements:

- This project requires ollama's llama3 to run.
- To download, run:
1. Install ```Ollama```
``` bash
curl -fsSL https://ollama.com/install.sh | sh
```
2. Install the required Llama 3 LLM model:
```
ollama pull llama3
```

## The threat hunter file:

- This python file runs a chatbot connected to the logs of wazuh

## Requirements file

- This file has all dependencies
- To install all dependencies, type:
``` bash
pip install requirements.txt
```

## Notes

### Elasticsearch Password:

The following instructions are for Windows.

- The elasticsearch file is saved in C:ELK
- The default password is "elastic".
- To check/regenerate password, type:
``` bash
cd C:\ELK\elasticsearch-9.1.0\bin
elasticsearch-reset-password.bat -u elastic
```

### Elasticsearch Setup:
- To run elasticsearch, run the elasticsearch.bat file (Windows).