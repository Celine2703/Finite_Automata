import information as info
import display as disp
import bisect

def standardization(dico, init, final, alphabet, traduction):
    string = []
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
                if (state not in string):
                    string.append(state)
                    string = sorted(string)
                if (dico[state][lettre] != [-1]):
                    if (dico[len(dico) - 1][lettre] == [-1]):
                        dico[len(dico) - 1][lettre] = []
                    for transition in dico[state][lettre]:
                        if (transition not in dico[len(dico) - 1][lettre]):
                            dico[len(dico) - 1][lettre].append(transition)
                            dico[len(dico) - 1][lettre] = sorted(dico[len(dico) - 1][lettre])
                          
    for i in range(len(init) - 1):
        init[i] = 0
    if (len(string) > 1):
        traduction[str(string)] = len(dico) - 1
    return traduction

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

def init_determinization(dico, init, final, alphabet, traduction):
    traduction = {}
    if (multiples_entry(dico, init, final, alphabet)):
        #add a new state
        if (info.if_empty_word(dico, init, final, alphabet)):
            final.append(1)
        else:
            final.append(0)
        init.append(1)
        dico.append({})

def determinization(dico, init, final, alphabet, traduction):
    if (multiples_entry(dico, init, final, alphabet)):
        traduction = standardization(dico, init, final, alphabet, traduction)
    # print ("traduction = ", traduction)
    for state in dico:
        for lettre in alphabet:
            composedstate = findtraduction(traduction, state[lettre])
            print("composedstate = ", composedstate,"\n\n")
            if (len(composedstate) > 1):
                if (traduction.get(str(composedstate)) == None):
                    dico.append({})
                    init.append(0)
                    if (info.is_final_state(final,  composedstate)):
                        final.append(1)
                    else:
                        final.append(0)
                    traduction[str(composedstate)] = len(dico) - 1
                    for elem in alphabet:
                        find_new_states(dico, composedstate, elem)
                # print ("state[lettre] = ", state[lettre], "traduction = ", traduction.get(str(state[lettre])))
                state[lettre] = [traduction[str(composedstate)]]
    # for state in dico:
    #     for lettre in alphabet:
    #         if (len(state[lettre]) > 1):
    #             #print("state[lettre] = ", state[lettre], "traduction = ", traduction.get(str(state[lettre])))
    #             if (traduction.get(str(state[lettre])) == None): #if the state state[lettre] is not in the traduction dictionnary
    #                 dico.append({})
    #                 init.append(0)
    #                 if (info.is_final_state(final, state[lettre])):
    #                     final.append(1)
    #                 else:
    #                     final.append(0)
    #                 traduction[str(state[lettre])] = len(dico) - 1 #create a new state state[lettre] in the traduction dictionnary and give it the name len(dico) - 1 = the index of the new state in dico
    #                 #print(state[lettre])
    #                 for elem in alphabet:
    #                     find_new_states(dico, state[lettre], elem)
    #             state[lettre] = [traduction[str(state[lettre])]]
    #             print("traduction = ", traduction)
    # print ("dict = ", dico)
    return traduction

def findtraduction(traduction ,transition):
    out = []
    ok = 1
    
    print ("transition = ", transition)
    for i in transition:
        if (disp.get_key(i, traduction) != False):
            ok = 0
            # print("CELINE disp.get_key(i, traduction) = ", disp.get_key(i, traduction))
            tmp = disp.get_key(i, traduction)
            s = tmp.strip('[]')  # supprimer les crochets du début et de la fin de la chaîne
            lst = [int(x) for x in s.split(',')]
            out = out + lst
            # print (" =",tmp)
        else:
           out.append(i)
    out = list(set(out))
    out.sort()
    return out


def find_new_states(dico, transition, elem):
    dico[len(dico) - 1][elem] = []
    for i in transition:
        for state in dico[i][elem]:
            if (state not in dico[len(dico) - 1][elem] and state != -1):
                dico[len(dico) - 1][elem].append(state)
        # if(i not in dico[len(dico) - 1][elem] and dico[i][elem] != [-1]):
        #     dico[len(dico) - 1][elem] += dico[i][elem]
    dico[len(dico) - 1][elem] = sorted(dico[len(dico) - 1][elem])
    if (dico[len(dico) - 1][elem] == []):
        dico[len(dico) - 1][elem] = [-1]
    
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