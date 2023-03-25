import importlib.util
# Import Int2-6-information
info_spec = importlib.util.spec_from_file_location("Int2-6-information", "./Int2-6-information.py")
info = importlib.util.module_from_spec(info_spec)
info_spec.loader.exec_module(info)

# Import Int2-6-display
disp_spec = importlib.util.spec_from_file_location("Int2-6-display", "./Int2-6-display.py")
disp = importlib.util.module_from_spec(disp_spec)
disp_spec.loader.exec_module(disp)
# import bisect

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

def init_determinization(dico, init, final, alphabet, traduction):
    traduction = {}
    new_dico = []
    new_init = []
    new_final = []
    traduction = {}
    trueindex = {}
        #add a new state
    if (info.if_empty_word(dico, init, final, alphabet)):
        new_final.append(1)
    else:
        new_final.append(0)
    new_init.append(1)
    new_dico.append({})
    list_init = list_init_states(init)
    if (alphabet[0] == '€'):
        list_init = add_empty_list(dico, list_init)
        traduction[str(list_init)] = 0
        trueindex[0] = 0

    else :
        list_init.sort()
        traduction[str(list_init)] = list_init
        trueindex[str(list_init)] = 0        
    
    for state in list_init:
        for lettre in alphabet:
            if (lettre == '€'):
                continue
            if (dico[state][lettre] != [-1]):
                if (new_dico[0].get(lettre) == None):
                    new_dico[0][lettre] = []
                for transition in dico[state][lettre]:
                    if (transition not in new_dico[0][lettre] and transition != -1):
                        new_dico[0][lettre].append(transition)
                        new_dico[0][lettre].sort()
    return traduction, new_dico, new_init, new_final, trueindex

def list_init_states(init):
    list_init = []
    for i in range(len(init)):
        if (init[i] == 1):
            list_init.append(i)
    return list_init

def add_empty_list(dico, list_prime):
    added = 0
    for elem in list_prime:
        if (elem not in dico[elem]['€']):
            for state in dico[elem]['€']:
                if (state not in list_prime and state != -1):
                    list_prime.append(state)
                    added = 1
                    list_prime = list(set(list_prime))
    list_prime = sorted(list_prime)
    if (added == 1):
        return (add_empty_list(dico, list_prime))
    return list_prime

def determinization2(dico, init, final, alphabet, traduction):
    traduction, new_dico, new_init, new_final , trueindex= init_determinization(dico, init, final, alphabet, traduction)
    for state in new_dico:
        for lettre in alphabet :
            if (lettre == '€'):
                continue
            for transition in state[lettre]:
                if transition == -1:
                    continue
                list_new_state = [transition]
                if (alphabet[0] == '€'):
                    list_new_state = add_empty_list(dico, list_new_state)
                if (str(list_new_state) not in traduction.keys() and trueindex.get(str(state[lettre])) == None):
                    traduction[str(list_new_state)] = transition
                if(str(state[lettre]) not in trueindex.keys()):
                    trueindex[str(state[lettre])] = len(new_dico)
                    new_dico.append({'a': [-1], 'b': [-1]})
                    new_init.append(0)
                    if (alphabet[0] == '€' and info.is_final_state(final, list_new_state) == True):
                        new_final.append(1)
                    elif (alphabet[0] != '€' and info.is_final_state(final, state[lettre]) == True):
                        new_final.append(1)
                    else:
                        new_final.append(0)
                for newletter in alphabet:
                    if (newletter == '€'):
                        continue
        
                    if (new_dico[(trueindex[str(state[lettre])])].get(newletter) == None or new_dico[(trueindex[str(state[lettre])])][newletter] == [-1]):
                        new_dico[(trueindex[str(state[lettre])])][newletter] = []
                    
                    if (list_transi(list_new_state, newletter, dico) != [-1] and list_transi(list_new_state, newletter, dico) not in new_dico[(trueindex[str(state[lettre])])][newletter]):
                        new_dico[(trueindex[str(state[lettre])])][newletter] += list_transi(list_new_state, newletter, dico)
                        state[lettre] = list (set(state[lettre]))
                        state[lettre].sort()
                        new_dico[(trueindex[str(state[lettre])])][newletter] = list(set(new_dico[(trueindex[str(state[lettre])])][newletter]))
                       
                    if (new_dico[(trueindex[str(state[lettre])])][newletter] == []):
                        new_dico[(trueindex[str(state[lettre])])][newletter] = [-1]
    new_alphabet = []
    for letter in alphabet:
        if (letter != '€'):
            new_alphabet.append(letter)
    build_automaton(new_dico, new_init, new_final, new_alphabet, traduction, trueindex)
    return new_dico, new_init, new_final, new_alphabet, traduction, trueindex

def list_transi (list_states, letter, dico):
    ret = []
    for i in list_states:
        for j in dico[i][letter]:
            if (j not in ret and j != -1):
                ret.append(j)
                ret.sort()
    if ret == []:
        ret.append(-1)
    return ret

def findtraduction(traduction ,transition):
    out = []
    for i in transition:
        if (disp.get_key(i, traduction) != False):
            tmp = disp.get_key(i, traduction)
            s = tmp.strip('[]')  # supprimer les crochets du début et de la fin de la chaîne
            lst = [int(x) for x in s.split(',')]
            out = out + lst
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
    groups = []
    for isfinal in final:
        if isfinal == 0:
            groups.append(1)
        else:
            groups.append(-1)
    print(groups)
    pattern = []
    for i in range(len(dico)):
        pattern.append([])
        for lettre in alphabet:
            print(dico)
            if dico[i].get(lettre) != -1:
                for j in range (len(dico[i].get(lettre))):
                    if final[dico[i].get(lettre)[j]] == 0:
                        pattern[i].append(0)
                    elif final[dico[i].get(lettre)[j]] == 1:
                        pattern[i].append(1)
    print(pattern)
    for i in range(len(groups)):
        if groups[i] == -1:
            groups[i] -= i
        else:
            groups[i] += i
    print(groups)
    for j in range(len(groups)):
        if groups[j] < 0:
            default_pattern = pattern[j]
            for i in range(len(pattern)):
                if pattern[i] == default_pattern:
                    if groups[i] < 0:
                        groups[i] = groups[j]
        if groups[j] > 0:
            default_pattern = pattern[j]
            for i in range(len(pattern)):
                if pattern[i] == default_pattern:
                    if groups[i] > 0:
                        groups[i] = groups[j]
    print(groups)
    print("minimization")
    return dico, init, final


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

def build_automaton(dico, init, final, alphabet, traduction, trueindex):
    for state in dico:
        # replace the state that is a list by the index of the state in the dico
        for lettre in alphabet:
            if str(state[lettre]) in traduction:
                state[lettre] = [traduction[str(state[lettre])]]
            if (str(state[lettre]) in trueindex):
                state[lettre] = [trueindex[str(state[lettre])]]