import json

def update_inference_component_arn(data, new_inference_component, account_mappings):
    updated_data = []
    for account_id, region in account_mappings.items():
        updated_entry = data.copy()
        updated_arn = updated_entry["InferenceComponentArn"].split(":")
        updated_arn[3] = region
        updated_arn[4] = account_id
        updated_arn[-1] = f"inference-component/{new_inference_component}"
        updated_entry["InferenceComponentArn"] = ":".join(updated_arn)
        updated_data.append((updated_entry))

    return updated_data

def build_inference_component_arn(region, account, inference_component):
    return f"arn:aws:sagemaker:{region}:{account}:inference-component/{inference_component}"

# Example input dictionary

data = {
            "CreationTime": "2024-11-01T13:25:14.026000+05:30",
            "InferenceComponentArn": "arn:aws:sagemaker:us-west-2:887927004414:inference-component/EinsteinTextEval",
            "InferenceComponentName": "EinsteinTextEval",
            "EndpointArn": "arn:aws:sagemaker:us-west-2:887927004414:endpoint/einsteinicep4d24xlarge",
            "EndpointName": "EinsteinICEP4D24XLarge",
            "VariantName": "EinsteinICEP4D24XLarge",
            "InferenceComponentStatus": "InService",
            "LastModifiedTime": "2025-02-21T14:00:31+05:30"
        }

new_inference_component = "EinsteinFlowGPT"
new_account_mappings = {
    "689332411343": "us-east-1",
    "815738957781": "eu-central-1"
}

updated_data = update_inference_component_arn(data, new_inference_component, new_account_mappings)

print(json.dumps(updated_data, indent=4))

[print(f"{entry['InferenceComponentArn']}") for entry in updated_data]

for account_id, region  in new_account_mappings.items():
    print(build_inference_component_arn(region, account_id, new_inference_component))

print("\n".join(build_inference_component_arn(region, account_id, new_inference_component) for account_id, region in new_account_mappings.items()))



