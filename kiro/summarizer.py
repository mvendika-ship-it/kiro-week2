import boto3

# Initialize Bedrock Runtime client
client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

prompt = """
Summarize the following text in 4-5 lines, make it clean and meaningful:
Artificial Intelligence (AI) is transforming the world by enabling machines to learn, reason, and make decisions like humans. It is impacting every industry including healthcare, education, business, and transportation. With rapid advancements, AI has the potential to solve complex global challenges and improve the quality of life for millions of people. However, it also requires responsible usage to ensure safety and fairness for everyone.
"""

body = {
    "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}]}],
    "max_tokens": 500,
    "temperature": 0.7,
}

response = client.invoke_model(
    modelId="anthropic.claude-3-haiku-20240307-v1:0",
    body=str(body)
)

print(response['body'].read().decode('utf-8'))
