def read_data(path):
    f = open(path, "r")
    data = f.read()
    f.close()
    return data

def write_data(path, content):
    f = open(path, "w")
    f.write(content)
    f.close()
    
def update_data(path, content):
    f = open(path, "a")    
    f.write(content)
    f.close()
