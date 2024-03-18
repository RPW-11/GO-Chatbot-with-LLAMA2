from llm import qa_engine

def get_answer (question: str) -> str:
    print("Inferencing....")
    print(f"Question: {question}")
    res = qa_engine.invoke(question)
    print("Done")
    return res['result']