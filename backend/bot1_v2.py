from flask import Flask, request, jsonify
import json

app = Flask(__name__)

keys_list={
    "courses":["fees","course","excel","tally","subjects"],
    "address":["address","location","place","where"],
    "contact":["mobile","phone","contact","whatsapp"],
    "placement":["job","placement","guarantee"],
    "refund":["refund","moneyback","return"],
    "owner":["owner","malik","teacher"],
    "faculty":["teachers","faculty","teacher"],
    "website":["website","site","webpage"]
}


qna = {
    "courses"   : "Tally - 11800\nBasic Computers - 6000\nExcel For Commerce - 3000",
    "where"     : "Navapur Road Boisar, 401501",
    "address"   : "Navapur Road Boisar, 401501",
    "fees"      : "Tally - 11800\nBasic Computers - 6000\nExcel For Commerce - 3000",
    "contact"   : "Mob : 1122334455\n Office : 3344552266",
    "timing"    : "Everyday, Moring 8 AM to Evening 8 PM \n Sunday Closed",
    "owner"     : "Abhijit Joshi",
    "whatsapp"  : "Whatsapp Number : 0099887766",
    "distance"  : "Just 10 min walking distance from Boisar station",
    "quality"   : "Very nice quality",
    "placement" : "We dont guarantee Placement, But knowledge is guaranteed",
    "job"       : "We dont guarantee Placement, But knowledge is guaranteed",
    "landmark"  : "Near Vikas Hospital\n or Search Tally Boisar in google",
    "website"   : "www.tallyboisar.com",
    "info"      : "Please visit: www.tallyboisar.com",
    "computer"  : "Must for every beginner who want to work on computers",
    "excel"     : "Must for every office and day to day operations",
    "refund"    : "Once taken addmission we do not refund(Conditions apply: we can consider on case basis)",
    "python"    : "Very helpful for learning coding skills and developing problem solving skills ",

    }


def find_answer(string):
    if string=='X':
        return f"Thanks for visiting us, for more info visit www.tallyboisar.com, \n Have a nice day, bye😊 "
    global qna,keys_list
    keys = string.lower().split()
    for key in keys:
        for k in keys_list:
            print(k)
            if key in keys_list[k]:
                return qna[k]
    return f"Your question is not clear to me, Try searching a different question😒😒😒 or visit www.tallyboisar.com"


@app.route('/getAnswer', methods=['GET'])
def get_answer():
    string = request.args.get("question")

    answer = find_answer(string)
    response = {"answer":answer}
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Tally academy Bot")
    app.run(port=5000)


