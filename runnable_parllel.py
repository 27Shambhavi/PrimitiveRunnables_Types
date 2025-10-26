from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel

load_dotenv()  # Load environment variables from .env file


prompt1= PromptTemplate(
    input_variables=["Topic"], 
    template="Generate a tweet about {Topic}?",
)
prompt2= PromptTemplate(
    input_variables=["Topic"], 
    template="Generate a linkedin post {Topic}?",
)
model = ChatOpenAI()
parser= StrOutputParser()

parllel_chain=RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin_post': RunnableSequence(prompt2, model, parser)
})

result=parllel_chain.invoke({"Topic":"Artificial Intelligence"})
print(result)  