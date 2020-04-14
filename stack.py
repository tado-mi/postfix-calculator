class stack_node:

    # constructor
    def __init__(self, data = None, next_link = None):

        self.data      = data
        self.next_link = next_link

    # print
    def disp(self):

        print self.data

class Stack:

    # constructor
    def __init__(self, top = None):

        self.top = top

    # classical methods
    def push(self, data):

        temp     = stack_node(data, self.top)
        self.top = temp


    def pop(self):

        temp     = self.top.data
        self.top = self.top.next_link

        return temp


    def peek(self):

        return self.top.data

    def is_empty(self):

        return (self.top == None)

    # print
    def disp(self):

        temp = self.top

        while (temp != None):

            temp.disp()
            temp = temp.next_link

        print '_________________\n'

# demo test function
def demo():

    s = Stack()

    s.push(12)
    s.push('sunflower seeds')
    s.push(3)
    s.push('cabbage')

    print 'displaying:'
    s.disp()

    print 'popping:'
    s.pop()

    print 'peek: '
    print s.peek()

    print 'displaying: '
    s.disp()
