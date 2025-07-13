import random

def read_log():
    with open('test_log.txt', 'r') as file:
        return[line.strip() for line in file]



def ShowAll():
    lines = read_log()
    for line in lines:
        print(line)
        
def Summary():
    total = 0
    line_count = 0
    lines = read_log()
    # for every entry in the list, access the number to compute num_steps and total
    for line in lines:
        date, steps = line.split(",")
        total += int(steps)
        line_count += 1
    print(f"Total steps: {total}")
    print(f"Average steps: {total/line_count}")


def Streak(x):
    lines = read_log()
    current_streak = 0
    largest_streak = 0
    for line in lines:
        date, steps = line.split(",")
        if int(steps) >= x:
            current_streak += 1
            largest_streak = max(largest_streak, current_streak)
        else:
            current_streak = 0
    print(f"Longest streak: {largest_streak} days")


def Progress(y):
    goal_met_count = 0 # days in which step goal was met
    num_lines = 0 # to track total number of days
    lines = read_log()
    for line in lines:
            num_lines += 1
            date, steps = line.split(",")
            num_steps = int(steps)
            if y > num_steps:
                goal_met_count += 1
            else:
                goal_met_count += 0

    print(f"Met goal on {goal_met_count} out of {num_lines} days")


def simulate(x):

   
    lines = read_log()
    
    last_line = lines[-1]
    last_date = last_line.split(',')[0]
    
    year, month, day = map(int, last_date.split('-')) 
               
    with open('test_log.txt', 'a') as file:
        for i in range(x):
            day += 1
            formatted_day = f"{day:02}"
            steps = random.randint(4000,12000)
            new_line = f"\n{year}-{month:02}-{formatted_day},{steps}"
            file.write(new_line)

def recommended():
    lines = read_log()
    total_steps = 0
    for line in lines[-5:]:
        data, steps = line.split(",")
        total_steps += int(steps)
    
    if total_steps / 5 > 9000:
        print("You're doing great! Keep it up!")
    
    elif 7000 < total_steps / 5 <= 9000:
        print("Great job! Let's aim for 9000+")
    
    else:
        print("Time to step up! Try reaching your goal!")
    

        
    
           


        
""" - old simulate function (error)
def simulate(x):
    
    with open('test_log.txt', 'r') as file:
        lines = file.readlines()
               
    with open('test_log.txt', 'a') as file:
        last_line = lines[-1].strip()
        last_date = last_line.strip().split(',')[0]
        for i in range(0,x):
            day = int(last_date.strip().split('-')[2]) + 1
            formatted = f"{day:02}"
            steps = random.randint(4000,12000)
            text = f"\n2025-06-{formatted},{steps}"
            file.write(text)
            last_line = lines[-1].strip()
            last_date = last_line.strip().split(',')[0]
    """

    



def Main(): # main function dealing with user interface
    print("Welcome to FitBuddy - StepTracker")
    text = "2025-06-01,4567\n2025-06-02,6290\n2025-06-03,7100\n2025-06-04,7500\n2025-06-05,9120"
    with open('test_log.txt','w') as file:
        file.write(text)



    while True:
        
        command = input("< ")
        if command == "quit":
            print("Goodbye!")
            break
        elif command == "show all":
            ShowAll()
        elif command == "show summary":
            Summary()
        elif command.startswith("goal"):
                parts = command.split() # splits command into two parts, so we can access the second value as the goal steps
                if len(parts) == 2 and parts[1].isdigit(): # checks if length of parts is two, and second part is a number
                    goal_steps = int(parts[1]) # assign the goal number of steps as the second part of the command
                    Streak(goal_steps) # passing in goal_steps into the Streak function
                else:
                    print("Please enter a valid number!")
        elif command == "progress":
            try:
                a = goal_steps
                Progress(a)
            except UnboundLocalError:
                print("Please enter your goal amount of steps first!")

        elif command.startswith("simulate"):
            parts1 = command.split()
            if len(parts1) == 2 and parts1[1].isdigit():
                new_entries = int(parts1[1])
                simulate(new_entries)
            else:
                print("please enter a number")
        
        elif command == "recommended":
            recommended()


        else:
            print("Please enter a valid command!")
        
            
        
if __name__ == "__main__":
    Main()

    







