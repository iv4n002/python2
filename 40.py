def eliminarcapicua(llista):
    
    if len(llista) <= 2:
        return llista
    
    elif llista[0] == llista[-1]:
        return eliminarcapicua(llista[1:-1])
        
    else:
        nova_llista = [llista[0]] + eliminarcapicua(llista[1:-1]) + [llista[-1]]
        return nova_llista

entrada = input("Introdueix els elements de la llista separats per coma: ")
llista_entrada = entrada.split(",")
llista_entrada = [int(i) for i in llista_entrada]

nova_llista = eliminarcapicua(llista_entrada)
print(nova_llista)