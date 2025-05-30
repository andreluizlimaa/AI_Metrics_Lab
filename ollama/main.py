from langchain_ollama.llms import OllamaLLM

llm = OllamaLLM(model="deepseek-r1:1.5b")

print(llm.invoke("explain to me what is the apollo program"))
print(llm.invoke("write a short story about a robot learning to love"))
print(llm.invoke("what is the capital of France?"))
print(llm.invoke("what are we talking about?"))