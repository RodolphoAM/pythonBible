def greet(*names, msg="good morning"):
    #this function greets the person
    for name in names:
        print("Hello, "+name+", "+msg)

greet("Monica")
greet("Bruce", "Irwing", "Roman", msg="how do you do?")