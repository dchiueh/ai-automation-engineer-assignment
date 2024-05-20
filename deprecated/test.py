import openai
import sys
from dotenv import load_dotenv
import os
import json
from data import output_1, output_2, output_3, input_1, input_2, input_3

load_dotenv('.env.example')
api_key = os.getenv('OPENAI_API_KEY')
print(api_key)

openai.api_key = api_key

try:
    with open(sys.argv[1], "r") as file:
        content = file.read()
        # print("File content:")
        # print(content)
except FileNotFoundError:
    print(f"Error: File not found.")


response = openai.chat.completions.create(
    model="gpt-4o",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a San Francisco Chronicle social media copywriter. Please return a headline, SEO URL, and social media post copy for each article the user inputs. Make sure the tone matches SF Chronicle standards, which is generally informative, balanced, and community-focused. Please return the result in JSON."},
        {"role": "user", "content": input_1}, 
        {"role": "assistant", "content": json.dumps(output_1)},
        {"role": "user", "content": input_2},
        {"role": "assistant", "content": json.dumps(output_2)},
        {"role": "user", "content": input_3},
        {"role": "assistant", "content": json.dumps(output_3)},
         {"role": "user", "content": content}
    ],
    temperature = 0.2,
    seed=1
)

print(response.choices[0].message.content)