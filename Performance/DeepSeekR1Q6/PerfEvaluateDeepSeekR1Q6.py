import time
import subprocess
from pathlib import Path
import numpy as np
from langchain.schema.runnable import RunnableLambda
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv


def measure_command_time(command):
    """Executes a system command and measures the response time."""
    start_time = time.perf_counter()

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    return {
        "command": command,
        "output": result.stdout.strip(),
        "error": result.stderr.strip(),
        "response_time": elapsed_time
    }


def run_commands_from_file(file_path, output_file_path):
    """Reads commands from a file and measures execution time for each."""
    path = Path(file_path)

    if not path.exists():
        print(f"Error: File '{file_path}' not found.")
        return []

    commands = [line.strip() for line in path.read_text().splitlines() if line.strip()]
    print(f"Total {len(commands)} commands to execute.")

    command_runner = RunnableLambda(measure_command_time)
    progress_bar = tqdm(total=len(commands), desc="Executing Commands", ncols=100, unit="command")

    results = []
    num_workers = 2
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = {executor.submit(command_runner.invoke, command): command for command in commands}

        for future in as_completed(futures):
            result = future.result()
            results.append(result)

            progress_bar.update(num_workers)
            # Update progress bar after every 2 executions
            '''
            if len(results) % 10 == 0:
                print("=" * 40)
                print(f"Command: {result['command']}")
                print(f"Output: {result['output']}")
                print(f"Error: {result['error'] if result['error'] else 'No Errors'}")
                print(f"Response Time: {result['response_time']:.6f} seconds")
                print("=" * 40)
            '''

    progress_bar.close()

    with open(output_file_path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write header
        writer.writerow(["command", "response_time"])

        # Write command and response time for each result
        for res in results:
            writer.writerow([res['command'], f"{res['response_time']:.3f}"])

    return results


file_path = Path("/Users/raghav.tanaji/Desktop/gitrepos/LEARNING/pythonDataScience/Performance/DeepSeekR1Q6/test_100_prompts.txt")
output_file_path = Path("DSR1Q6_2.txt")
results = run_commands_from_file(file_path, output_file_path)

response_times = [res['response_time'] for res in results]
# Calculate min, max, and 95th percentile response times
min_time = np.min(response_times)
max_time = np.max(response_times)
p95_time = np.percentile(response_times, 95)

# Display statistical results
print("\nStatistical Summary:")
print(f"Minimum Response Time: {min_time:.3f} seconds")
print(f"Maximum Response Time: {max_time:.3f} seconds")
print(f"95th Percentile Response Time: {p95_time:.3f} seconds")
