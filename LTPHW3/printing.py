v1 = 'Helked'
v2 = 'damned'
v3 = 'is'
v4 = '.'

#Formatting One
print("\nFormatting 1")
print(f"1. To make a meaningful sentence first word should be {v1}{v4}")
print(f"2. As you can guess next word is {v3}{v4}")
print(f"3. And final one is {v2}{v4}")
print(f"4. As we sum up we get '{v1} {v3} {v2}{v4}'")

#Formatting Two
print("\nFormatting 2")
name = "Her name is {}"
print(name.format(v1))

#Formatting Three
print("\nFormatting 3")
print("Her name is", v1 )
print("Her name is" + v1 )

#Formatting Four
print("." * 50)

formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))

#In order to escape double quote in a string use \ such as:
print("Here is \"Example\"")

#or """
print("""
Here is "Example"
""")

print("\n")
