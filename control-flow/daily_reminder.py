task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority == "high":
    message = f"'{task}' is a high priority task"
elif priority == "medium":
    message = f"'{task}' is a medium priority task"
elif priority == "low":
    message = f"'{task}' is a low priority task"
else:
    message = f"'{task}' has unknown priority"

if time_bound == "yes":
    print(f"Reminder: {message} that requires immediate attention today!")
else:
    print(f"Note: {message}. Consider completing it when you have free time.")

