
import information as info

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

def if_empty(dico, init, final, alphabet):
    for i in range(len(init)):
        if init[i] == 1 and final[i] == 1:
            return True
    return False

info.is_standard(dico, init, final, alphabet)

info.is_deterministic(dico, init, final, alphabet)

info.is_complete(dico, init, final, alphabet)

'''def standardization(dico, init, final, alphabet):
    if is_standard(dico, init, final, alphabet):
        return dico, init, final
    else:
        #add a new state
        if (if_empty(dico, init, final, alphabet)):
            final.append(1)
        else
            final.append(0)
        init.append(1)
        dico.append({})
        for i in range(len(alphabet)):
            dico[len(dico) - 1][alphabet[i]] = [-1]
        
        return dico, init, final
    
print(standardization(dico, init, final, alphabet))'''

