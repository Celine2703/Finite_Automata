import information as info
import display as disp


# create a dictionnary table
def create_dict_array(n):
    dict_array = []
    for i in range(n):
        dict_array.append({})
    return dict_array

#create an array of init states
def create_init_array(n):
    init_array = []
    for i in range(n):
        init_array.append(0)
    return init_array

#create an array of final states
def create_final_array(n):
    final_array = []
    for i in range(n):
        final_array.append(0)
    return final_array

def open_file(num):
    #opening and saving lines of the automata file
    name_file = "int2-6-" + str(num) + ".txt"
    with open(name_file, 'r') as f:
        lines = f.readlines()

    # creating a list of the characters of the alphabet
    alphabet = lines[0].split(",")
    alphabet[-1] = alphabet[-1].rstrip("\n")

    # the number of states
    states = int(lines[1].rstrip("\n"))

    # creating a list showing if states are initial
    init = create_init_array(states)
    init_list = lines[2].split(",")
    init_list[-1] = init_list[-1].rstrip("\n")
    for i in range(len(init_list)):
            init[int(init_list[i])] = 1

    # creating a list showing if states are final
    final = create_final_array(states)
    final_list = lines[3].split(",")
    final_list[-1] = final_list[-1].rstrip("\n")
    for i in range(len(final_list)):
        final[int(final_list[i])] = 1

    #creating the dictionnary of transitions
    dico = create_dict_array(states)
    for i in range (len(lines)-4):
        transition = lines[i+4].rstrip("\n")
        dico[int(transition[0])][transition[1]] = transition[2:]

    return dico, init, final, alphabet


def main():
    #the menu of our program
    global dico, init, final, alphabet
    print("\nWhich file do you want to open? (type -1 to quit)")
    x = int(input("-"))
    if x != -1:
        return tests(open_file(x)[0],open_file(x)[1],open_file(x)[2],open_file(x)[3])
    else:
        return

def if_empty_word(dico, init, final, alphabet):
    for i in range(len(init)):
        if init[i] == 1 and final[i] == 1:
            return True
    return False


def tests (dico, init, final, alphabet):
    if info.is_standard(dico, init, final, alphabet):
        print("Standard!!")

    if info.is_deterministic(dico, init, final, alphabet):
        print("Deterministic!!")

    if info.is_complete(dico, init, final, alphabet):
        print("Complete!!")
        
    disp.display_table(dico, init, final, alphabet)

    main()


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
