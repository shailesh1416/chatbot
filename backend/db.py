import sqlite3
import datetime

def get_all_keys():
   key_list={}
   conn = sqlite3.connect('chat.db')
   data = conn.execute("select key,reply_id from keyResponseMap;"); 
   for key,id in data:  
      key_list[key]=id
   conn.close()
   return key_list

def get_response(key):
   conn = sqlite3.connect('chat.db')
   data = conn.execute("select reply from response where id="+str(key)+";")
   response = data.fetchone()[0]
   conn.close()
   return response

# save chat ID function
def saveChatId(user):
   conn = sqlite3.connect('chat.db')
   a = conn.execute(f"INSERT INTO chat (username,timestamp) values({str(user)},{datetime.datetime.now().timestamp()});")
   lastid = a.lastrowid
   conn.commit()
   conn.close()
   return lastid 

# save chat Title
def saveTitle(chatid,title):
   try:
      conn = sqlite3.connect('chat.db')
      conn.execute("UPDATE chat  SET title=? WHERE ID=?",(title,chatid))
      conn.commit()
      conn.close()
      return True
   except Exception as e:
      print("err",e)
      conn.close()
      return False

   
# save chat ID function
def saveChat(chatid,request,reply):
   try:
      conn = sqlite3.connect('chat.db')
      result=conn.execute("INSERT INTO chatdetails (chatid, request,reply,timestamp) values(?,?,?,?)",(chatid,request,reply,str(datetime.datetime.now().timestamp())))
      print(result.lastrowid)
      conn.commit()
      conn.close()
      return True 
   except Exception as e:
      print("err",e)
      conn.close()
      return False

def getChatHistory(userId):
   try:
      conn = sqlite3.connect('chat.db')
      result=conn.execute("SELECT * from chat where username=? ORDER BY timestamp DESC",(userId))
      history =[]
      for id,username,title,timestamp in result:  
         history.append({'id':id,'title':title,'timestamp':timestamp})
      conn.close()
      return history
   except Exception as e:
      print("err",e)
      conn.close()
      return False

      

def displayChatDetails(chatId):
   try:
      conn = sqlite3.connect('chat.db')
      result=conn.execute("SELECT chatid,request,reply,timestamp from chatdetails where chatid=? ",(chatId,))
      chatDetails =[]
      for chatid,request,reply,timestamp in result:  
         chatDetails.append({'id':chatid,'request':request,'reply':reply,'timestamp':timestamp})
      conn.close()
      return chatDetails
   except Exception as e:
      print("err",e)
      conn.close()
      return False



def registerUser(email,password):
   try:
      conn = sqlite3.connect('chat.db')
      # check if user already exist---> Pick here
      query = conn.execute("")
      # result=conn.execute("INSERT INTO chatdetails (chatid, request,reply,timestamp) values(?,?,?,?)",(chatid,request,reply,str(datetime.datetime.now().timestamp())))
      print(result.lastrowid)
      conn.commit()
      conn.close()
      return True 
   except Exception as e:
      print("err",e)
      conn.close()
      return False