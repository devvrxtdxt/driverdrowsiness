import file

copy = input("Which operation you want to perform : ")
match(copy):
    case"r":
        try:
            path = input("which file you want read, enter the path of the file : ")
            data = file.read_data(path)
            print(data)
        except FileNotFoundError as e:
            print("File not found")
    case"w":
        try :
            path = input("which file you want to write : ")
            data1 = input("enter the content you want to write : ")
            file.write_data(path, file.read_data(data1))
        except FileNotFoundError as e:
            print("File not found")                