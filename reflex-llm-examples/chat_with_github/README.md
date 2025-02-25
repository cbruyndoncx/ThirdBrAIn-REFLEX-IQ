# Chat with Github  

Chat with Github is an LLM app that utilizes **Retrieval Augmented Generation (RAG)** to enable meaningful interaction with Github Readme files. Powered by **Llama 3.2** running locally, the app provides accurate answers to your questions based on the Github Repo.  

---

## Getting Started  

### 1. Clone the Repository  
Clone the GitHub repository to your local machine:  
```bash  
git clone https://github.com/reflex-dev/reflex-llm-examples.git  
cd reflex-llm-examples/chat_with_github  
```  

### 2. Install Dependencies  
Install the required dependencies:  
```bash  
pip install -r requirements.txt
```

### 3. Get your GitHub Access Token
Get your GitHub [Personal Access Token](https://docs.github.com/en/enterprise-server@3.6/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token) with the necessary permissions and set it as environment variable to access any GitHub repository.

### 4. Pull and Run Llama 3.2 Using Ollama  
Download and set up the Llama 3.2 model locally:  
```bash  
ollama pull llama3.2  
```  

### 5. Run the Reflex App  
Run the application to start chatting with your PDF:  
```bash  
reflex run  
```  
