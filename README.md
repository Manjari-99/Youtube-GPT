# Youtube-Title and Script Generator 
![](https://github.com/Manjari-99/Youtube-GPT/blob/5e71eaf08db545f79ba65e6c049ebc76d7c11f94/GPT-1-2.png)
## About
Generative Pre-trained Transformers, commonly known as GPT, are a family of neural network models that uses the transformer architecture and is a key advancement in artificial intelligence (AI) powering generative AI applications such as ChatGPT. GPT models give applications the ability to create human-like text and content (images, music, and more), and answer questions in a conversational manner. Organizations across industries are using GPT models and generative AI for Q&A bots, text summarization, content generation, and search.

Companies like Khan Academy, Duolingo are making their own GPT. Bloomberg has fine-tuned its own GPT model. 

<b>So the Question Lies...Why don't we all do it?</b>
  
Using Langchain Framework - prompts, chains and memory here - and streamlit; I have built an application that Generates the YouTube Title and corresponding video script as per what our user feeds in the prompt. 

## OpenAI - API 
We need to create our own API Key in our OpenAI account and set that value to the variable 'apikey' in apikey.py. This is later imported to our app.py

## Methodology
#### Inside app.py

We set the api key in the os environment dictionary to connect to OpenAI.
We use streamlit as our application framework.
We then add streamlit title, text_input.
We then create an instance of our service with LLMs. 
We use prompt templates and LLMChains. Prompt takes our topic and plugs in with the query, i.e. formatted. LLM has the temperature set that shows the creative independence of the output. We use LLM Chain to run user prompt.
We also use a script chain, and connect it with sequential script chain. We also bring in memory to our application through ConversationBufferMemory. We also add some tools like WikipediaAPIWrapper. So, our prompt template not only takes a title, but also takes in some Wikipedia Research. And... our application is good to go!

## Demo Snapshots 

#### The application 
![](https://github.com/Manjari-99/Youtube-GPT/blob/5e71eaf08db545f79ba65e6c049ebc76d7c11f94/GPT-1.png)

#### The prompt input
![](https://github.com/Manjari-99/Youtube-GPT/blob/5e71eaf08db545f79ba65e6c049ebc76d7c11f94/GPT-2.png)

#### The Title and Script output
![](https://github.com/Manjari-99/Youtube-GPT/blob/5e71eaf08db545f79ba65e6c049ebc76d7c11f94/GPT-3.png)
  
 #### Memory Buffers
 ![](https://github.com/Manjari-99/Youtube-GPT/blob/5e71eaf08db545f79ba65e6c049ebc76d7c11f94/GPT-4.png)
 
 #### Title and Script History
 ![](https://github.com/Manjari-99/Youtube-GPT/blob/5e71eaf08db545f79ba65e6c049ebc76d7c11f94/GPT-5.png)
 
 #### Wikipedia Research 
 ![](https://github.com/Manjari-99/Youtube-GPT/blob/5e71eaf08db545f79ba65e6c049ebc76d7c11f94/GPT-6.png)
 
 ## Conclusion
 
 This project has been made with the fundamental motive of getting familiarised with the concepts of GPT, LLMs, Langchain, etc.


