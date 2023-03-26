from tabulate import tabulate

# function that creates a line for the table_to_display
def display_ligne(dico, init, final, alphabet, i, traduction, trueindex):
    tab = []
    tab.append('')
    if (init[i] == 1):
        tab[0] += 'I '
    if (final[i] == 1):
        tab[0] += 'F'
    if traduction:
        if trueindex == None:
            key = get_key(i, traduction)
            if key:
                tab.append(key.replace("[", "").replace("]", "").replace(", ", "·"))
            else:
                tab.append(i)
        else:
            key = get_key(i, trueindex)
            if key and key not in tab:
                tab.append(key.replace("[", "").replace("]", "").replace(", ", "·"))
            else :
                index = i
                tab.append(index)
    else:
        tab.append(i)
    for j in range(len(alphabet)):
        if (dico[i][alphabet[j]] == [-1]):
            tab.append('--')
        else:
            if traduction:       
                key = get_key(int(str(dico[i][alphabet[j]]).replace("[", "").replace("]", "")), trueindex)
                if key:
                    tab.append(key.replace(", ", "·"))
                else:
                    tab.append(dico[i][alphabet[j]])
            else:
                tab.append(dico[i][alphabet[j]])
    return (tab)

# function that displays the automaton by creating a table with a header
def display_table(dico, init, final, alphabet, traduction = None, trueindex = None):
    tab = []
    header = []
    header.append('')
    header.append('State')
    for i in range(len(alphabet)):
        if(alphabet[i] == '€'):
            header.append('ε')
        else:
            header.append(alphabet[i])
    for i in range(len(dico)):
        tab.append(display_ligne(dico, init, final, alphabet, i, traduction, trueindex))
    print(tabulate(tab, headers=header, tablefmt='pipe'))

#function to get key from value in a dictionnary
def get_key(val, dico):
    for key, value in dico.items():
        if val == value:
            return key
    return False