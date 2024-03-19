from langchain.llms.llamacpp import LlamaCpp
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from vector_store import pine_vectorstore
from constants import PROMP_TEMPLATE, TEMPLATE_INPUT_VARIABLES



prompt_template = PromptTemplate(template=PROMP_TEMPLATE, input_variables=TEMPLATE_INPUT_VARIABLES)
chain_type_kwargs = {'prompt':prompt_template}
_llama2, _qa_engine = [None, None]

def init():
    print(f"Initializing model...")

    global _llama2
    _llama2 = LlamaCpp(
        model_path='models/llama-2.gguf',
        n_gpu_layers=-1,
        n_batch=512,
        verbose=False,
        temperature=0.7
    )

    global _qa_engine
    _qa_engine = RetrievalQA.from_chain_type(
        llm=_llama2,
        chain_type='stuff',
        retriever=pine_vectorstore.as_retriever(search_kwargs={'k':2}),
        return_source_documents=True,
        chain_type_kwargs=chain_type_kwargs
    )
    print(f"Success")


def get_qaengine():
    if _qa_engine == None or _llama2 == None:
        raise Exception("Initialize the model first!")
    return _qa_engine

