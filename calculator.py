from stack import Stack

# boolean

def is_trig(str):

    trig = ['sin', 'cos', 'tan', 'cot', 'arcsin', 'arccos', 'arctan', 'arccot']
    return str in trig


def is_log(str):

    log = ['ln', 'log']
    return str in log

def is_num(char):

    try:
        float(char)
        return True

    except (ValueError):
        pass

    try:
        import unicodedata
        unicodedata.numeric(char)
        return True
    except (TypeError, ValueError):
        pass

    return False

def is_alph(char):

    cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sml = 'abcdefghijklmnopqrstuvwxyz'

    return char in cap or char in sml

def is_operator(char):

    operators = ['+', '-', '*', '/', '^']
    return char in operators

# posrfix
def preced(char):

    if char == '+' or char == '-':

        return 1

    if char == '*' or char == '/':

        return 2

    if char == '^':

        return 3

    if is_trig(char) or is_log(char):

        return 4

    return -1

def padd(exp_list):

    ans = []
    to_cont = False

    for i in range(0, len(exp_list)):

        if to_cont:

            to_cont = False
            continue

        cr = exp_list[i]                                        # current term

        pr = '' if i == 0                 else exp_list[i - 1]  # previous term
        nx = '' if i == len(exp_list) - 1 else exp_list[i + 1]  # next term

        if pr == '' or pr == '(':

            if cr == '+': continue

            if cr == '-': ans.append('0')

        if is_trig(pr) or is_log(pr):

            if cr == '+': continue

            if cr == '-':

                ans.append('(')
                ans.append('0')
                ans.append('-')
                ans.append(nx)
                ans.append(')')

                to_cont = True
                continue

        if pr == ')':

            if cr == '(' or is_num(cr): ans.append('*')

        if is_num(pr):

            if cr == '(': ans.append('*')

        ans.append(cr)

    return ans

def to_list(exp):

    ans = []

    for term in exp:

        if term == ' ':

            continue

        last = ' '

        if ans:
            last = ans[-1]

        if is_num(term) or term == '.':

            if is_num(last):

                ans = ans[:-1]
                term = last + term
                if not is_num(term):

                    error.append('illegal number')
                    return

        if is_alph(term):

            if is_alph(last[0]) and not is_operator(last):

                ans = ans[:-1]
                term = last + term

        ans.append(term)

    return padd(ans)

class Calculator:

    # constructor
    def __init__(self):

        self.error  = []
        self.degree = True
        self.exp    = None

    def postfix(self):

        infix = to_list(self.exp)
        if not infix: return

        # final answer
        postfix = []

        # temp operator stack
        operator = Stack()

        for focus in infix:

            if focus == ' ':
                continue

            if is_num(focus):

                postfix.append(focus)

            elif focus == '(':

                operator.push(focus)

            elif focus == ')':

                top = operator.peek()

                while top != '(':

                    postfix.append(top)
                    operator.pop()

                    if operator.is_empty():

                        error.append('parenthesis mismatch')
                        return

                    top = operator.peek()

                # poping the closing parenthesis
                operator.pop()

            elif is_operator(focus):

                if not operator.is_empty():

                    top = operator.peek()

                    while preced(focus) <= preced(top):

                        postfix.append(top)
                        operator.pop()

                        if operator.is_empty():
                            break

                        top = operator.peek()

                operator.push(focus)

        while not operator.is_empty():

            top = operator.peek()
            if top == '(':

                error.append('parenthesis mismatch')
                return

            postfix.append(top)
            operator.pop()

        return postfix

    # evaluate postfix

    def evaluate(exp):

        postfix = to_postfix(exp)

        if not postfix:

            return

        value = Stack()

        for focus in postfix:

            if is_num(focus):

                value.push(focus)

            elif is_trig(focus) or is_log(focus):

                if value.is_empty():

                    error.append('missing operand')
                    return

                num = value.pop()
                to_push = perform(num, focus)
                value.push(to_push)

            else:

                if value.is_empty():

                    error.append('missing operand')
                    return

                num_1 = value.pop()

                if value.is_empty():

                    error.append('missing operand')
                    return

                num_2 = value.pop()

                to_push = perform(num_2, focus, num_1)

                if to_push == None:

                    error.append('invalid operation')
                    return

                value.push(to_push)

        ans = value.pop()

        if not value.is_empty():

            error.append('extra operand')
            return

        return ans


    def evaluate(self, exp):

        self.exp = exp
        postfix = self.postfix()

        if not postfix:

            print 'no postfix found'
            return

        value = Stack()

        for focus in postfix:

            if is_num(focus):

                value.push(focus)

            elif is_trig(focus) or is_log(focus):

                if value.is_empty():

                    self.error.append('missing operand')
                    return

                num = value.pop()
                to_push = self.perform(num, focus)
                value.push(to_push)

            else:

                if value.is_empty():

                    error.append('missing operand')
                    return

                num_1 = value.pop()

                if value.is_empty():

                    error.append('missing operand')
                    return

                num_2 = value.pop()

                to_push = self.perform(num_2, focus, num_1)

                if to_push == None:

                    error.append('invalid operation')
                    return

                value.push(to_push)

        ans = value.pop()

        if not value.is_empty():

            error.append('extra operand')
            return

        return ans


    def perform(self, n, op, m = None):

        import math

        n = float(n)

        if is_log(op):

            if (n < 0):

                error.append('log n undefined')
                return

            return math.log(n)

        if is_trig(op):

            org_n = n # save the original value

            if (self.degree):

                n = math.radians(n)

            if op == 'sin':

                return math.sin(n)

            if op == 'cos':

                return math.cos(n)

            if op == 'tan':

                if math.cos(n) == 0:

                    error.append('tangent undefined')
                    return

                return math.tan(n)

            if op == 'cot':

                if math.tan(n) == 0:

                    error.append('cotangent undefined')
                    return

                return 1 / math.tan(n)

            n = org_n

            if n > 1 or n < -1:

                error.append('inverse trig undefined')
                return

            if op == 'arcsin':

                return math.asin(n)

            if op == 'arccos':

                return math.acos(n)

            if op == 'arctan':

                return math.atan(n)

            if op == 'arccot':

                if n == 0:

                    error.append('cotangent undefined')
                    return

                return math.atan(1 / n)

        m = float(m)

        if op == '+':

            return n + m

        if op == '-':

            return n - m

        if op == '*':

            return n * m

        if op == '/':

            if m == 0:

                error.append('division by 0')
                return

            return n / m

        if op == '^':

            return pow(n, m)

        return

c = Calculator()
print c.evaluate('5 + 4')
