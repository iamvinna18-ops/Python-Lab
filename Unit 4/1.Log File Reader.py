# Lab Exercise 1:Log File Reader

filename = "log.txt"

# Create a sample log file
with open(filename, "w") as file:
    file.write("System Started\n")
    file.write("User Logged In\n")
    file.write("Error Occurred\n")
    file.write("System Shutdown\n")

# Read the log file
with open(filename, "r") as file:
    content = file.read()

print("----- LOG FILE CONTENT -----")
print(content)

# Count lines, words and characters
lines = content.splitlines()
words = content.split()
characters = len(content)

print("Total Lines:", len(lines))
print("Total Words:", len(words))
print("Total Characters:", characters)