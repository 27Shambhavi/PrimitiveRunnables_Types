from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()  # Load environment variables from .env file

passthrough=RunnablePassthrough()

# print(passthrough.invoke({"name":"hema"}))

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

jokegen_chain=RunnableSequence(prompt1,model,parser)

parllel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(jokegen_chain,parllel_chain)
result=final_chain.invoke({"Topic":"Cricket"})
print(result)