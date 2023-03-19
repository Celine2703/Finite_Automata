import information as info
import display as disp
import algo as algo


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
    print("\nWhich file do you want to open? (type -1 to quit)")
    x = int(input("-"))
    dico, init, final, alphabet = open_file(x)
    disp.display_table(dico, init, final, alphabet)
    if x != -1:
        print("\nWhat do you want to do?\n 1)Is it standard?\n 2)Is it deterministic?\n 3)Is it complete?\n 4)Standardisation\n 5)Determinization\n 6)Completion\n 7)Minimization\n 8)Read a word\n")
        x = int(input("-"))
        if x == 1:
            if info.is_standard(dico, init, final, alphabet):
                print("It is standard!")
        elif x==2:
            if info.is_deterministic(dico, init, final, alphabet):
                print("It is deterministic!")
        elif x==3:
            if info.is_complete(dico, init, final, alphabet):
                print("It is complete!")
        elif x==4:
            dico, init, final = algo.standardization(dico, init, final, alphabet)
            disp.display_table(dico, init, final, alphabet)
        elif x==5:
            dico, init, final = algo.determinization(dico, init, final, alphabet)
            disp.display_table(dico, init, final, alphabet)
        elif x==6:
            dico, init, final = algo.completion(dico, init, final, alphabet)
            disp.display_table(dico, init, final, alphabet)
        elif x==7:
            dico, init, final = algo.minimization(dico, init, final, alphabet)
            disp.display_table(dico, init, final, alphabet)
        elif x==8:
            print("Input a word please. (type 'end' if you want to return to the menu)")
            w = input("-")
            while w != "end":
                algo.recognize_word(dico, init, final, alphabet,w)
                print("Input a word please. (type 'end' if you want to return to the menu)")
                w = input("-")
        main()
    else:
        return


main()