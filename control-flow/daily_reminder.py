task = input("Enter your task: ").capitalize()
time_bound = input("Is it time-bound? (yes/no): ").lower()
priority = input("Priority (high/medium/low): ").lower()


match priority:
    case "high": 
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Please complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be done today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to complete it soon.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that can be done today.")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")        
    case _:
        print(f"Unknown task or priority level.")