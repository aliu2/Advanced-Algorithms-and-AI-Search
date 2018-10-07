def check_path(path):
    # return true/false depending on whether the path is valid or not.
    i = 0
    while i < len(path)-1:
        child = path[i]
        parent = path[i+1]
        if child not in parent.get_moves():
            return False
        i+=1
    return True
