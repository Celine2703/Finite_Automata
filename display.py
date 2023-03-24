from tabulate import tabulate

def display_ligne(dico, init, final, alphabet, i, traduction):
    tab = []
    tab.append('')
    if (init[i] == 1):
        tab[0] += 'I '
    if (final[i] == 1):
        tab[0] += 'F'
    if traduction:
        key = get_key(i, traduction)
        if key:
            tab.append(key.replace("[", "").replace("]", ""))
        else:
            tab.append(i)
    else:
        tab.append(i)
    for j in range(len(alphabet)):
        if (dico[i][alphabet[j]] == [-1]):
            tab.append('--')
        else:
            if traduction:
                key = get_key(int(str(dico[i][alphabet[j]]).replace("[", "").replace("]", "")), traduction)
                if key:
                    tab.append(key)
                else:
                    tab.append(dico[i][alphabet[j]])
            else:
                tab.append(dico[i][alphabet[j]])
    return (tab)

def display_table(dico, init, final, alphabet, traduction = None):
    print ("dico = ", dico)
    tab = []
    header = []
    header.append('')
    header.append('State')
    for i in range(len(alphabet)):
        header.append(alphabet[i])
    for i in range(len(dico)):
        tab.append(display_ligne(dico, init, final, alphabet, i, traduction))
    print(tabulate(tab, headers=header, tablefmt='pipe'))

#function to get key from value in a dictionnary
def get_key(val, dico):
    for key, value in dico.items():
        if val == value:
            return key
    return False