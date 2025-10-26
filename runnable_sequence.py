from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()  # Load environment variables from .env file

prompt1 = PromptTemplate(
    input_variables=["Topic"], 
    template="Suggest a catchy blog title about {Topic}?",
)

model=ChatOpenAI()

parser=StrOutputParser()
prompt2=PromptTemplate(
    input_variables=["text"],
    template="Take the following blog title and make it more exciting: {text}",
)

chain= RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({"Topic":"Artificial Intelligence"}))