import boto3
import json
from sagemaker.predictor import Predictor
from sagemaker.serializers import JSONSerializer
from sagemaker.deserializers import JSONDeserializer

# Define the SageMaker endpoint name
ENDPOINT_NAME = "EinsteinDeepSeekR1"

# Create the SageMaker predictor
predictor = Predictor(
    endpoint_name=ENDPOINT_NAME,
    serializer=JSONSerializer(),
    deserializer=JSONDeserializer()
)


# Input and output file paths
input_file = "copilot_function_call_nextstep_230_as_text__gpt-4o.jsonl"
output_file = "copilot_function_call_nextstep_230_as_text__deepSeekr1.jsonl"

# Process the JSONL file
updated_objects = []

with open(input_file, "r") as infile:
    for line in infile:
        #line = infile.readline()
        obj = json.loads(line.strip())  # Read each JSON object
        input_prompt = obj.get("input", "")

        if input_prompt:  # Ensure input exists
            body = {"inputPrompt": input_prompt}
            #print(body)
            try:
                response = predictor.predict(body)
                #print(response)
                obj["output"] = response.get("completions", "No response")
            except Exception as e:
                obj["output"] = f"Error: {str(e)}"
            print(f"\nResponse: {obj['output']}")
        updated_objects.append(obj)

# Save the updated objects back to a JSONL file
with open(output_file, "w") as outfile:
    for obj in updated_objects:
        json.dump(obj, outfile)
        outfile.write("\n")

print(f"Processing complete. Output saved to: {output_file}")
