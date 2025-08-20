# Wazuh-MCP-Server

## Overview

This project integrates Wazuh logs with a chatbot powered by Ollama's LLaMA 3 language model, allowing you to query and analyze security data in natural language.It also includes utilities for generating and viewing logs in your Elasticsearch instance.

## Prerequisites

- Ollama installed on your system

- LLaMA 3 model available locally

- Elasticsearch server (local or remote)

- Python 3.8+

## Installation

### 1. Install Ollama
```
curl -fsSL https://ollama.com/install.sh | sh
```
### 2. Download the LLaMA 3 model
```
ollama pull llama3
```
### 3. Install Python dependencies
```
pip install -r requirements.txt
```
### 4. Change the Lines 34 and 35 to have the Chatbot's login info:
```
username="<CHATBOT_USERNAME>"
password="<CHATBOT_PASSWORD>"
```
## Project Structure

| File                 | Description                                                      |
| -------------------- | ---------------------------------------------------------------- |
| `Threat_hunter.py`   | Chatbot interface connected to Wazuh logs                        |
| `create_fake_log.py` | Generates sample logs in your Elasticsearch server               |
| `view_logs.py`       | Retrieves and displays logs from a specified Elasticsearch index |
| `requirements.txt`   | Python dependencies list                              

## Elasticsearch Setup

### 1. Running Elasticsearch (Windows)

If Elasticsearch is installed in C:\ELK, start it by running:
```
cd C:\ELK\elasticsearch-9.1.0\bin
elasticsearch.bat
```
### 2. Default Password

Default elastic user password: `elastic`

To reset or view the password:
```
cd C:\ELK\elasticsearch-9.1.0\bin
elasticsearch-reset-password.bat -u elastic
```
## Notes

The chatbot requires a running Elasticsearch instance with Wazuh logs indexed.

The LLaMA 3 model must be loaded via Ollama before starting Threat_hunter.py.

