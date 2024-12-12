import ops

choice = input("which ops you wnat to perform? r for read w for write u for update : ")
match(choice):
    case "r":
        try :
            path = input("which file you want read, enter the path of the file : ")
            data = ops.read_data(path)
            print(data)
        except FileNotFoundError as e:
            print("CHeck the file again")
    case "w":
        try :
            path = input("which file you want to write : ")
            content = input("enter the content you want to write : ")
            ops.write_data(path, content)
        except FileNotFoundError as e:    
            print("Check the file again")
    case "u":
        path = input("which file you want to update : ")
        content = input("enter the content you want to update : ")
        ops.update_data(path, content)
        print("data updated successfully")
