import collections

def get_anagrams(palabras):
    dict = {}
    for palabra in palabras:
        palabra_ordenada = ''.join(sorted(palabra))
        if palabra_ordenada in dict:
            arreglo = dict[palabra_ordenada]
            arreglo.append(palabra)
            dict[palabra_ordenada] = arreglo
        else:
            dict[palabra_ordenada] = [palabra]
    return dict
                
    
print(get_anagrams(["eat", "tea", "tan", "ate", "nat", "bat","tab","tsb"]))