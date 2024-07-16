
# OpenAI
Access OpenAI models


## Installation

#### Add Virtual Environment
```bash
    python -m venv venv
    source venv/bin/activate
```

#### Install openAI

```bash
    pip install openai
```
    
## Documentation

[OpenAI - Api-keys](https://platform.openai.com/settings/profile?tab=api-keys)

```
    OPENAI_API_KEY = sk-None-2n9XsnynslmDJbPMcjsAT3BlbkFJsj8bKltuSR90JSdBjTXY
```

#### Set environment variable

```python
    import os
    import pprint
    os.environ["OPENAI_API_KEY"]="sk-None-2n9XsnynslmDJbPMcjsAT3BlbkFJsj8bKltuSR90JSdBjTXY"
    openai_key = os.environ.get('OPENAI_API_KEY')
    print(openai_key)

    # Get the list of user's 
    env_var = os.environ

    # Print the list of user's 
    print("User's Environment variable:") 
    pprint.pprint(dict(env_var), width = 1) 
    
```
