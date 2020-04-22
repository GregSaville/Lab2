def createMenu(option):
    tmp = ""; ct = 0
    for opt in option:
        tmp += str(ct) + ". " + opt +'\n'
        ct += 1 
    return tmp
