from src.llm import ask_llm


question = "What is income from other sources?"

answer = ask_llm(question)

print("\nAnswer:\n")
print(answer)