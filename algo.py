import information as info
import display as disp
import bisect

def standardization(dico, init, final, alphabet):
    #add a new state
    if (info.if_empty_word(dico, init, final, alphabet)):
        final.append(1)
    else:
        final.append(0)
    init.append(1)
    dico.append({})
    # add the transitions to the new state
    for lettre in alphabet:
        dico[len(dico) - 1][lettre] = [-1]
    for state in range(len(dico) - 1):
        for lettre in alphabet:
            if (init[state] == 1):
                if (dico[state][lettre] != [-1]):
                    if (dico[len(dico) - 1][lettre] == [-1]):
                        dico[len(dico) - 1][lettre] = []
                    for transition in dico[state][lettre]:
                        if (transition not in dico[len(dico) - 1][lettre]):
                            dico[len(dico) - 1][lettre].append(transition)
                            dico[len(dico) - 1][lettre] = sorted(dico[len(dico) - 1][lettre])
                          
    for i in range(len(init) - 1):
        init[i] = 0
    return dico, init, final

def completion(dico, init, final, alphabet):
    #add a new state
    dico.append({})
    init.append(0)
    final.append(0)
    # add the transitions frome the new state to the new state (think state)
    for lettre in alphabet:
        dico[len(dico) - 1][lettre] = [len(dico) - 1]
    # add the transitions to the new state
    for state in range(len(dico) - 1):
        for lettre in alphabet:
            if (dico[state][lettre] == [-1]):
                dico[state][lettre] = [len(dico) - 1]
    return dico, init, final

def multiples_entry(dico, init, final, alphabet):
    j=0
    for i in range(len(dico)):
        if (init[i] == 1):
            j+=1
            if (j>1):
                return True
    return False

def determinization(dico, init, final, alphabet):
    if (multiples_entry(dico, init, final, alphabet)):
        dico, init, final = standardization(dico, init, final, alphabet)
    traduction = {}
    for state in dico:
        for lettre in alphabet:
            if (len(state[lettre]) > 1):
                print("state[lettre] = ", state[lettre], "traduction = ", traduction.get(str(state[lettre])))
                if (traduction.get(str(state[lettre])) == None): #if the state state[lettre] is not in the traduction dictionnary
                    dico.append({})
                    init.append(0)
                    if (info.is_final_state(final, state[lettre])):
                        final.append(1)
                    else:
                        final.append(0)
                    traduction[str(state[lettre])] = len(dico) - 1 #create a new state state[lettre] in the traduction dictionnary and give it the name len(dico) - 1 = the index of the new state in dico
                    print(state[lettre])
                    for elem in alphabet:
                        find_new_states(dico, state[lettre], elem)
                state[lettre] = [traduction[str(state[lettre])]]
    return traduction

def find_new_states(dico, statlettre, elem):
    dico[len(dico) - 1][elem] = []
    for i in statlettre:
        dico[len(dico) - 1][elem] += dico[i][elem]
    dico[len(dico) - 1][elem] = sorted(dico[len(dico) - 1][elem])

def minimization(dico, init, final, alphabet):
    print("minimization")

def complementarisaton(dico, init, final, alphabet):
    for state in range(len(final)):
        if (final[state] == 1):
            final[state] = 0
        else:
            final[state] = 1
    return dico, init, final

def recognize_word(dico, init, final, alphabet, word):
    for lettre in word:
        if (lettre not in alphabet):
            return False
    for i in range(len(init)):
        if (init[i] == 1):
            state = i
            for lettre in word:
                if(dico[state][lettre] == [-1]):
                    return False
                else:
                    state = dico[state][lettre][0]
            if (final[state] == 1):
                return True
    else:
        return False