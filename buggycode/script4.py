

def func1(list_of_names):
    for i, name in enumerate(list_of_names):
        list_of_names[i] = name + "!"

    func2(list_of_names)  

    return list_of_names  

def func2(list_of_names):
    greeting = "Hello, "
    for i, name in enumerate(list_of_names):
        list_of_names[i] = greeting + name
    
    func3(list_of_names)

def func3(list_of_names):
    end_greeting = " How are you?"
    for i, name in enumerate(list_of_names):
        list_of_names[i] = name + end_greeting


def main():
    names = ["Jeremy", "Rocky"]
    new_names = func1(names)
    print(new_names)

if __name__ == "__main__":
    main()