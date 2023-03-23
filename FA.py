import information as info
import display as disp
import algo as algo
import init as ini

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
    # the menu of our program
    print("\nWhich automaton do you want? (type 0 to quit)")
    x = int(input("-> "))
    if x == 0 :
        print("Goodbye.\n")
        return
    dico, init, final, alphabet = ini.open_file(x)
    traduction = {}
    disp.display_table(dico, init, final, alphabet, traduction = None)
    test_automaton(dico, init, final, alphabet)
    y = -1
    while y != 0:
        print_menu()
        y = int(input("-> "))
        if y == 1:
            if info.is_standard(dico, init, final, alphabet) == -1:
                print("This automaton is already standard.")
            else:
                traduction = algo.standardization(dico, init, final, alphabet, traduction)
                print("Standardization done, the automaton is now:")
                disp.display_table(dico, init, final, alphabet, traduction)
        elif y == 2:
            if info.is_deterministic(dico, init, final, alphabet) == -1:
                if info.is_complete(dico, init, final, alphabet) == -1:
                    print("This automaton is already deterministic and complete.")
                else:
                    algo.completion(dico, init, final, alphabet)
                    print("Completion done, the automaton is now:")
            else:
                traduction = algo.determinization(dico, init, final, alphabet, traduction)
                print("traduction = ", traduction)
                if info.is_complete(dico, init, final, alphabet) == -1:
                    print("Determinization done, the automaton is already complete, it is now:")
                else:
                    dico, init, final = algo.completion(dico, init, final, alphabet)
                    print("Determinization and completion done, the automaton is now:")
            disp.display_table(dico, init, final, alphabet, traduction)
        elif y == 3:
            dico, init, final = algo.minimization(dico, init, final, alphabet)
            disp.display_table(dico, init, final, alphabet, traduction)
        elif y == 4:
            print("Input your word. (type 'end' to return to the menu)")
            w = input("-> ")
            while w != "end":
                if algo.recognize_word(dico, init, final, alphabet, w):
                    print("Yes: this word has been recognized!")
                else:
                    print("No: this word has not been recognized!")
                print("Another word? (type 'end' to return to the menu)")
                w = input("-> ")
        elif y == 6:
            main()
        elif y == 0:
            print("Goodbye.\n")
            exit()

main()
