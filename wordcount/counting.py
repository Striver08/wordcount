#par = "This is is the second time i am is doing time"
def counti(para):
    wordlist = para.split()
    #print(wordlist)
    wordlist.sort()
    dict1 = {}
    
    for word in wordlist:
        if word in dict1:
            dict1[word] += 1
        else:
            dict1[word] = 1

    return dict1

#freq = counti(par)
#print(type(freq))

