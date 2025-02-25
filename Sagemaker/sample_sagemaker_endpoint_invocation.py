import boto3
import json
from sagemaker.predictor import Predictor
from sagemaker.serializers import JSONSerializer
from sagemaker.deserializers import JSONDeserializer

# Define the SageMaker endpoint name
ENDPOINT_NAME = "EinsteinDeepSeekR1Sglang"

# Create the SageMaker predictor
predictor = Predictor(
    endpoint_name=ENDPOINT_NAME,
    serializer=JSONSerializer(),
    deserializer=JSONDeserializer()
)

inputPrompt = "Write a simple poem like khalil gibran and think"
maxOutputTokens = 20
body = f'{{ "inputPrompt": {json.dumps(inputPrompt)}, "maxOutputToken": {maxOutputTokens} }}'


print(body)
response = predictor.predict(json.loads(body))
print(response)
