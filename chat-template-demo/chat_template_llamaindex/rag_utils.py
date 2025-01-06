import os

from llama_index.core import VectorStoreIndex, ServiceContext
from llama_index.core.base.base_query_engine import BaseQueryEngine
from llama_index.llms.openai import OpenAI


from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


_query_engine: BaseQueryEngine

DATA_DIR = os.getenv("DATA_DIR", "data")


def load_remote_vector_store(data_dir: str = DATA_DIR):
    global _query_engine
    llm = OpenAI(model="gpt-4-0125-preview")
    service_context = ServiceContext.from_defaults(llm=llm)
    print(f"loading data from local: {data_dir}")
    documents = SimpleDirectoryReader(
        data_dir, required_exts=[".md", ".mdx"], recursive=True
    ).load_data()
    print(f"loaded {len(documents)}")
    loaded_index = VectorStoreIndex.from_documents(
        documents=documents, service_context=service_context
    )
    _query_engine = loaded_index.as_query_engine()


def get_engine():
    return _query_engine
