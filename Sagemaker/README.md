# Perf evaluation of DeepSeekR1

This script runs predictions using an **AWS SageMaker endpoint**.  
It reads input samples, sends them for inference, and records the response time.

## 🚀 Features
- **Loads sample input data** from a file (`samples.txt` by default)
- **Sends batch predictions** to a SageMaker endpoint
- **Records response time** and computes statistics
- **Outputs results** to a JSON file (`samples_results.txt` by default)

---

## 📦 Dependencies

Make sure you have the following dependencies installed:

```sh
pip install boto3 sagemaker tqdm tabulate numpy
```

## 🔧 Usage Instructions

1️⃣ Running with Default Settings

```sh
python predictor.py --model-name EinsteinDeepSeekR1Sglang

```

2️⃣ Running with Custom Settings

```sh
python predictor.py --model-name MySageMakerModel \
                    --input-file my_data.json \
                    --num-samples 100 \
                    --output-file results.json

```

## Understanding the Output

```text
+---------------------+----------+----------+----------+----------+----------+
| Model Name         | Min (s)  | Max (s)  | Mean (s) | Median (s) | P95 (s)  |
+---------------------+----------+----------+----------+----------+----------+
| EinsteinDeepSeekR1 | 0.35     | 1.21     | 0.67     | 0.55      | 1.15     |
+---------------------+----------+----------+----------+----------+----------+

```