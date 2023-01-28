import sqlite3
import datetime,time
conn = sqlite3.connect('chat.db')

# creating table
# conn.execute('''CREATE TABLE chatdetails (ID INTEGER PRIMARY KEY AUTOINCREMENT, chatid TEXT NOT NULL,request TEXT NOT NULL,reply TEXT NOT NULL,timestamp TEXT NOT NULL, FOREIGN KEY (chatid) REFERENCES chat(ID));''')  

conn.execute('''CREATE TABLE chat (ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL,title TEXT ,timestamp TEXT NOT NULL, FOREIGN KEY (username) REFERENCES user(ID));''')  

# conn.execute('''CREATE TABLE user (ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL,password TEXT NOT NULL);''')  

# creating key-reply-map table
# conn.execute('''CREATE TABLE keyResponseMap (ID INT PRIMARY KEY NOT NULL, key TEXT NOT NULL, reply_id INTEGER, FOREIGN KEY (reply_id) REFERENCES response(id));''')  

# insert 
# conn.execute("INSERT INTO response (ID,reply) VALUES (16,'You are welcome😊, please visit, www.tallyacademy.com for more info')"); 

# conn.execute("INSERT INTO user (username,password) VALUES ('shailesh','shailesh123')"); 
# conn.execute("DROP TABLE chat"); 

# conn.execute("INSERT INTO keyResponseMap (ID,key,reply_id) VALUES (34, 'thank',16)"); 

# conn.execute('''CREATE TABLE keyResponseMap (ID INT PRIMARY KEY NOT NULL, key TEXT NOT NULL, reply_id INTEGER, FOREIGN KEY (reply_id) REFERENCES response(id));''')  

# update
# conn.execute("UPDATE keyResponseMap  SET reply_id=1 WHERE ID=10;"); 

# conn.execute('delete from chat')
# conn.execute('delete from chatdetails')
conn.commit() 
conn.close()

# data = conn.execute("select * from user"); 
# for row in data:  
#    print (row[0],'\t| ',row[1],"\t| ", row[2])

# print(datetime.datetime.now().date())
# print(datetime.datetime.now().time())

# print(datetime.datetime.now().timestamp())
# a =datetime.datetime.now().timestamp()

# print(datetime.datetime.fromtimestamp(a))





