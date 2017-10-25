tokenList = {
    "coin":1*46,
    "x":0,
}

def getToken(token):
    file = open("teletoken.txt",'r')
    file.seek(tokenList[token])
    token = file.read()
    file.close()
    return token[:45]
