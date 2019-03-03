def read_file_contents():
    """ This function reads data from a file and prints it out """
    try:
        file = input("Enter the filename: ")
        with open(file,"r") as read_file:
            file_contents = read_file.readlines()
            return file_contents

    except FileNotFoundError:
        print ("File Is Not Found DickHead")


    
result =  read_file_contents()
print(result)