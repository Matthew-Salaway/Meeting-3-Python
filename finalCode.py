# Copy this code into your own repl. Click the navigation bar in the top left corner and go to My Repl.
# Click the New Repl on the left, create the repl, and paste the code. Or put into another IDE

# We have some important information about officers, so lets talk about it now
# Also lets explore GitHub!

# Lets review last weeks concepts with a game of MadLibs. We want to ask the user for two pieces of information and transform it into a story. First make two variables and ask the user for input to store personalized user data into the variables.
# Then, with sring concatenation, make a story out of the user input. Feel free to make your own story, or follow this example.

# Create the variable typeOfPet and store user input. Create the variable nameOfPet and store user input. Then, using string concatenation, create the variable story as: I just bought a (typeOfPet) and named it (nameOfPet). Print story

typeOfPet = input("Enter a type of animal: ")
nameOfPet = input("Enter a name: ")
story = "I just bought a " + typeOfPet + " and named it " + nameOfPet + "."
print(story)

# Now lets learn functions!
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
"""
def sayHi():
    print("Hello Scottsdale Arizona")
sayHi()
def sayHello(name, age):
    print("Hello " + name + ". You are age : " + str(age))
sayHello("Matthew", 18)
"""

# Functions are useful for code that needs to be repeated. Lets make a function that is called yearsTillOneHundred. The parameter will be the age, and the function will print how many years until the person is 100 and then return the variable. Try it!
# Need a challenge? Use if/else statments in case the age is 100, below 0, or over 100.
"""
def yearsTillOneHundred(age):
    if age < 0:
        yearsUntil = 100 - age
        print("Imagine not being born yet.")
        return yearsUntil
    if age >= 0 and age < 100:
        yearsUntil = 100 - age
        print("You only have " + str(yearsUntil) + " years until you are 100!")
        return yearsUntil
    if age == 100:
        yearsUntil = 0
        print("Congrats, you are 100!")
        return yearsUntil
    if age > 100:
        yearsUntil = 100 - age
        print("Stop flexing...")
        return yearsUntil
    else:
        print("The argument must be a number!")
        return -1
yearsTillOneHundred(-3)
yearsTillOneHundred(44)
yearsTillOneHundred(100)
yearsTillOneHundred(0)
yearsTillOneHundred(200)
storedAge = yearsTillOneHundred(44)
print(storedAge)
"""

# Lets create a function that calls on another function! How about a greeing, followed by how many more years until 100. Name the funtion greetingCard. Call the say hello function, and then the yearsTillOneHundred function.
"""
def greetingCard(name, age):
    sayHello(name, age)
    yearsTillOneHundred(age)
greetingCard("Matthew", 18)
"""
