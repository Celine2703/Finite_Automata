# function that returns if the automaton recognizes the empty word (a state is initial and final)
def if_empty_word(dico, init, final, alphabet):
    for i in range(len(init)):
        if init[i] == 1 and final[i] == 1:
            return True
    return False

# fuction that returns if a state is final
def is_final_state(final, state):
    for i in state:
        if final[i] == 1:
            return True
    return False

# function that returns if the automaton is standard
def is_standard(dico, init, final, alphabet):
    initstate = -1
    #test if there is only one initial state
    for i in range(len(init)):
        if init[i] != 0:
            if initstate == -1:
                initstate = i
            else:
                return -2
    #test if there is a transition to the initial state
    for state in dico:
        for lettre in alphabet:
            for transition in state[lettre]:
                if transition == initstate:
                    return 0
    return -1

# function that returns if the automaton is deterministic
def is_deterministic(dico, init, final, alphabet):
    if ("€" in alphabet):
        return -3
    initstate = -1
    #test if there is only one initial state
    for i in range(len(init)):
        if init[i] != 0:
            if initstate == -1:
                initstate = i
            else:
                return -2
    #test if there is more than one transition for a letter
    for i in range (len(dico)):
        for lettre in alphabet:
            if len(dico[i][lettre]) > 1:
                return i
    return -1

# function that returns if the automaton is complete
def is_complete(dico, init, final, alphabet):
    if alphabet == []:
        return -1
    for i in range(len(dico)):
        for lettre in alphabet:
            if dico[i][lettre] == [-1]:
                return i
    return -1