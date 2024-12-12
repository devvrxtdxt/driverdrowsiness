def read_data(path):
    f = open(path, "r")
    data = f.read()
    f.close()
    return data

def write_data(path, data1):
    f = open(path, "w")
    f.write(data1)
    f.close()