from langchain.llms.llamacpp import LlamaCpp
from langchain_core.runnables import RunnablePassthrough
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
    )

    global _qa_engine
    _qa_engine = (
        { "context": pine_vectorstore.as_retriever(), "question": RunnablePassthrough()  }
        | prompt_template
        | _llama2
    )
    print(f"Success")


def get_qaengine():
    if _qa_engine == None or _llama2 == None:
        raise Exception("Error in initializing the LLM, Have you initialized the model?")
    return _qa_engine

