task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")


match task:
    case _ if priority == "high" and time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case _ if priority == "high" and time_bound == "no":
        print(f"Reminder: '{task}' is a high priority task. Please complete it as soon as possible.")
    case _ if priority == "low" and time_bound == "no":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _ if priority == "medium" and time_bound == "yes":
        print(f"Reminder: '{task}' is a medium priority task that should be done today!")
    case _:
        print(f"Unknown task or priority level.")