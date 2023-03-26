import copy
import time
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

# function for the standardization of an automaton : add a new initial state and add the transitions to the new state
def standardization(dico, init, final, alphabet, traduction):
    list_init = []
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
                if (state not in list_init):
                    list_init.append(state)
                    list_init = sorted(list_init)
                if (dico[state][lettre] != [-1]):
                    if (dico[len(dico) - 1][lettre] == [-1]):
                        dico[len(dico) - 1][lettre] = []
                    for transition in dico[state][lettre]:
                        if (transition not in dico[len(dico) - 1][lettre]):
                            dico[len(dico) - 1][lettre].append(transition)
                            dico[len(dico) - 1][lettre] = sorted(dico[len(dico) - 1][lettre])
    #the other states are not initial                     
    for i in range(len(init) - 1):
        init[i] = 0
    if (len(list_init) > 1):
        traduction[str(list_init)] = len(dico) - 1
    return traduction

# fuction that complete an automaton : add a new think state and add the transitions to it
def completion(dico, init, final, alphabet):
    #add a new state
    dico.append({})
    init.append(0)
    final.append(0)
    # add the transitions frome the new state to the new state (think state)
    for lettre in alphabet:
        dico[len(dico) - 1][lettre] = [len(dico) - 1]
    # add the transitions to the new think state
    for state in range(len(dico) - 1):
        for lettre in alphabet:
            if (dico[state][lettre] == [-1]):
                dico[state][lettre] = [len(dico) - 1]
    return dico, init, final

# fuction that create the initial state of the deterministic automaton
def init_determinization(dico, init, final, alphabet, traduction):
    new_dico = []
    new_init = []
    new_final = []
    trueindex = {}
    fin =0
    #add a new state
   
    new_init.append(1)
    new_dico.append({})
    list_init = list_init_states(init)
    if (alphabet[0] == '€'):
        list_init = add_empty_list(dico, list_init)
        for k in (list_init):
            if (final[k]):
                fin = 1
        if (fin == 1):
            new_final.append(1)
        else:
            new_final.append(0)
        traduction[str(list_init)] = 0
        trueindex[0] = 0
    else :
        if (info.if_empty_word(dico, init, final, alphabet)):
            new_final.append(1)
        else:
            new_final.append(0)
        list_init.sort()
        if (traduction != {}):
            key = disp.get_key(int(str(list_init).replace("[","").replace("]","")), traduction)
            if (key):
                traduction[str(list_init)] = key
                trueindex[key] = 0
        else: 
            trueindex[str(list_init)] = 0        
    
    # add the transitions to the new state
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

# fuction that gives the list of initial states
def list_init_states(init):
    list_init = []
    for i in range(len(init)):
        if (init[i] == 1):
            list_init.append(i)
    return list_init

# fuction that add the transitions with empty word from the states : give the "prime" states
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

# function for the determinization of an automaton : add a new state for each transition
def determinization2(dico, init, final, alphabet, traduction):
    #call to the fuction that create the initial state
    traduction, new_dico, new_init, new_final , trueindex = init_determinization(dico, init, final, alphabet, traduction)
    #add the new state for each transition
    for state in new_dico:
        for lettre in alphabet :
            #not adding the transition for the empty word or an empty transition
            if (lettre == '€'): 
                continue
            if (state.get(lettre) == None):
                state[lettre] = [-1]
            for transition in state[lettre]:
                if transition == -1:
                    continue
                
                #add the new state
                list_new_state = [transition]
                if (alphabet[0] == '€'):
                    list_new_state = add_empty_list(dico, list_new_state) #call to the function that add the empty transition to the new state
                    list_new_state = list(set(list_new_state))
                    list_new_state = sorted(list_new_state)
                if (str(list_new_state) not in traduction.keys() and trueindex.get(str(state[lettre])) == None):
                    traduction[str(list_new_state)] = transition
                if(str(state[lettre]) not in trueindex.keys()):
                    trueindex[str(state[lettre])] = len(new_dico)
                    new_dico.append({})
                    new_init.append(0)
                    if (alphabet[0] == '€' and info.is_final_state(final, list_new_state) == True):
                        new_final.append(1)
                    elif (alphabet[0] != '€' and info.is_final_state(final, state[lettre]) == True):
                        new_final.append(1)
                    else:
                        new_final.append(0)
    
                #add the transition to the new state
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
                        new_dico[(trueindex[str(state[lettre])])][newletter].sort()                       
                    if (new_dico[(trueindex[str(state[lettre])])][newletter] == []):
                        new_dico[(trueindex[str(state[lettre])])][newletter] = [-1]

    #remove the empty word from the alphabet
    new_alphabet = []
    for letter in alphabet:
        if (letter != '€'):
            new_alphabet.append(letter)
    #call to the function that translate the states of the new automaton
    build_automaton(new_dico, new_init, new_final, new_alphabet, traduction, trueindex)
    return new_dico, new_init, new_final, new_alphabet, traduction, trueindex

# fuction that return the list of the transition states for a given list of state(s) and a given letter
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

def minimization(dico, init, final, alphabet, trueindex):
    minimization_change = 0
    # displaying changements in name of states
    if trueindex != None:
        for i in range(len(trueindex)):
            print("The state", disp.get_key(i, trueindex), "is renamed: ", i)
    groups = []
    # separating final and initial states
    for isfinal in final:
        if isfinal == 0:
            groups.append(1)
        else:
            groups.append(-1)
    print("\nSeparating final states and other states:\n")
    disp.display_partition(dico, init, final, alphabet, groups)
    time.sleep(1)
    # first step: separating on the pattern of states of arrivals (NT / T)
    pattern = []
    for i in range(len(dico)):
        pattern.append([])
        for char in alphabet:
            if dico[i].get(char) != -1:
                for j in range (len(dico[i].get(char))):
                    if final[dico[i].get(char)[j]] == 0:
                        pattern[i].append(0)
                    elif final[dico[i].get(char)[j]] == 1:
                        pattern[i].append(1)
    for i in range(len(groups)):
        if groups[i] == -1:
            groups[i] -= i
        else:
            groups[i] += i
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
    # displaying partitions of this first separation
    print("\nFirst iteration of the minimisation:\n")
    disp.display_partition(dico, init, final, alphabet, groups)
    time.sleep(1)
    # 2nd step: separating depending on 1) if states of arrival belongs to the group of the state we are on
    #           2) if not, recognizing other states doing the same that goes in the same group
    old_groups =[0]*len(groups)
    iteration = 2
    while old_groups != groups: # processing until there is no more changes
        count_pos, count_neg = 0,0
        for i in range (len(groups)):
            if old_groups[i] != groups[i]:
                if groups[i] > 0:
                    count_pos += 1
                else:
                    count_neg -= 1
        old_groups = copy.deepcopy(groups)
        for j in range(len(groups)):
            list_of_related_states = []
            # initial states part
            if groups[j] > 0:
                our_group = groups[j]
                for i in range(len(groups)):
                    if groups[i] == our_group:
                        list_of_related_states.append(i)
                done = 0
                for char in alphabet:
                    if done == 0:
                        if dico[j].get(char)[0] not in list_of_related_states:
                            free_number = 1
                            while free_number in groups:
                                free_number += 1
                            if free_number <= count_pos:
                                groups[j] = free_number
                            for x in list_of_related_states:
                                if dico[j].get(char)[0] == dico[x].get(char)[0]:
                                    groups[x] = groups[j]
                            for char2 in alphabet:
                                if dico[j].get(char2)[0] not in list_of_related_states:
                                    if char2 != char:
                                        for x in list_of_related_states:
                                            if dico[j].get(char2)[0] != dico[x].get(char2)[0]:
                                                free_number = 1
                                                while free_number in groups:
                                                    free_number += 1
                                                if free_number <= count_pos:
                                                    groups[x] = free_number
                            done = 1
            # final states part
            if groups[j] < 0:
                our_group = groups[j]
                for i in range(len(groups)):
                    if groups[i] == our_group:
                        list_of_related_states.append(i)
                done = 0
                for char in alphabet:
                    if done == 0:
                        if dico[j].get(char)[0] not in list_of_related_states:
                            free_number = -1
                            while free_number in groups:
                                free_number -= 1
                            if free_number >= count_neg:
                                groups[j] = free_number
                            for x in list_of_related_states:
                                if dico[j].get(char)[0] == dico[x].get(char)[0]:
                                    groups[x] = groups[j]
                            for char2 in alphabet:
                                if dico[j].get(char2)[0] not in list_of_related_states:
                                    if char2 != char:
                                        for x in list_of_related_states:
                                            if dico[j].get(char2)[0] != dico[x].get(char2)[0]:
                                                free_number = -1
                                                while free_number in groups:
                                                    free_number -= 1
                                                if free_number >= count_neg:
                                                    groups[x] = free_number
                            done = 1
        #displaying partitions
        if old_groups != groups:
            if iteration == 2:
                print("\n",iteration,"nd iteration of the minimisation:\n")
            elif iteration == 3:
                print("\n",iteration,"rd iteration of the minimisation:\n")
            else:
                print("\n",iteration,"th iteration of the minimisation:\n")
            disp.display_partition(dico, init, final, alphabet, groups)
            time.sleep(1)
            iteration += 1

    #removing lines that we merge
    list_of_removed_index = []
    for i in range(-len(groups), len(groups)+1):
        list_index = []
        for index in range(len(groups)):
            if groups[index] == i:
                list_index.append(index)
        for x in range(1, len(list_index)):
            for lettre in alphabet:
                for new_state in dico[list_index[x]].get(lettre):
                    if new_state not in list_index[1:]:
                        if new_state not in dico[list_index[0]].get(lettre):
                            dico[list_index[0]].get(lettre).append(new_state)
                for remove_element in list_index[1:]:
                    for j in range(len(dico[list_index[0]].get(lettre))):
                        if dico[list_index[0]].get(lettre)[j] == remove_element:
                            dico[list_index[0]].get(lettre)[j] = list_index[0]
        for i in range(1,len(list_index)):
            print("\nThe state", list_index[-i], "will be merged into the state", list_index[0], "!")
            minimization_change = 1
            list_of_removed_index.append(list_index[-1])
            del dico[list_index[-i]]
            if final[list_index[-i]] == 1:
                final[list_index[0]] = 1
            del final[list_index[-i]]
            if init[list_index[-i]] == 1:
                init[list_index[0]] = 1
            del init[list_index[-i]]
    #creating a new list of index
    trueindex_new = {}
    change = 0
    for i in range(len(dico)):
        if i in list_of_removed_index:
            change += 1
        i_list = [i+change]
        trueindex_new[str(i_list)]=i
    if minimization_change == 0:
        print("\nNo changes, automaton already minimised at its best.")
    #displaying changements in name of states
    return dico, init, final, trueindex_new

# function that returns the complementary automaton : tranform final states into non-final states and vice-versa
def complementarisation(dico, init, final, alphabet):
    for state in range(len(final)):
        if (final[state] == 1):
            final[state] = 0
        else:
            final[state] = 1
    return dico, init, final

# fuction that returns if the word is recognized by the automaton
def recognize_word(dico, init, final, alphabet, word):
    for lettre in word:
        if (lettre not in alphabet):
            return False
    #following the transition table
    for i in range(len(init)):
        if (init[i] == 1): #beginning with the initial state
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

# fuction that translate the states of the automaton to match the index of the state in the dictionnary
def build_automaton(dico, init, final, alphabet, traduction, trueindex):
    for state in dico:
        # replace the state that is a list by the index of the state in the dico
        for lettre in alphabet:
            if str(state[lettre]) in traduction:
                state[lettre] = [traduction[str(state[lettre])]]
            if (str(state[lettre]) in trueindex):
                state[lettre] = [trueindex[str(state[lettre])]]