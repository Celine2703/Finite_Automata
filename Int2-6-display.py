from tabulate import tabulate

# function that display partitions for minimization
def display_partition(dico, init, final, alphabet, groups):
    partition_number = 0
    for i in range(-len(groups), len(groups)+1):
        partition = []
        newinit = []
        newfinal = []
        list_index = []
        trueindex = {}
        place = 0
        for index in range(len(groups)):
            if groups[index] == i:
                list_index.append(index)
                index_list = [index]
                trueindex[str(index_list)]= place
                if init[index] == 1:
                    newinit.append(1)
                else:
                    newinit.append(0)
                if final[index] == 1:
                    newfinal.append(1)
                else:
                    newfinal.append(0)
                place += 1
        for j in list_index:
            partition.append(dico[j])
        if i in groups:
            partition_number += 1
            print("Partition number °", partition_number)
            display_table(partition, newinit, newfinal, alphabet, True , trueindex, False)

# function that creates a line for the table_to_display
def display_ligne(dico, init, final, alphabet, i, traduction, trueindex, donot):
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
            if traduction and donot:
                if trueindex != None:
                    key = get_key(int(str(dico[i][alphabet[j]]).replace("[", "").replace("]", "")), trueindex)
                    if key:
                        tab.append(key.replace(", ", "·"))
                    else:
                        tab.append(dico[i][alphabet[j]])
                else:
                    key = traduction.get(str(dico[i][alphabet[j]]))
                    tab.append(dico[i][alphabet[j]])
            else:
                tab.append(dico[i][alphabet[j]])
    return (tab)

# function that displays the automaton by creating a table with a header
def display_table(dico, init, final, alphabet, traduction = None, trueindex = None, donot = True):
    tab = []
    header = []
    header.append('')
    header.append('State')
    for i in range(len(alphabet)):
        if(alphabet[i] == 'â‚¬'):
            header.append("Ɛ")
        else:
            header.append(alphabet[i])
    for i in range(len(dico)):
        tab.append(display_ligne(dico, init, final, alphabet, i, traduction, trueindex, donot))
    print(tabulate(tab, headers=header, tablefmt='pipe'))

#function to get key from value in a dictionnary
def get_key(val, dico):
    for key, value in dico.items():
        if val == value:
            return key
    return False