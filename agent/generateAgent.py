import random
from agent.UserAgentList import userAgentList
from agent.AcceptEncoding import AcceptEncoding
from agent.Accept import Accept
from agent.ContentType import ContentType
from agent.AcceptLanguage import AcceptLanguage

def head():
    Agent = randData(userAgentList)
    Accept_Encoding = randData(AcceptEncoding)
    headers = {
            'User-Agent':Agent,
            'Accept-Encoding':Accept_Encoding,
            'Connection':'keep-alive',
            'Accept-Language':AcceptLanguage,
            'Content-Type':ContentType,
            'Accept': Accept
            }
    return headers

def randData(listDate):
    list_length = len(listDate)
    selectDate = random.randint(0, list_length-1)
    data = listDate[selectDate]
    return data

