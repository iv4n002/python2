def nums_que_comencen_per():
    num_palabras_a = 0
    
    while True:
        palabra = input("Introduce una palabra (o escribe 'fin' para terminar): ")
        
        if palabra == "fin":
            break
        
        if len(palabra) > 0 and palabra[0] == "a":
            num_palabras_a += 1
    
    print("El número total de palabras que comienzan por 'a' es:", num_palabras_a)