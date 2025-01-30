import random
from pathlib import Path
from datasets import load_dataset

# Load the MMLU dataset
dataset = load_dataset("cais/mmlu", "all", split="test")

# Convert dataet to a Pandas Datafram for easy manipulation
df = dataset.to_pandas()

# Sample 20 questions from each subject
num_samples = 20
commands = []

for subject in df['subject'].unique():
    subject_df = df[df['subject'] == subject]

    sampled_questions = subject_df.sample(n=min(num_samples, len(subject_df)), random_state=42)

    for question in sampled_questions["question"]:
        # Skip questions that contain single or double quotes
        if "'" in question or '"' in question:
            continue

        # Construct the command
        command = (
            f'hawk predict get-prediction --app-name EinsteinBYOM --predictor EinsteinSMEndpointSME '
            f'--global --caller-service-ou app --input \'{{ "inputPrompt": "{question}", "maxOutputToken": 200, "additionalProperties":{{}} }}\' '
            f'-e dev4 --header "x-model-name=EinsteinDeepSeekR1"'
        )
        commands.append(command)

# save the commands to a file
output_file = Path("DSR1Q6_hawk_commands.txt")
output_file.write_text("\n".join(commands))

print(f"Command saved to {output_file}")