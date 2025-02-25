import random
import json
import time
from tqdm import tqdm
from tabulate import tabulate
from sagemaker.predictor import Predictor
from sagemaker.serializers import JSONSerializer
from sagemaker.deserializers import JSONDeserializer
import numpy as np  # For statistical calculations

# Define SageMaker endpoint
ENDPOINT_NAME = "EinsteinDeepSeekR1Sglang"

# File paths
INPUT_FILE = "/Users/raghav.tanaji/Desktop/gitrepos/LEARNING/pythonDataScience/Performance/DeepSeekR1Q6/Datasets/samples.txt"
OUTPUT_FILE = "samples_results.txt"

# Create SageMaker predictor
predictor = Predictor(
    endpoint_name=ENDPOINT_NAME,
    serializer=JSONSerializer(),
    deserializer=JSONDeserializer()
)


def load_valid_json_lines(file_path, sample_size=50):
    """Reads a file, filters valid JSON lines, and returns a random sample."""
    with open(file_path, "r") as file:
        valid_lines = [line.strip() for line in file if is_valid_json(line)]

    if len(valid_lines) < sample_size:
        raise ValueError(f"Not enough valid JSON lines. Found {len(valid_lines)}, needed {sample_size}")

    sampled_lines = random.sample(valid_lines, sample_size)
    return [json.loads(line) for line in sampled_lines]


def is_valid_json(line):
    """Checks if a string is valid JSON."""
    try:
        json.loads(line)
        return True
    except json.JSONDecodeError:
        return False


def prepare_payloads(json_objects):
    """Extracts input data from JSON objects for prediction."""
    return [
        {
            "inputPrompt": obj.get("inputPrompt", ""),
            "maxOutputToken": obj.get("maxOutputToken", 100)  # Default to 100 if missing
        }
        for obj in json_objects
    ]


def run_predictions(payloads):
    """Runs predictions on a batch of payloads and records response times."""
    results = []
    times = []

    for payload in tqdm(payloads, desc="Processing Payloads"):
        start_time = time.time()
        try:
            response = predictor.predict(payload)
        except Exception as e:
            response = {"error": str(e)}
        end_time = time.time()

        elapsed_time = end_time - start_time
        times.append(elapsed_time)

        completion_text = extract_completion_text(response)

        results.append({
            "input": payload,
            "output": completion_text,
            "time_taken": elapsed_time
        })

    return results, times


def extract_completion_text(response):
    """Extracts completion text from the model's response."""
    if isinstance(response, dict) and "completions" in response and response["completions"]:
        return response["completions"][0].get("completionText", "").strip()
    return ""


def calculate_statistics(times):
    """Computes timing statistics."""
    return {
        "min_time": np.min(times),
        "max_time": np.max(times),
        "mean_time": np.mean(times),
        "median_time": np.median(times),
        "p95_time": np.percentile(times, 95)
    }


def save_results_to_file(results, file_path):
    """Saves results to a JSON file."""
    with open(file_path, "w") as f:
        json.dump(results, f, indent=4)


def print_statistics_table(stats):
    """Prints performance statistics in a table format."""
    table = [
        ["EinsteinDeepSeekR1 - JumpStart", stats["min_time"], stats["max_time"],
         stats["mean_time"], stats["median_time"], stats["p95_time"]]
    ]
    headers = ["Model Name", "Min (s)", "Max (s)", "Mean (s)", "Median (s)", "P95 (s)"]
    print(tabulate(table, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    try:
        json_objects = load_valid_json_lines(INPUT_FILE)
        payloads = prepare_payloads(json_objects)
        results, times = run_predictions(payloads)
        save_results_to_file(results, OUTPUT_FILE)

        stats = calculate_statistics(times)
        print_statistics_table(stats)

    except Exception as e:
        print(f"Error: {e}")
