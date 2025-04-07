def word_count(path_to_file):
    c = -1
    with open(path_to_file) as f:
        c = len(f.read().split()) 
    return c

def char_count(path_to_file):
    caratteri = {}
    with open(path_to_file) as f:
        stringa = f.read().lower()
        for carastring in stringa:
            if carastring in caratteri:
                caratteri[carastring] += 1
            else:
                caratteri[carastring] = 1
    return caratteri

def estrai(dicto):
    return dicto["count"]

def riordina(dicto):
    caratteri = []
    for car in dicto:
        if car.isalpha():
            caratteri.append({"char": car, "count": dicto[car]})
    
    
    caratteri.sort(reverse=True, key=estrai)
    
    return caratteri