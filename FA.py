import information as info
import display as disp

#creer un tableau de dictionnaires
def create_dict_array(n):
    dict_array = []
    for i in range(n):
        dict_array.append({})
    return dict_array

def create_init_array(n):
    init_array = []
    for i in range(n):
        init_array.append(0)
    return init_array

def create_final_array(n):
    final_array = []
    for i in range(n):
        final_array.append(0)
    return final_array

#def put_in_dico

#test
alphabet = ['a', 'b']
dico = create_dict_array(6)
dico[0]['a'] = [1]
dico[0]['b'] = [2]
dico[1]['a'] = [4]
dico[1]['b'] = [4]
dico[2]['a'] = [4]
dico[2]['b'] = [5]
dico[3]['a'] = [1, 2]
dico[3]['b'] = [3]
dico[4]['a'] = [-1]
dico[4]['b'] = [-1]
dico[5]['a'] = [-1]
dico[5]['b'] = [-1]
init = create_init_array(6)
init[0] = 1
init[3] = 1
final = create_final_array(6)
final[0] = 1

disp.display_table(dico, init, final, alphabet)

def if_empty_word(dico, init, final, alphabet):
    for i in range(len(init)):
        if init[i] == 1 and final[i] == 1:
            return True
    return False

info.is_standard(dico, init, final, alphabet)

info.is_deterministic(dico, init, final, alphabet)

info.is_complete(dico, init, final, alphabet)

def standardization(dico, init, final, alphabet):
    if (info.is_standard(dico, init, final, alphabet)):
        return dico, init, final
    else:
        #add a new state
        if (if_empty_word(dico, init, final, alphabet)):
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

standardization(dico, init, final, alphabet)
disp.display_table(dico, init, final, alphabet)
info.is_standard(dico, init, final, alphabet)
info.is_deterministic(dico, init, final, alphabet)
