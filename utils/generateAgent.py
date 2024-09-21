import random
from utils.userAgentList import userAgentList
from utils.AcceptEncoding import AcceptEncoding

def head():
    Agent = randData(userAgentList)
    Accept_Encoding = randData(AcceptEncoding)
    headers = {
            'User-Agent':Agent,
            'Accept-Encoding':Accept_Encoding
            }
    return headers

def randData(listDate):
    list_length = len(listDate)
    selectDate = random.randint(0, list_length-1)
    data = listDate[selectDate]
    return data

