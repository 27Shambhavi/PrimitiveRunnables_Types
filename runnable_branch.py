from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda

load_dotenv()  # Load environment variables from .env file

prompt1 = PromptTemplate(
    input_variables=["Topic"], 
    template="Write a detailed topic {Topic}?",
)

prompt2=PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in a concise manner: {text}",
)
model=ChatOpenAI()

parser=StrOutputParser()
report_gen_chain=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableParallel(
    (lambda x: len(x['text'].split()) > 500):RunnableSequence(prompt2,model,parser)
    default:RunnablePassthrough()
)
final_chain=RunnableSequence(report_gen_chain,branch_chain)
final_chain.invoke({"Topic":"Climate Change Effects"})  
result=final_chain.invoke({"Topic":"Climate Change Effects"})
print(result)