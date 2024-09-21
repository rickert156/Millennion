import random
from utils.userAgentList import userAgentList
def head():
    list_length = len(userAgentList)
    selectAgent = random.randint(0, list_length)
    Agent = userAgentList[selectAgent]
    headers = {'User-Agent':Agent}
    return headers


#number_agent = 0
#for agent in userAgentList:
#    number_agent+=1
#    print(f'[{number_agent}] {agent}\n')
