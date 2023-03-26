import importlib.util

# Import Int2-6-information
info_spec = importlib.util.spec_from_file_location("Int2-6-information", "./Int2-6-information.py")
info = importlib.util.module_from_spec(info_spec)
info_spec.loader.exec_module(info)

# Import Int2-6-display
disp_spec = importlib.util.spec_from_file_location("Int2-6-display", "./Int2-6-display.py")
disp = importlib.util.module_from_spec(disp_spec)
disp_spec.loader.exec_module(disp)

# Import Int2-6-algo
algo_spec = importlib.util.spec_from_file_location("Int2-6-algo", "./Int2-6-algo.py")
algo = importlib.util.module_from_spec(algo_spec)
algo_spec.loader.exec_module(algo)

# Import Int2-6-init
ini_spec = importlib.util.spec_from_file_location("Int2-6-init", "./Int2-6-init.py")
ini = importlib.util.module_from_spec(ini_spec)
ini_spec.loader.exec_module(ini)


def print_menu():
    print("\nWhat do you want to do?\n")
    print("1- Standardisation")
    print("2- Determinization and completion")
    print("3- Minimization")
    print("4- Read a word")
    print("5- Complementary automaton")
    print("6- Select another automaton")
    print("0- Quit\n")

def test_automaton(dico, init, final, alphabet):
    x = info.is_standard(dico, init, final, alphabet)
    if x == -1:
        print("The automaton is standard")
    elif x == -2:
        print("Not standard: more than one initial state")
    else:
        print("Not standard: transition to initial state")
    x = info.is_deterministic(dico, init, final, alphabet)
    if x == -1:
        print("The automaton is deterministic")
    elif x == -2:
        print("Not deterministic: more than one initial state")
    else:
        print("Not deterministic: more than one transition for a letter in state", x)
    x = info.is_complete(dico, init, final, alphabet)
    if x == -1:
        print("The automaton is complete")
    else:
        print("Not complete: transition to nowhere in state", x)


def main():
    trueindex = 0
    # the menu of our program
    print("\nWhich automaton do you want? (type 0 to quit)")
    x = input("-> ")
    if x == '0' :
        print("Goodbye.\n")
        return
    dico, init, final, alphabet = ini.open_file(x)
    traduction = {}
    disp.display_table(dico, init, final, alphabet, traduction = None)
    test_automaton(dico, init, final, alphabet)
    y = -1
    minimized = False
    while y != 0:
        print_menu()
        y = input("-> ")
        if y == '1':
            if info.is_standard(dico, init, final, alphabet) == -1:
                print("This automaton is already standard.")
            else:
                traduction = algo.standardization(dico, init, final, alphabet, traduction)
                print("Standardization done, the automaton is now:")
                disp.display_table(dico, init, final, alphabet, traduction)
        elif y == '2':
            if info.is_deterministic(dico, init, final, alphabet) == -1:
                if info.is_complete(dico, init, final, alphabet) == -1:
                    print("This automaton is already deterministic and complete.")
                else:
                    algo.completion(dico, init, final, alphabet)
                    print("Completion done, the automaton is now:")
            else:
                dico, init,final, alphabet,traduction,trueindex = algo.determinization2(dico, init, final, alphabet, traduction)
                if info.is_complete(dico, init, final, alphabet) == -1:
                    print("Determinization done, the automaton is already complete, it is now:")
                else:
                    dico, init, final = algo.completion(dico, init, final, alphabet)
                    print("Determinization and completion done, the automaton is now:")
            disp.display_table(dico, init, final, alphabet, traduction, trueindex)
        elif y == '3':
            dico, init, final = algo.minimization(dico, init, final, alphabet)
            minimized = True
            disp.display_table(dico, init, final, alphabet, traduction)
        elif y == '4':
            print("Input your word. (type 'end' to return to the menu)")
            w = input("-> ")
            while w != "end":
                if algo.recognize_word(dico, init, final, alphabet, w):
                    print("Yes: this word has been recognized!")
                else:
                    print("No: this word has not been recognized!")
                print("Another word? (type 'end' to return to the menu)")
                w = input("-> ")
        elif y == '5':
            if(info.is_deterministic(dico, init, final, alphabet) != -1):
                print("The automaton is not deterministic, it cannot be complemented.")
            if(info.is_complete(dico, init, final, alphabet) != -1):
                print("The automaton is not complete, it cannot be complemented.")
            if(info.is_deterministic(dico, init, final, alphabet) == -1 and info.is_complete(dico, init, final, alphabet) == -1):
                if(minimized):
                    print("Complementary automaton with the AFDCM:")
                else:
                    print("Complementary automaton with the AFDC:")
                algo.complementarisation(dico, init, final, alphabet)
                disp.display_table(dico, init, final, alphabet, traduction, trueindex)
        elif y == '6':
            main()
        elif y == '0':
            print("Goodbye.\n")
            exit()
        else:
            print("Wrong input, try again.")

main()
