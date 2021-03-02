def addition(variable1,variable2):
    return variable1+variable2

quit=""
while quit != "q":
    try:
        variable1=int(input("Please enter the first number: "))
        variable2=int(input("Please enter the second number: "))
    except ValueError:
        print("Please enter a intager")
    except:
        print("There was an error, please try agian")
    else:
        answer=addition(variable1,variable2)
        print(f"{variable1} + {variable2} = {answer}23")
    
    quit=input("Would you like to continue (q to quit)?")