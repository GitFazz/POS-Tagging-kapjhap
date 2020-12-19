import numpy as np

fp = open("dataset.txt","r")

#ifp = open("input.txt","a")
#ofp = open("output.txt","a")

X = []
Y = []

while True:
    line = fp.readline()
    if not line: break

    words = line.split(" ")

    X_sentence = []
    Y_sentence = []

    for w in words:
        com = w.split("\\")
        X_sentence.append(com[0])
        Y_sentence.append( com[1].split(".",2)[0] )

    #ifp.write(','.join(X_sentence))
    #ofp.write(','.join(Y_sentence))
    
            
    

fp.close()