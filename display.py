from tabulate import tabulate

def display_ligne(dico, init, final, alphabet, i):
    tab = []
    tab.append('')
    if (init[i] == 1):
        tab[0] += 'I'
    if (final[i] == 1):
        tab[0] += 'F'
    tab.append(i)
    for j in range(2, len(alphabet) + 2):
        if (dico[i][alphabet[j-2]] == [-1]):
            tab.append('--')
        else:
            tab.append(dico[i][alphabet[j-2]])
    return (tab)

def display_table(dico, init, final, alphabet):
    tab = []
    nom = []
    nom.append('')
    nom.append('State')
    for i in range(len(alphabet)):
        nom.append(alphabet[i])
    for i in range(len(dico)):
        tab.append(display_ligne(dico, init, final, alphabet, i))
    print(tabulate(tab, headers=nom, tablefmt='pipe'))