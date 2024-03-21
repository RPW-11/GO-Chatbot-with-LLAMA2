from llm import get_qaengine

def get_answer (question: str) -> str:
    qa_engine = get_qaengine()
    print("Inferencing....")
    print(f"Question: {question}")
    res = qa_engine.invoke(question)
    print("Done")
    print(res)
    return res