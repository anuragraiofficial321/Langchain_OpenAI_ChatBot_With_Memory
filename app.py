from flask import Flask, render_template, jsonify, request
from api_key import private_key
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)


app = Flask(__name__)

llm = ChatOpenAI(temperature=0, openai_api_key=private_key, model="gpt-3.5-turbo")

# for hr

# Prompt
hr_prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a nice chatbot having a conversation with Human Resources (HR) professionals and streamline tasks for Human Resources (HR) professionals. As a sophisticated chatbot, your goal is to provide efficient assistance in various HR-related domains. Recognize the professional context and offer personalized responses to meet the unique needs of HR professionals. Prioritize clarity, security, and a seamless user experience in your design."
        ),
        # The `variable_name` here is what must align with memory
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
)

# hr_memory = ConversationBufferMemory(memory_key="chat_history",max_token_limit=1000, return_messages=True)
hr_memory = ConversationSummaryBufferMemory(
    llm=llm, return_messages=True, max_token_limit=1000, memory_key="chat_history"
)
hr_conversation = LLMChain(llm=llm, prompt=hr_prompt, verbose=True, memory=hr_memory)


# Prompt
hr_prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a nice chatbot having a conversation with Human Resources (HR) professionals and streamline tasks for Human Resources (HR) professionals. As a sophisticated chatbot, your goal is to provide efficient assistance in various HR-related domains. Recognize the professional context and offer personalized responses to meet the unique needs of HR professionals. Prioritize clarity, security, and a seamless user experience in your design."
        ),
        # The `variable_name` here is what must align with memory
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
)

# hr_memory = ConversationBufferMemory(memory_key="chat_history",max_token_limit=1000, return_messages=True)
hr_memory = ConversationSummaryBufferMemory(
    llm=llm, return_messages=True, max_token_limit=1000, memory_key="chat_history"
)
hr_conversation = LLMChain(llm=llm, prompt=hr_prompt, verbose=True, memory=hr_memory)


# Prompt
hr_prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a nice chatbot having a conversation with Human Resources (HR) professionals and streamline tasks for Human Resources (HR) professionals. As a sophisticated chatbot, your goal is to provide efficient assistance in various HR-related domains. Recognize the professional context and offer personalized responses to meet the unique needs of HR professionals. Prioritize clarity, security, and a seamless user experience in your design."
        ),
        # The `variable_name` here is what must align with memory
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}"),
    ]
)

# hr_memory = ConversationBufferMemory(memory_key="chat_history",max_token_limit=1000, return_messages=True)
hr_memory = ConversationSummaryBufferMemory(
    llm=llm, return_messages=True, max_token_limit=1000, memory_key="chat_history"
)
hr_conversation = LLMChain(llm=llm, prompt=hr_prompt, verbose=True, memory=hr_memory)


@app.route("/")
def chatbot():
    return render_template("home_page.html")


@app.route("/developer")
def developer():
    return "developer"


@app.route("/hr")
def hr():
    return "hr"


@app.route("/business_coach")
def business_coach():
    return "business_coach"


@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["user_message"]

    answer = hr_conversation({"question": f"{user_message}"})
    bot_response = answer["text"]

    return jsonify({"bot_response": bot_response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
