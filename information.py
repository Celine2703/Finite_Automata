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
    for state in dico:
        for lettre in alphabet:
            for transition in state[lettre]:
                if transition == initstate:
                    print("Not standard: transition to initial state")
                    return False
    print("The automaton is standard")
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
        for lettre in alphabet:
            if len(dico[i][lettre]) > 1:
                print("Not deterministic: more than one transition for letter '", lettre, "' in state", i)
                return False
    print("The automaton is deterministic")
    return True

def is_complete(dico, init, final, alphabet):
    for state in dico:
        for lettre in alphabet:
            if state[lettre] == [-1]:
                print("Not complete: transition to nowhere")
                return False
    print("The automaton is complete")
    return True