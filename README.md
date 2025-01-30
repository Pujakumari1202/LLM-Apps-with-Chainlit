## Create a ChatBot with LLMs and Chainlit

This is a simple chatbot that uses the OpenAI API to generate responses based on the user's input.



# How to run?
### STEPS:

### STEP 01- Create a conda environment after opening the repository

```bash
conda create --name chainlit python=3.9
```

```bash
conda activate chainlit
```


### STEP 02- install the requirements
```bash
python -m pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your OPENAI_API_KEY credentials as follows:

```ini
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
chainlit init
```
## To launch the chainlit server
```bash
chainlit run app.py
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- OpenAI
- GPT 3.5 turbo
- ChoromaDB

