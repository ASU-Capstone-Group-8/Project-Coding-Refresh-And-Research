def flatten(iterable):
    return flattener(iterable)

def flattener(iterable):
    if(isinstance(iterable, list)):
        if(len(iterable) > 0):            
            return flattener(iterable[0]) + flattener(iterable[1:])
        else:
            return []
    elif(iterable is None):
        return []
    else:
        return [iterable]
        
            
    

    
