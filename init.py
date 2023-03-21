# create a dictionnary table
def create_dict_array(n, alphabet):
    dict_array = []
    for i in range(n):
        dict_array.append({})
        for j in range(len(alphabet)):
            dict_array[i][alphabet[j]] = [-1]
    return dict_array

# create an array
def create_array(n):
    array = []
    for i in range(n):
        array.append(0)
    return array

def open_file(num):
    # opening and saving lines of the automata file
    name_file = "Int2-6-" + str(num) + ".txt"
    with open(name_file, 'r') as f:
        lines = f.readlines()

    # creating a list of the characters of the alphabet
    alphabet = lines[0].split(",")
    alphabet[-1] = alphabet[-1].rstrip("\n")

    # the number of states
    states = int(lines[1].rstrip("\n"))

    # creating a list showing if states are initial
    init = create_array(states)
    init_list = lines[2].split(",")
    init_list[-1] = init_list[-1].rstrip("\n")
    for i in range(len(init_list)):
        init[int(init_list[i])] = 1

    # creating a list showing if states are final
    final = create_array(states)
    final_list = lines[3].split(",")
    final_list[-1] = final_list[-1].rstrip("\n")
    for i in range(len(final_list)):
        final[int(final_list[i])] = 1

    # creating the dictionnary of transitions
    dico = create_dict_array(states, alphabet)
    for i in range(len(lines) - 4):
        transition = lines[i + 4].rstrip("\n")
        if dico[int(transition[0])][transition[1]] == [-1]:
            dico[int(transition[0])][transition[1]] = []
        dico[int(transition[0])][transition[1]].append(int(transition[2:]))

    return dico, init, final, alphabet