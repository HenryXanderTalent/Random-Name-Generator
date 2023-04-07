import random

num_input = 0

names = set()

def addNames():
    #and not user_input.isalpha()
    #check for duplicates
    user_input = '?'
    while user_input != '':
        user_input = input("Using only letters enter names to add to your shortlist: ")
        names.add(user_input)
        while user_input == '' and len(names) == 0:
            user_input = input("Please enter at least one name: ")
        else:
            while user_input != '':
                user_input = input("Add more names or press enter to stop: ")
                
                if user_input != '':
                    names.add(user_input)

            else:
                if len(names) == 1:
                    addMore = input("you only have one name in your list, the output will be very predictable, would like to add more names? Y or N: ") 
                    if addMore == 'Y' or addMore == 'y':
                        addNames()
                    else:
                        return addNumber()
                else:
                    return addNumber()

    return addNumber();

def addNumber():

    num_input = input(f"Enter a number between 1 and {len(names)}: ")

    newN = int(num_input)

    while newN > len(names) or newN <= 0:
        num_input = input(f"Number entered must be between 1 and {len(names)} inclusive: ")
        
        newN = int(num_input)

    else:
        newN = int(num_input)

        indices = []

        for i in range(newN):

            #rNum = None
            def newNum():
                rNum = random.randint(1, len(names))

                while rNum in indices:
                    rNum = random.randint(1, len(names))
                else:
                    return rNum
                
            indices.append(newNum())
            
            #print(indices)

        output = []

        for j in indices:
            nameList = list(names)
            output.append(nameList[j-1])
            #print(nameList[j-1])
           
        return output
    
    #newN = int(num_input)

    #if newN <= 0:
        
       # return 'Number should be positive'
    #else:
       # return newN

print(addNames())

#print(type(num_input))

#addNames()

