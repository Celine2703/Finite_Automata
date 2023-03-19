def is_standard(dico, init, final, alphabet):
    initstate = -1
    #test if there is only one initial state
    for i in range(len(init)):
        if init[i] != 0:
            if initstate == -1:
                initstate = i
            else:
                print("Not standard: more than one initial state")
                return False
    #test if there is a transition to the initial state
    for i in range(len(dico)):
        for j in range(len(alphabet)):
            for k in range(len(dico[i][alphabet[j]])):
                if dico[i][alphabet[j]][k] == initstate:
                    print("Not standard: transition to initial state")
                    return False
    return True

def is_deterministic(dico, init, final, alphabet):
    initstate = -1
    #test if there is only one initial state
    for i in range(len(init)):
        if init[i] != 0:
            if initstate == -1:
                initstate = i
            else:
                print("Not deterministic: more than one initial state")
                return False
    #test if there is more than one transition for a letter
    for i in range (len(dico)):
        for j in range(len(alphabet)):
            if len(dico[i][alphabet[j]]) > 1:
                print("Not deterministic: more than one transition for letter '", alphabet[j], "' in state", i)
                return False
    return True

def is_complete(dico, init, final, alphabet):
    for i in range(len(dico)):
        for j in range(len(alphabet)):
            if dico[i][alphabet[j]] == -1:
                print("Not complete: transition to nowhere")
                return False
    return True