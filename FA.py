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
dico = create_dict_array(3)
dico[0]['a'] = [1, 0]
dico[0]['b'] = [-1]
dico[1]['a'] = [1]
dico[1]['b'] = [2]
dico[2]['a'] = [-1]
dico[2]['b'] = [-1]
print(dico)
init = create_init_array(3)
init[0] = 1
final = create_final_array(3)
final[0] = 1

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

print(is_standard(dico, init, final, alphabet))

def is_complete(dico, init, final, alphabet):
    for i in range(len(dico)):
        for j in range(len(alphabet)):
            if dico[i][alphabet[j]] == -1:
                print("Not complete: transition to nowhere")
                return False
    return True

print(is_complete(dico, init, final, alphabet))

def standardization(dico, init, final, alphabet):
    if is_standard(dico, init, final, alphabet):
        return dico, init, final
    else:
        #add a new state
        return dico, init, final
    
print(standardization(dico, init, final, alphabet))

#def is_deterministic(dico, init, final, alphabet):
