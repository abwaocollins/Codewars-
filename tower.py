def tower_builder(n_floors):

    lista = []
    stringa = ' * '
    mult = n_floors * 2
    k = n_floors-1
    z = n_floors -1
    if(n_floors > 1):
        for i in range(1,mult,2):
            if(i > 1 and i%2!=0 ): 
                    k = k-1
                    lista.append((k*" ")+(stringa.strip()*(i))+(k*" "))
                    
            else:
                lista.append(stringa)
        lista.insert(0,(z*" "+"*"+z*" "))
        lista.pop(1)
        return lista
    else:
        lista.append(stringa.strip())
        return lista



print(tower_builder(3))