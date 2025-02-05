from together import Together

client = Together(api_key="tgp_v1_0KGRmgcAHo-SvuQALUXyCi0ly_MsUTp0i2Ps0DxD6w8")

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    messages=[
        {
                "role": "user",
                "content": "hello DS, tell me a story"
        }
    ],
    max_tokens = 100,
    temperature=0.6,
    top_p=0.95,
    top_k=50,
    repetition_penalty=1,
    stop=["<｜end▁of▁sentence｜>"],
    stream=False
)

print(response.choices[0].message.content)
'''
for token in response:
    if hasattr(token, 'choices'):
        print(token.choices[0].delta.content, end='', flush=True)
'''