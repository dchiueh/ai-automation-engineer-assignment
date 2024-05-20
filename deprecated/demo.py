from superjsonmode.integrations.openai import StructuredOpenAIModel
import openai
from pydantic import BaseModel
import json
from dotenv import load_dotenv
import os

load_dotenv('.env.example')
api_key = os.getenv('OPENAI_API_KEY')
print(api_key)


model = StructuredOpenAIModel(model="gpt-4o")

class Output(BaseModel):
    headline: str
    seo_url: str
    social_media_post: int

prompt = ""
prompt_template = """{prompt}

Please fill in the following information about this character for this key. Keep it succinct. It should be a {type}.

{key}: """

output = model.generate(
    prompt,
    extraction_prompt_template=prompt_template,
    schema=Output,
    batch_size=3,
    stop=["\n\n"],
    temperature=0,
)

print(json.dumps(output, indent=2))