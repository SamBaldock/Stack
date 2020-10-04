class Stack:
    def __init__(self):
        self.stack = []

    def Is_Empty(self):
        return self.stack == []

    def Push(self, data, max):
        if len(self.stack) == max:
            print('The stack is full')
        else:
            self.stack.append(data)
    def Pop(self):
            return self.stack.pop()
    def Peak(self):
            return self.stack[(len(self.stack)-1)]


USER_STACK = Stack()
Max = int(input("How long do you want the stack? -->"))
while True:
    print('push <number> (PUSHES A NUMBER ONTO THE STACK)')
    print('Pop (REMOVES AND RETURNS LAST VALUE)')
    print("Peak (SHOWS YOU THE LAST ITEM ON THE STACK)")
    print('Quit (QUITS)')
    user_select = input('What would you like to do? ').split()

    option = user_select[0].strip().lower()
    if option == 'push':
        USER_STACK.Push(int(user_select[1]),Max)
    elif option == 'pop':
        if USER_STACK.Is_Empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', USER_STACK.Pop())
    elif option == "peak":
        if USER_STACK.Is_Empty():
            print('Stack is empty.')
        else:
            print('peaked value: ', USER_STACK.Peak())
    else:
        break
