import time, os

DIR_LOG = 'Log'

def createDir():
    if not os.path.exists(DIR_LOG):
        os.makedirs(DIR_LOG)
    
def Loger(site, dataServer):
    createDir()
    url = site.split('//')[1]
    domain = url.split('/')[0]
    timeLog = time.strftime("Time: %H-%M-%S  Date: %d/%m/%Y")
    
    formatDataList = []
    for key, value in dataServer.items():
        formatDataList.append(f"{key}: {value}")
    formatData = '\n'.join(formatDataList)

    with open(f'{DIR_LOG}/{domain}.txt', 'w') as file:
        write = file.write(f'{timeLog}\n\n{site}\n\n{formatData}\n')
