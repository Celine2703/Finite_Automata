import information as info

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

def determinization(dico, init, final, alphabet):
    #create a new dictionnary
    new_dico = []
    new_init = []
    new_final = []
    #add the initial state
    new_dico.append({})
    new_init.append(1)
#si l un des etat init final alors final
    new_final.append(0)
    for lettre in alphabet:
        new_dico[0][lettre] = []
    #add the transitions
    for state in range(len(dico)):
        for lettre in alphabet:
            if (init[state] == 1):
                if (dico[state][lettre] != [-1]):
                    for transition in dico[state][lettre]:
                        if (transition not in new_dico[0][lettre]):
                            new_dico[0][lettre].append(transition)

    ###################################################################
    #add the new states
    for state in range(len(new_dico)):
        for lettre in alphabet:
            if (new_dico[state][lettre] == []):
                new_dico.append({})
                new_init.append(0)
                new_final.append(0)
                for lettre in alphabet:
                    new_dico[len(new_dico) - 1][lettre] = []
                new_dico[state][lettre] = [len(new_dico) - 1]
    #add the transitions
    for state in range(len(new_dico)):
        for lettre in alphabet:
            for transition in new_dico[state][lettre]:
                if (transition not in new_dico[state][lettre]):
                    new_dico[state][lettre].append(transition)
    #add the final states
    for state in range(len(new_dico)):
        for transition in new_dico[state][alphabet[0]]:
            if (final[transition] == 1):
                new_final[state] = 1
    #################################################################################

    return new_dico, new_init, new_final

def minimization(dico, init, final, alphabet):

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