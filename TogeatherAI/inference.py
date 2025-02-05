import json
import requests
import os

# Load API key from environment variables
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "your-api-key")


def model_fn(model_dir):
    """Load model artifacts (not used, as we're calling an external API)."""
    return None


def input_fn(request_body, request_content_type):
    """Parse incoming requests."""
    if request_content_type == "application/json":
        return json.loads(request_body)
    else:
        raise ValueError(f"Unsupported content type: {request_content_type}")


def predict_fn(input_data, model):
    """Process input and make request to Together AI."""
    api_url = "https://api.together.xyz/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": input_data.get("messages", []),
        "max_tokens": input_data.get("max_tokens", None),
        "temperature": 0.6,
        "top_p": 0.95,
        "top_k": 50,
        "repetition_penalty": 1,
        "stop": ["<｜end▁of▁sentence｜>"],
        "stream": False  # Set to False to get a normal response
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}


def output_fn(prediction, response_content_type="application/json"):
    """Format output response."""
    return json.dumps(prediction), response_content_type
