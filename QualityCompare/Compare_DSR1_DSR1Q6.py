import subprocess
import json
import random

import openai  # Assuming GPT-4 API is used for evaluation


openai.api_key = "
# Read the file
file_path = "/Users/raghav.tanaji/Desktop/gitrepos/LEARNING/pythonDataScience/Performance/DeepSeekR1Q6/Datasets/samples.txt"

# Extract input prompts
input_prompts = []
with open(file_path, "r") as file:
    for line in file:
        try:
            input_prompts.append(line.strip().replace("'", '"'))
        except json.JSONDecodeError:
            continue  # Skip lines that aren't valid JSON

# Select 10 random prompts
random_prompts = random.sample(input_prompts, 10)
random_prompts

# Define models
models = ["EinsteinDeepSeekR1", "EinsteinDeepSeekR1Full"]
app_name = "EinsteinBYOM"
predictor = "EinsteinSMEndpointSME"
env = "dev4"

# Selected prompts from samples.txt
prompts = [
    "When did the cyber-security discourse emerge? (When did politicians, academics, and other agents begin to talk seriously about cyber-security?)",
    "According to Cicero, immorality is __________, and expediency is __________.",
    "In 1997, the World Bank found that the fraction of the world’s population living in low and lower-middle income countries—that is, countries with per capita incomes of $1230 or less—was approximately",
    "An insurance agent is successful in selling a life insurance policy to 20 percent of the customers he contacts. He decides to construct a simulation to estimate the mean number of customers he needs to contact before being able to sell a policy. Which of the following schemes should he use to do the simulation?",
    "Two scientists at a conference on evolution take to the stage on day 3 to argue their theories against one other. Each is a devout student of their own philosophy. The first scientist contends that organisms evolved via the increase of organs that were used the most during their time. They would then pass these on to subsequent generations. The second scientist, however, believed that advantages each organism possessed were absent for a long time, randomly occurred, and when they were beneficial, that organism would rapidly populate the population over a short period of time, evolutionarily speaking. Which of the following statements would strengthen the second scientist’s argument?",
    "A balance of payments deficit means that a country has",
    "The solid-state structures of the principal allotropes of elemental boron are made up of which of the following structural units?",
    "A framework categorizes different services, which, in turn, influence the degree to which market offerings can be evaluated, and three main properties are identified:",
    "Form A of a standardized personality test was given in the fall and again in the spring to the same group of people. The reliability estimate that resulted from this research is referred to as",
    "A researcher interested in examining the potential impact of parent alcoholism on child and family development recruits 12-year-olds (n = 100), 13-year-olds (n = 100), and 14-year-olds (n = 100)—half of whom have an alcoholic parent and half of whom do not—into a multiple-year longitudinal study assessing various outcomes. This study is best characterized as:"
]

prompts = random_prompts


def get_prediction(model, prompt):
    """Runs the hawk CLI command and extracts the response."""
    command = f"""
    hawk predict get-prediction --app-name {app_name} --predictor {predictor} \
    --global --caller-service-ou app --input '{prompt}' \
    -e {env} --header "x-model-name={model}" | jq '{{request: .inputPrompt, response: .completions[].completionText}}'
    """

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return json.loads(result.stdout) if result.stdout else None
    except Exception as e:
        print(f"Error running command: {e}")
        return None


def evaluate_responses(response1, response2, prompt, log_file="/Users/raghav.tanaji/Desktop/gitrepos/LEARNING/pythonDataScience/Performance/DeepSeekR1Q6/Resultsevaluation_log.txt"):
    """Uses GPT-4 to evaluate accuracy, coherence, and relevance."""
    evaluation_prompt = f"""
    Compare the following responses to the question: "{json.loads(prompt)["inputPrompt"]}"

    Model 1 Response: {response1}
    Model 2 Response: {response2}

    Rate each model on:
    - Accuracy (1-5)
    - Coherence (1-5)
    - Relevance (1-5)

    Provide structured JSON output: 
    {{"Model1": {{"accuracy": X, "coherence": Y, "relevance": Z}}, "Model2": {{"accuracy": A, "coherence": B, "relevance": C}}}}
    """

    with open(log_file, "a") as file:
        file.write(evaluation_prompt + "\n\n")
    ''''
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an evaluator that scores AI-generated text."},
                  {"role": "user", "content": evaluation_prompt}],
        temperature=0
    )

    return json.loads(response["choices"][0]["message"]["content"])
    '''
    return None


def main():
    results = []

    for prompt in prompts:
        responses = {model: get_prediction(model, prompt) for model in models}

        if all(responses.values()):
            eval_result = evaluate_responses(responses[models[0]]["response"], responses[models[1]]["response"], prompt)
            results.append({"prompt": prompt, "responses": responses, "evaluation": eval_result})
        else:
            print(f"Failed to fetch responses for: {prompt}")

    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()
