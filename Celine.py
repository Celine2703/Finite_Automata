import information as info
import display as disp
import algo as algo

# create a dictionnary table
def create_dict_array(n):
    dict_array = []
    for i in range(n):
        dict_array.append({})
    return dict_array

#create an array for the states
def create_array(n):
    init_array = []
    for i in range(n):
        init_array.append(0)
    return init_array

init=create_array(3)
init[0]=1
final=create_array(3)
final[2]=1
alphabet=['a','b']
dico=create_dict_array(3)
dico[0]['a']=[1]
dico[0]['b']=[2]
dico[1]['a']=[2]
dico[1]['b']=[-1]
dico[2]['a']=[-1]
dico[2]['b']=[1]

info.is_complete(dico, init, final, alphabet)
disp.display_table(dico, init, final, alphabet)
algo.completion(dico, init, final, alphabet)
print("\n")
disp.display_table(dico, init, final, alphabet)
info.is_standard(dico, init, final, alphabet)
info.is_deterministic(dico, init, final, alphabet)
info.is_complete(dico, init, final, alphabet)