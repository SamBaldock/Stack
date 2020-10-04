class Stack: #Creating the stack as a class
    def __init__(self):
        self.stack = []#Creating a self.items variable that stores the values
                        #Which all the functions can use and edit

    def Is_Empty(self):
        return self.stack == [] #Checks to see if the stack is Is Empty

    def Push(self, data, max):
        if len(self.stack) == max:
            print('The stack is full')#Chekcs to see if an element can be pushes
                                      #If the stack is full it cant
        else:
            self.stack.append(data)#If not it pushes the item
    def Pop(self):
            return self.stack.pop()#Removes and returns the last item
    def Peak(self):
            return self.stack[(len(self.stack)-1)]#Returns the last item in the array
            #but doesnt remove it


USER_STACK = Stack()
Max = int(input("How long do you want the stack? -->")) #Assigning th estack length
while True:
    print('push <number> (PUSHES A NUMBER ONTO THE STACK)')#Asking the user for their option
    print('Pop (REMOVES AND RETURNS LAST VALUE)')
    print("Peak (SHOWS YOU THE LAST ITEM ON THE STACK)")
    print('Quit (QUITS)')
    user_select = input('What would you like to do? ').split()

    option = user_select[0].strip().lower()#Makes sure the option in lower case
    if option == 'push':
        USER_STACK.Push(int(user_select[1]),Max)
    elif option == 'pop':
        if USER_STACK.Is_Empty():
            print('Stack is empty.')#Makes sure the stack is populated before
            popping
        else:
            print('Popped value: ', USER_STACK.Pop())
    elif option == "peak":
        if USER_STACK.Is_Empty():
            print('Stack is empty.')
        else:
            print('peaked value: ', USER_STACK.Peak())
    else:
        break
