import requests
import json
import time
import statistics

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

# Read 10 input prompts from samples.txt
samples = []
with open("/Users/raghav.tanaji/Desktop/gitrepos/LEARNING/pythonDataScience/Performance/DeepSeekR1Q6/Datasets/samples.txt", "r", encoding="utf-8") as file:
    for _ in range(10):
        line = file.readline()
        if not line:
            break
        try:
            data = json.loads(line)
            samples.append(data["inputPrompt"])
        except json.JSONDecodeError:
            continue

# Store response times
response_times = {model: [] for model in MODELS}

# Store results
results = {model: [] for model in MODELS}

# Send requests
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

        try:
            response_json = response.json()
            generations = response_json.get("generation_details", {}).get("generations", [])
            content = generations[0].get("content", "No response") if generations else "No response"
            results[model].append(content)
        except json.JSONDecodeError:
            results[model].append("Invalid JSON response")


# Calculate statistics
def calculate_statistics(times):
    return {
        "min": min(times) if times else 0,
        "max": max(times) if times else 0,
        "median": statistics.median(times) if times else 0,
        "p50": statistics.median(times) if times else 0,
        "p95": statistics.quantiles(times, n=100)[94] if len(times) >= 20 else 0
    }


stats = {model: calculate_statistics(response_times[model]) for model in MODELS}

# Print results
for model, stat in stats.items():
    print(f"Model: {model}")
    print(
        f"Min: {stat['min']:.3f} s, Max: {stat['max']:.3f} s, Median: {stat['median']:.3f} s, P50: {stat['p50']:.3f} s, P95: {stat['p95']:.3f} s")
    '''
    print("Responses:")
    for i, response in enumerate(results[model], 1):
        print(f"{i}. {response}")
    '''
    print("-" * 50)
