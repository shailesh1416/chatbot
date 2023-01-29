from flask import Flask, request, jsonify
import sqlite3
from db import get_all_keys,get_response,saveChatId,saveChat,getChatHistory,saveTitle,displayChatDetails
import uuid

app = Flask(__name__)


def find_answer(string):
    if string=='X':
        return f"Thanks for visiting us,\n Have a nice day, bye😊 "
    keys = string.lower().split()
    db_keys = get_all_keys()

    for key in keys:
        if key in db_keys.keys():
            return get_response(db_keys[key])
    return get_response(db_keys['err'])

# handle request from client
@app.route('/getAnswer', methods=['GET'])
def get_answer():
    try:
        query = request.args.get("question")
        chatId = request.args.get("chat_id")
        # print("CHat ID : ",chatId)
        answer = find_answer(query)
        saveChat(chatId,query,answer)
        response = {"answer":answer}
        response = jsonify(response)
        response.headers.add('Access-Control-Allow-Origin', '*') 
        return response
    except:
        return False

@app.route('/getNewChatId', methods=['GET'])
def getNewChatId():
    user = request.args.get("userId")
    # global user
    newid = saveChatId(user)
    response = {"id":newid}
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*') 
    return response

@app.route('/saveChatTitle', methods=['GET'])
def saveChatTitle():
    title = request.args.get("title")
    # user = request.args.get("userId")
    chatId = request.args.get("chat_id")
    # global user
    newTitle = saveTitle(chatId,title)
    response = {"status":newTitle}
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*') 
    return response

@app.route('/getChatHistory', methods=['GET'])
def getChats():
    user = request.args.get("userId")
    # global user
    history = getChatHistory(user)
    response = {"history":history}
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*') 
    return response

@app.route('/displayChat', methods=['GET'])
def displayChat():
    chatId = request.args.get("chat_id")
    # global user
    chatDetails = displayChatDetails(chatId)
    response = {"chatDetails":chatDetails}
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*') 
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Tally academy Bot")
    app.run(port=5000)


