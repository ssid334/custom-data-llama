
from langchain.chains.router import MultiRetrievalQAChain
from langchain.llms import LlamaCpp

from langchain.embeddings import LlamaCppEmbeddings
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import gradio

N_CTX = 3000
N_THREADS = 8

#inputData = TextLoader('/opt/data/someinput.txt').load_and_split()

from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("/opt/data/someinput.pdf")
inputData = loader.load_and_split()

vectorstore = Chroma.from_documents(documents=inputData, embedding=LlamaCppEmbeddings(model_path='/opt/llama.bin', n_ctx=N_CTX, n_threads=N_THREADS))

llm = LlamaCpp(model_path='/opt/llama.bin', n_ctx=N_CTX, n_threads=N_THREADS)
qa_chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())


def get_response(message, history):
    resp = qa_chain({"query": message})
    return resp.get('result', 'problem retrieving response')

webui = gradio.ChatInterface(get_response)
webui.launch(server_name="0.0.0.0", server_port=8080, auth=('llama', 'supersecret123'))
