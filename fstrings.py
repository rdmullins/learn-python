# Learning about fstring for including computed items in print strings

name = "Roger"
age = 43

print ("This is a normal print")
print ("This concantenates - my name is " + name)
print (f"Now for the fun part. I'm currently {age} years old and in ten years I'll be {age+10} years old.")
print (len(name))
print (f"So that's how many letters my name has in it. A total of {len(name)}.")