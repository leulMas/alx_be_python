task = input("Enter your task: ")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no) ").lower()


if priority == "high":
    if time_bound == "yes":
        print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
elif priority == "low":
    if time_bound == "no":
        print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
else:
    print("enter a valid task")