# Chat with PDF  

Chat with PDF is an LLM app that utilizes **Retrieval Augmented Generation (RAG)** to enable meaningful interaction with PDF files. Powered by **Llama 3.2** running locally, the app provides accurate answers to your questions based on the content of the uploaded PDF.  

---

## Features  
- **Upload PDF Documents:** Easily upload any PDF document to start querying.  
- **Interactive Q&A:** Ask questions about the content of the uploaded PDF.  
- **Accurate Answers:** Get precise responses using RAG and the Llama 3.2 model.  

---

## Getting Started  

### 1. Clone the Repository  
Clone the GitHub repository to your local machine:  
```bash  
git clone https://github.com/reflex-dev/reflex-llm-examples.git  
cd reflex-llm-examples/chat_with_pdf_locally  
```  

### 2. Install Dependencies  
Install the required dependencies:  
```bash  
pip install -r requirements.txt  
```  

### 3. Pull and Run Llama 3.2 Using Ollama  
Download and set up the Llama 3.2 model locally:  
```bash  
ollama pull llama3.2  
```  

### 4. Run the Reflex App  
Run the application to start chatting with your PDF:  
```bash  
reflex run  
```  