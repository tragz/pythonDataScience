from difflib import unified_diff

file_path = "/Users/raghav.tanaji/Desktop/gitrepos/LEARNING/pythonDataScience/Performance/DeepSeekR1Q6/CRM/copilot_function_call_nextstep_230_as_text__gpt-4o.jsonl"
fixed_file_path = "/Users/raghav.tanaji/Desktop/gitrepos/LEARNING/pythonDataScience/Performance/DeepSeekR1Q6/CRM/copilot_function_call_fixed_json_file.jsonl"

# Read original file
with open(file_path, "r", encoding="utf-8") as original_file:
    original_lines = original_file.readlines()

# Read fixed file
with open(fixed_file_path, "r", encoding="utf-8") as fixed_file:
    fixed_lines = fixed_file.readlines()

# Generate the diff
diff = list(unified_diff(original_lines, fixed_lines, fromfile="original.jsonl", tofile="fixed.jsonl"))

# Join and display the difference if any
diff_output = "\n".join(diff) if diff else "No differences found."
diff_output[:5000]