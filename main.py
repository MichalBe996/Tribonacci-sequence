def tribonacci(signature, n):
    tribo_list = []
    if n == 0:
        return []
    elif n == 1:
        tribo_list.append(signature[0])
        return tribo_list
    elif n == 2:
        tribo_list.append(signature[0])
        tribo_list.append(signature[1])
        return tribo_list
    elif n == 3:
        tribo_list.append(signature[0])
        tribo_list.append(signature[1])
        tribo_list.append(signature[2])

        return tribo_list
    elif n > 3:
        i = 0
        
        j = 1
        
        k = 2
        
        
        for x in signature:
            tribo_list.append(x)
        for x in range(n-3):
            tribo_list.append(tribo_list[i] + tribo_list[j] + tribo_list[k])
            i+=1
            j+=1
            k+=1
            
    return tribo_list
            
            
