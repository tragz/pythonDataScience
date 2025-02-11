import requests
import json
import time
import statistics
import concurrent.futures
from collections import defaultdict
from tabulate import tabulate

# API URL and headers
API_URL = "https://bot-svc-llm.sfproxy.einstein.aws-dev4-uswest2.aws.sfdc.cl/v1.0/chat/generations"
HEADERS = {
    "Authorization": "API_KEY 651192c5-37ff-440a-b930-7444c69f4422",
    "x-client-feature-id": "Service replies",
    "x-sfdc-core-tenant-id": "core/falcondev-core002sdb3/00DSB0000003kSv2AI",
    "x-sfdc-app-context": "EinsteinGPT",
    "Content-Type": "application/json"
}

# Models to test
MODELS = [
    "llmgateway__EinsteinDeepSeekR1",
    "llmgateway__OpenAIGPT35Turbo_01_25",
    "llmgateway__BedrockAnthropicClaude35Sonnet",
    "llmgateway__VertexAIGeminiPro15"
]

MODELS = ["llmgateway__EinsteinDeepSeekR1"]

# Create 30 "Hello" prompts
samples = ["Hello"] * 30

# Store response times
response_times = defaultdict(list)


# Function to send request
def send_request(model, prompt):
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": model,
        "generation_settings": {}
    }

    start_time = time.time()
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    end_time = time.time()

    return model, end_time - start_time


for model in MODELS:
    for prompt in samples:
        payload = {
            "messages": [{"role": "user", "content": prompt}],
            "model": model,
            "generation_settings": {}
        }

        start_time = time.time()
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        end_time = time.time()

        elapsed_time = end_time - start_time
        response_times[model].append(elapsed_time)


# Calculate statistics
def calculate_statistics(times):
    if not times:
        return {"min": 0, "max": 0, "mean": 0, "median": 0, "p50": 0, "p95": 0}

    times.sort()
    p95_index = max(1, int(0.95 * len(times))) - 1  # Ensure at least 1 index
    return {
        "min": min(times),
        "max": max(times),
        "mean": statistics.mean(times),
        "median": statistics.median(times),
        "p95": times[p95_index]  # Use sorted list for p95 calculation
    }


stats = {model: calculate_statistics(response_times[model]) for model in MODELS}

# Print results as a table
table_data = []
for model, stat in stats.items():
    table_data.append(
        [model, f"{stat['min']:.3f}", f"{stat['max']:.3f}", f"{stat['mean']:.3f}", f"{stat['median']:.3f}",
         f"{stat['p95']:.3f}"])

print(tabulate(table_data, headers=["Model Name", "Min (s)", "Max (s)", "Mean (s)", "Median (s)", "P95 (s)"],
               tablefmt="grid"))
