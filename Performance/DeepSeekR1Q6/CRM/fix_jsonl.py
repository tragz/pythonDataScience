import json
file_path = "/Users/raghav.tanaji/Desktop/gitrepos/LEARNING/pythonDataScience/Performance/DeepSeekR1Q6/CRM/copilot_function_call_nextstep_230_as_text__gpt-4o.jsonl"

fixed_json_lines = []
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        try:
            json_obj = json.loads(line)  # Validate and parse JSON
            fixed_json_lines.append(json_obj)  # Store valid JSON objects
        except json.JSONDecodeError:
            print("Skipping malformed JSON line:", line.strip())


fixed_file_path = "/Users/raghav.tanaji/Desktop/gitrepos/LEARNING/pythonDataScience/Performance/DeepSeekR1Q6/CRM/copilot_function_call_fixed_json_file.jsonl"
with open(fixed_file_path, "w", encoding="utf-8") as fixed_file:
    for json_obj in fixed_json_lines:
        fixed_file.write(json.dumps(json_obj, ensure_ascii=False) + "\n")

print(fixed_file_path)
