#logical operators
#write a program to check if a person is eligible to vote
#The person must be a kenyan, uganda or tanzania citizen and above 18 years.
nationality = input ("Enter your nationality: ").lower()
age = int (input ("Enter your age: "))
country = ["kenya","uganda","tanzania"]
if nationality in country and age >18:
    print ("You are eligible to vote")
else: 
    print("You are not eligible to vote!")