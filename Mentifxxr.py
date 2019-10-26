import json
import requests
from threading import Thread
import datetime


def getNewID():
    x = json.loads(requests.post('https://www.menti.com/core/identifier').text)
    return x["identifier"]

def getInfo(pin, err=True):
    x = requests.get('https://www.menti.com/core/objects/vote_ids/' + str(pin)).text
    try:
        (json.loads(x))["id"]
        return json.loads(x)
    except KeyError:
        if err == True:
            print("ERR: No such code")
            exit()
        return False

def printInfo(info):
    i = 0
    activeid = info["pace"]["active"]
    print("Name:\t\t", info["name"])
    print("id:\t\t", info["id"])
    print("Pin:\t\t", info["vote_id"])
    print("last update:\t", datetime.datetime.strptime((info["updated_at"]).replace("+00:00", ""), '%Y-%m-%dT%H:%M:%S'))
    print("No. questions:\t", len(info["questions"]))
    print("\nQuestion Specific:")
    for x in info["questions"]:
        i += 1
        if x["id"] == activeid:
            print("Question Nr:\t", i)
            print("Type:\t\t", x["type"])
            if (x["type"] == "wordcloud") | (x["type"] == "open"):
                print("Max Enteries:\t", x["max_nb_words"])

            elif (x["type"] == "choices") | (x["type"] == "choices_images") | (x["type"] == "winner") | (x["type"] == "ranking") | (x["type"] == "scales"):
                print("Choices:")
                for y in x["choices"]:
                    print("\tNo.:\t", y["position"] + 1)
                    print("\tlabel:\t", y["label"])
                    print("\tid:\t", y["id"], "\n")
            print("Question name:\t", x["question"])
            print("Public Key:\t", x["public_key"])

def listInfo(info):
    l = []
    i = 0
    activeid = info["pace"]["active"]
    l.append("Name: " + info["name"])
    l.append("id: " + info["id"])
    l.append("Pin: " + str(info["vote_id"]))
    l.append("last update: " + str(datetime.datetime.strptime((info["updated_at"]).replace("+00:00", ""), '%Y-%m-%dT%H:%M:%S')))
    l.append("No. questions: " + str(len(info["questions"])))
    l.append("Question Specific:")
    for x in info["questions"]:
        i += 1
        if x["id"] == activeid:
            l.append("Question Nr: " + str(i))
            l.append("Type: "+ x["type"])
            if (x["type"] == "wordcloud") | (x["type"] == "open"):
                l.append("Max Enteries: "+ str(x["max_nb_words"]))

            elif (x["type"] == "choices") | (x["type"] == "choices_images") | (x["type"] == "winner") | (x["type"] == "ranking") | (x["type"] == "scales"):
                l.append("Choices:")
                for y in x["choices"]:
                    l.append("  No.: "+ str(y["position"] + 1))
                    l.append("  label: "+ y["label"])
                    l.append("  id: "+ str(y["id"]) + "\n")
            l.append("  Question name: "+ str(x["question"]))
            l.append("  Public Key: "+ str(x["public_key"]))
    return l

def getActiveId(info):
    return info["pace"]["active"]

def getActiveQuestionid(info):
    activeid = info["pace"]["active"]
    for x in info["questions"]:
        if x["id"] == activeid:
            return x["public_key"]

def getActiveQuestionType(info):
    activeid = info["pace"]["active"]
    for x in info["questions"]:
        if x["id"] == activeid:
            return x["type"]

def getActiveQuestion(info):
    activeid = info["pace"]["active"]
    for x in info["questions"]:
        if x["id"] == activeid:
            return x["choices"]
def getActiveQuestionMinMax(info):
    activeid = info["pace"]["active"]
    for x in info["questions"]:
        if x["id"] == activeid:
            return x["range"]

def awnser(Questionid, type, ID, info, awnser):

    t = getActiveQuestionType(info)
    u = getActiveQuestion(info)
    #print("choices:", u)
    if (t == "choices") | (t == "choices_images") | (t == "winner") | (t == "ranking"):
        # cross reference
        for x in u:
            if x["position"] + 1 == awnser:
                awnser = [(x["id"])]
                

    data = {"question_type":type,"vote":awnser}
    #print(data)

    headers = {
    "x-identifier":ID,
    "cookie": "identifier1=" + ID,
    "Content-Type":"application/json",
    }
    
    requests.post(url = 'https://www.menti.com/core/votes/' + Questionid, data = json.dumps(data), headers=headers)

def spamm(word):
    ids = []
    idtred = []

    def addnewidtolist():
        global ids
        ids.append(Mentifxxr.getNewID())

    for x in range(1):
        t1 = Thread(target = addnewidtolist)
        idtred.append(t1)


"""
try:
    pin = 569245
    word = "small_Brain"

    pin = input("Input Pin\n> ")
    y = getInfo(pin)
    
    word = input("What to say\n> ").replace(" ","_")
    times = int(input("Times\n> "))
    
    printInfo(y)
    q = getActiveQuestion(y)
    for x in y["questions"]:
        if x["id"] == q:
            t = x["type"]
            print(x["type"])
    t = "wordcloud"

    r = range(times)

    for x in r:
        newid = getNewID()
        awnser(q, t, newid, word)
        print("\r", x+1, "/", len(r), end="\r")
        

except KeyboardInterrupt:
    print("Interrupt detected")

"""