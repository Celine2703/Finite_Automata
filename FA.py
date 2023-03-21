import information as info
import display as disp
import algo as algo


# create a dictionnary table
def create_dict_array(n, alphabet):
    dict_array = []
    for i in range(n):
        dict_array.append({})
        for j in range(len(alphabet)):
            dict_array[i][alphabet[j]] = [-1]
    return dict_array


# create an array of init states
def create_init_array(n):
    init_array = []
    for i in range(n):
        init_array.append(0)
    return init_array


# create an array of final states
def create_final_array(n):
    final_array = []
    for i in range(n):
        final_array.append(0)
    return final_array


def open_file(num):
    # opening and saving lines of the automata file
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

    # creating the dictionnary of transitions
    dico = create_dict_array(states, alphabet)
    for i in range(len(lines) - 4):
        transition = lines[i + 4].rstrip("\n")
        if dico[int(transition[0])][transition[1]] == [-1]:
            dico[int(transition[0])][transition[1]] = []
        dico[int(transition[0])][transition[1]].append(int(transition[2:]))

    return dico, init, final, alphabet


def main():
    # the menu of our program
    print("\nWhich file do you want to open? (type 0 to quit)")
    x = int(input("-"))
    if x == 0 :
        print("\nGoodbye.\n")
        return
    dico, init, final, alphabet = open_file(x)
    disp.display_table(dico, init, final, alphabet)
    y = -1
    while y != 0:
        print("\nWhat do you want to do?\n 1)Is it standard?\n 2)Is it deterministic?\n 3)Is it complete?\n 4)Standardisation\n 5)Determinization and completion \n 6)Minimization\n 7)Read a word\n (0 to return to the selection of the file)\n")
        y = int(input("-"))
        if y == 1:
            if info.is_standard(dico, init, final, alphabet):
                print("It is standard!")
        elif y == 2:
            if info.is_deterministic(dico, init, final, alphabet):
                print("It is deterministic!")
        elif y == 3:
            if info.is_complete(dico, init, final, alphabet):
                print("It is complete!")
        elif y == 4:
            if info.is_standard(dico, init, final, alphabet):
                print("This automaton is already standard.")
            else:
                dico, init, final = algo.standardization(dico, init, final, alphabet)
                disp.display_table(dico, init, final, alphabet)
        elif y == 5:
            if info.is_deterministic(dico, init, final, alphabet):
                print("This automaton is already determined.")
                if info.is_complete(dico, init, final, alphabet):
                    print("This automaton is already complete and determined.")
                else:
                    dico, init, final = algo.completion(dico, init, final, alphabet)
                    print("Completion done, the CFDA is:")
                    disp.display_table(dico, init, final, alphabet)
            else:
                dico, init, final = algo.completion(dico, init, final, alphabet)
                dico, init, final = algo.determinization(dico, init, final, alphabet)
                print("Completion and determinization complete, the CDFA is:")
                disp.display_table(dico, init, final, alphabet)
        elif y == 6:
            dico, init, final = algo.minimization(dico, init, final, alphabet)
            disp.display_table(dico, init, final, alphabet)
        elif y == 7:
            print("Input words please. (type 'end' if you want to return to the menu)")
            w = input("-")
            while w != "end":
                if algo.recognize_word(dico, init, final, alphabet, w):
                    print("This word can be read!")
                else:
                    print("This word can't be read!")
                print("Input a word please. (type 'end' if you want to return to the menu)")
                w = input("-")
        elif y == 0:
            main()


main()
