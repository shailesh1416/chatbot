print("Hello, WELCOME to TALLY ACADEMY 💻")
USER = input("What is your good name please.")
print(f"Hello {USER}")

qna = {
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
    keys = string.split()
    print(keys)
    for key in keys:
        if key in qna.keys():
            return qna[key]
    return f"Your question is not clear to me, Try searching a different question😒😒😒"

print(f"How can I help you {USER}?")

END_CHAT = False
while not END_CHAT:
    print("Type X to exit")
    user_question = input("Ask something :")
    if user_question=="X":
        print(f"Thanks {USER}, Do visit again,\n Have a nice day, bye😊 ")
        break
    answer = find_answer(user_question)
    print(f"Reply :{answer}")
print("=======Chat Ended=======")
