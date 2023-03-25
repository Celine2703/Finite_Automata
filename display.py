from tabulate import tabulate

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
            # print ("i = ", i, "trueindex = ", trueindex)
            key = get_key(i, trueindex)
            if key:
                # print("key", key)
                tab.append(key)
            else :
                index = i
                tab.append(index)
                print ("index = ", index)
    else:
        tab.append(i)
    for j in range(len(alphabet)):
        if (dico[i][alphabet[j]] == [-1]):
            tab.append('--')
        else:
            if traduction:
                key = get_key((str(dico[i][alphabet[j]]).replace("[", "").replace("]", "")), traduction)
                if key:
                    tab.append(key.replace(", ", "·"))
                else:
                    tab.append(dico[i][alphabet[j]])
            else:
                tab.append(dico[i][alphabet[j]])
    return (tab)

def display_table(dico, init, final, alphabet, traduction = None, trueindex = None):
    tab = []
    header = []
    header.append('')
    header.append('State')
    print ("\ndico end = ", dico)
    for i in range(len(alphabet)):
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