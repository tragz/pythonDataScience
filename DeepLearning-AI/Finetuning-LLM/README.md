

## Lamini

#### Add Virtual Environment
```bash
    python -m venv venv
    source venv/bin/activate
```

### Install langchain
```bash
    pip install lamini
```


Restart the Kernal after installing the packages

```bash
    curl --location "https://api.lamini.ai/v1/completions" \
--header "Authorization: Bearer 0d17c985c8a4a589637629179374c627ee762f04" \
--header "Content-Type: application/json" \
--data '{
    "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
    "prompt": "How are you?"
}'
```