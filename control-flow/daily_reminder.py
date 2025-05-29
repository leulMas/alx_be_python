Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low):").lower()
Time_bound = input("Is it time-bound? (yes/no) ").lower()


if Priority == "high":
    if Time_bound == "yes":
        print(f"Reminder: {Task} is a high priority task that requires immediate attention today!")
elif Priority == "low":
    if Time_bound == "no":
        print(f"Note: {Task} is a low priority task. Consider completing it when you have free time.")
else:
    print("enter a valid task")