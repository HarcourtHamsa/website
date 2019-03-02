def get_Api():
    pass

def read_file_contents():
    """ This function reads data from a file and prints it out """
    try:
        file  =  input("Provide a file name : ")
        open_file  =  open(file, "r")
        file_data  = open_file.readlines()
        return file_data

    except FileNotFoundError:
        print ("File Not Found DickHead")


    
read_file_contents()