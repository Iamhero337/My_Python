#take the input of the from user it also prints the string which you gave with it 
name = input("What is your name?: ")

#that's how you print the input you just took in the same line of function which you called 
print("Hello,", name)
print(name)
#so it is in python documentaion that you can give the action or string to use in the last of the printed value by def it is /n
#and here what I did is gave that end nothing so it did nothing and my name was printed in the same line with it.
print("Hello, ", end='')
print(name)
#so you have got the idea of print I guess
print("Hello, ", end='RANDOM THING')
print(name)
#here is on corner case of printing the ""(You can use ' or " quote to in giving arguments both works but stick with one)
# print("Hello,'hero'")
#or
# print('Hello, "hero"')
#last(here what we did is the we used that same qote to print that thing we used bacslash to make it obvious taht it is what it is  )
# print("Hello, \"hero\"") 


'So just learnt that this is a comment'
"""And this too"""
"what about this"


#here is the last and final way to do this perfectly
print(f"Hello,{name}")


#string input clean up a little bit( it will remove the whitespaces means blank space)
name = name.strip()

print(f"Hello, {name}")

#here I will clean it and make the first word capital letter
name = name.capitalize()
# but this will fail if you give it first and last name both so

print(f"Hello, {name}")

#we will do this 
name = name.title()

print(f"Hello, {name}")


#Lets wrap things up (Everything at one place)

name = input("What is your name: ").strip().title()

print(f"Hello, what's up {name}")

