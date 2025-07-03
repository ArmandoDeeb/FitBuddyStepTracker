try: # see if the file exists
    file = open('test_log.txt', 'r') 
except FileNotFoundError: 
    print("No file found - exiting now") # print this message if the file does not exist
    exit() 

def ShowAll():
    overview = file.read()
    print(overview)
    file.seek(0) # returns the pointer back to the start of the file
        
def Summary():
    file.seek(0) # returns the pointer back to the start of the file
    total = 0
    line_count = 0
    list = []  
    # removing newline characters and adding values to a new list
    for line in file: 
        if line[-1] == '\n': 
            list.append(line[:-1])
        else:
            list.append(line)
    # for every entry in the list, access the number to compute num_steps and total
    for item in list:
        num_steps = int(item[11:])
        total += num_steps
        line_count += 1
    print(total)
    print(total/line_count)
    

def Main(): # main function dealing with user interface
    print("Welcome to FitBuddy - StepTracker")
    while True:
        
        command = input("< ")
        if command == "quit":
            print("Goodbye!")
            break
        elif command == "show all":
            ShowAll()
        elif command == "show summary":
            Summary()
        else:
            print("Please enter a valid command!")
            
        

Main()

    







