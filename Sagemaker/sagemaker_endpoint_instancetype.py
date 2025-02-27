import boto3
from tabulate import tabulate

# Initialize AWS clients
sagemaker_client = boto3.client("sagemaker")
sts_client = boto3.client("sts")


def get_account_and_region():
    """Fetch AWS account ID and region."""
    account_id = sts_client.get_caller_identity()["Account"]
    region = sagemaker_client.meta.region_name
    return account_id, region


def list_endpoints_with_instance_types():
    """Fetch all SageMaker endpoints along with their instance types."""
    response = sagemaker_client.list_endpoints()
    endpoints = response.get("Endpoints", [])

    result = []

    for endpoint in endpoints:
        endpoint_name = endpoint["EndpointName"]

        # Get endpoint details
        endpoint_details = sagemaker_client.describe_endpoint(EndpointName=endpoint_name)

        # Get endpoint configuration name
        endpoint_config_name = endpoint_details["EndpointConfigName"]

        # Get endpoint config details
        endpoint_config_details = sagemaker_client.describe_endpoint_config(EndpointConfigName=endpoint_config_name)

        # Extract instance types from ProductionVariants
        instance_types = [
            variant["InstanceType"] for variant in endpoint_config_details.get("ProductionVariants", [])
        ]

        result.append([endpoint_name, ", ".join(instance_types) if instance_types else "No instance type found"])

    return result


if __name__ == "__main__":
    # Get AWS account and region
    account_id, region = get_account_and_region()

    # Get endpoints data
    endpoints = list_endpoints_with_instance_types()

    # Display output
    print(f"AWS Account: {account_id}")
    print(f"Region: {region}")

    if not endpoints:
        print("No SageMaker endpoints found.")
    else:
        print(tabulate(endpoints, headers=["Endpoint Name", "Instance Types"], tablefmt="grid"))
