# Prompt the user to initiate the Love Calculator

print(input("Welcome to the Love Calculator! Press any key to continue\n"))

# Prompt the user to input two names for the love calculation

name1 = input("What is your name? \n\n")
print("")
name2 = input("What is their name? \n\n")
print("") 

# Combine the inputted names into a single string

combined_string = name1 + name2 

# Convert the combined string to lowercase for consistent comparisons

lower_string = combined_string.lower()

# Count occurrences of letters 't', 'r', 'u', 'e' in the combined string 

t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e") 

true = t + r + u + e 

# Count occurrences of letters 'l', 'o', 'v', 'e' in the combined string

l = lower_string.count("l")
o = lower_string.count("o")
v = lower_string.count("v")
e = lower_string.count("e") 

love = l + o + v + e

# Combine the "true" and "love" variables

love_score = int(str(true) + str(love)) 
 
# if statement to determine the love score

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.\n")
elif (love_score > 40) and (love_score < 50):
    print(f"Your score is {love_score}, you are alright together.\n")
else: 
    print(f"Your score is {love_score}.\n")






