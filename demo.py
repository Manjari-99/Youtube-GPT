from langchain.llms import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(temperature=0.9) #randomness of output
text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))