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

def multiples_entry(dico, init, final, alphabet):
    j=0
    for i in range(len(dico)):
        if (init[i] == 1):
            j+=1
            if (j>1):
                return True
    return False

def traduction_new_states(dico, init, final, alphabet, index , state_to_translate, lettre):
    for i in state_to_translate:
        dico[index][lettre] += dico[i][lettre]

def determinization(dico, init, final, alphabet):
    if (multiples_entry(dico, init, final, alphabet)):
        dico, init, final = standardization(dico, init, final, alphabet)
    traduction = {}
    for state in dico:
        for lettre in alphabet:
            if (len(state[lettre]) > 1):
                if (traduction.get(str(state[lettre])) == None):
                    dico.append({})
                    traduction[str(state[lettre])] = len(dico) - 1 #create a new state state[lettre] in the traduction dictionnary and give it the name len(dico) - 1 = the index of the new state in dico
                    #to do append in init and final the new state
                    # to do changer la valeur des transitions du nouvel etats
                    for lettre in alphabet:
                        dico[len(dico) - 1][lettre] = [-1]
                else:
                    state[lettre] = traduction[str(state[lettre])]

                # for transition in state[lettre]:
                #     if (transition not in traduction):
                #         dico.append({})
                #         state[lettre] = dico.len() - 1
                #         traduction[transition] = dico.len() - 1
                #         for lettre in alphabet:
                #             dico[len(dico) - 1][lettre] = [-1]
                #     else:
                #         state[lettre] = traduction[transition]

"""
    #create a new dictionnary
    new_dico = dico
    new_init = []
    new_final = []
    #add the initial state
    new_dico.append({})
    new_init.append(1)
#si l un des etat init final alors final
    new_final.append(0)
    for lettre in alphabet:
        new_dico[0][lettre] = []
    
    1- on cree un dico traduction qui va permettre de connaitre l'etat du nouveau dico correspondant a la transition indetermine 
    2- si plusieurs etat initiaux on les met dans un etat init (voir standardisation)
    3 - on ajoute les transitions de l'ancien dico au nouveau
        3.1 - on parcour le dico
            si on trouve un transition indetermine (len(dico[state][lettre])>1)
                on regarde dans le dico traduction si on a deja cree un etat correspondant a cette transition
                    si non on cree un etat dans new_dico et on l'ajoute au dico traduction
                    si oui on ajoute l'etat correspondant a la transition dans new_dico
    

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

"""
    

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