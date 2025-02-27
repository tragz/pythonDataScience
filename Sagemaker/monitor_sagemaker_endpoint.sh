#!/bin/bash

# Take endpoint name as input
read -p "Enter the SageMaker Endpoint Name: " ENDPOINT_NAME

while true; do
    # Fetch the endpoint status
    STATUS=$(aws sagemaker describe-endpoint --endpoint-name "$ENDPOINT_NAME" --query 'EndpointStatus' --output text)

    # Print the status with timestamp
    echo "$(date) - Endpoint '$ENDPOINT_NAME' Status: $STATUS"

    # If endpoint is InService, exit
    if [[ "$STATUS" == "InService" ]]; then
        echo "✅ Endpoint '$ENDPOINT_NAME' is ready!"
        break
    fi

    # Wait for 1 minute before checking again
    sleep 60
done
