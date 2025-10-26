from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda

load_dotenv()  # Load environment variables from .env file

prompt1 = PromptTemplate(
    input_variables=["Topic"], 
    template="Suggest a catchy blog title about {Topic}?",
)

model=ChatOpenAI()

parser=StrOutputParser()
joke_gen_chain=RunnableSequence(prompt1,model,parser)

parllel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(lambda x: len(x['joke'].split())),
    'explanation':RunnableSequence(prompt1,model,parser)
})  

final_chain=RunnableSequence(joke_gen_chain,parllel_chain)
result=final_chain.invoke({"Topic":"ML"})  
print(result)