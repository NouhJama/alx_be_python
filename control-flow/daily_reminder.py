task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is is time-bound? (yes/no): " )


match task:
    case _ if priority == "high" and time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case _ if priority == "low" and time_bound == "no":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Unknown task or priority level.")