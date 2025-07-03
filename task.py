try:
    file = open('test_log.txt', 'r')
except FileNotFoundError:
    print("No file found - exiting now")
    exit()

def ShowAll():
    overview = file.read()
    print(overview)
    file.seek(0) # returns the pointer back to the start of the filesjpw 
        
def Summary():
    total = 0
    line_count = 0
    list = []  
    for line in file:
        if line[-1] == '\n':
            list.append(line[:-1])
        else:
            list.append(line)
    for item in list:
        num_steps = int(item[11:])
        total += num_steps
        line_count += 1
    print(total)
    print(total/line_count)
    total = 0
    line_count = 0
    list = []

def Main():
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
            
        

Main()

    







