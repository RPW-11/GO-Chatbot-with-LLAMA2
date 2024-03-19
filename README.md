# GO-Chatbot-with-LLAMA2

### To start the app, run the following code

#### 1. Set up a python virtual environment.
```bash
python -m venv .venv
```
Activate the virtual environment
```bash
source .venv/bin/activate
```

#### 2. Run the setup script.
Then run `setup.sh`
```bash
bash setup.sh
```

#### 3. Fill the created environment file.
Open the `.env` file and fill in the required informations. The project uses Pinecone to store the data. You can fill your pinecone credentials (API_KEY, ENV NAME, etc.) here. See `.env.example` for a better understanding.
```ini
PINECONE_API_KE=XXXXXXXXXXXXXXX
PINECONE_API_ENV=XXXXXXXXXXXXXX
```

#### 4. Run the program.
Copy and paste this command in your terminal. Make sure you are in the root directory of this project.
```bash
python app/app.py
```

