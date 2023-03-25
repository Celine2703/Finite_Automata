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
            key = get_key(i, trueindex)
            print ("key for  ", i, " is " , key)
            if key:
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
                # key = get_key((str(dico[i][alphabet[j]]).replace("[", "").replace("]", "")), traduction)
                # key = traduction.get(str(dico[i][alphabet[j]]).replace("[", "").replace("]", ""))
                # print ("key for  ", str(dico[i][alphabet[j]]), " is " , key)
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
    print("dico to print : ", dico)
    print("\n\n traduction : ", traduction)
    print("\n\n trueindex : ", trueindex)
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