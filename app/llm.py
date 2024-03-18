from langchain.llms.llamacpp import LlamaCpp
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from constants import PROMP_TEMPLATE, TEMPLATE_INPUT_VARIABLES
from vector_store import pine_vectorstore


prompt_template = PromptTemplate(template=PROMP_TEMPLATE, input_variables=TEMPLATE_INPUT_VARIABLES)
chain_type_kwargs = {'prompt':prompt_template}

llama2 = LlamaCpp(
    model_path='models/llama-2.gguf',
    n_gpu_layers=-1,
    n_batch=256,
    verbose=False
)

qa_engine = RetrievalQA.from_chain_type(
    llm=llama2,
    chain_type='stuff',
    retriever=pine_vectorstore.as_retriever(search_kwargs={'k':2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

