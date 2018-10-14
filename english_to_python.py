# call === result of
# return result of multiply with parameters x plus two and y plus four

# return (expression) -> nil
# result of (function name) with parameters (list) -> expression
# (expression plus expression) -> expression
# expression and expression -> list

from lark import Lark, Transformer
import traceback
import synonyms
import re

grammar = open('pythonicEnglish.lark').read()

parser = Lark(grammar, start='start', debug=True)

def synonymize(text):
    for (k, v) in synonyms.synonyms.items():
        text = re.sub(k, v, text)
        #text = text.replace(k, v)
    return text.lower()

def list_to_str(l):
    return "[" + ''.join([x + "," for x in l])[:-1] + "]"

class PythonTransformer(Transformer):
    def sum(self, items):
        return items[0] + "+" + items[1]

    def difference(self, items):
        return items[0] + "-" + items[1]

    def product(self, items):
        return items[0] + "*" + items[1]
    
    def int(self, n):
        return str(n[0])
    
    def call(self, n):
        fn = n[0]
        args = n[1]
        return fn + "(" + args + ")"

    def list(self, list):
        return list_to_str(list)
    
    def tuple(self, items):
        return list_to_str(items)[1:-1]

    def paren_tuple(self, items):
        return "(" + list_to_str(items)[1:-1] + ")"
    
    def expression(self, items):
        return str(items[0])
    
    def statement(self, items):
        out = ""
        for i in items:
            out += "\n" + str(i)
        
        return out[1:]
    
    def drv(self, items):
        return str(items[0])
    
    def WORD(self, items):
        return items[0]
    
    def lt(self, items):
        return "<"
    def gt(self, items):
        return ">"
    def lte(self, items):
        return "<="
    def gte(self, items):
        return ">="
    def eq(self, items):
        return "=="
    
    def length(self, items):
        return "len(" + items[0] + ")"

    def comparison(self, items):
        return items[0] + " " + items[1] + " " + items[2]
    
    def set_var(self, items):
        return items[0] + " = " + items[1]
    
    def array_element(self, items):
        return items[1] + "[" + items[0] + "]"
    
    
    def ifelse(self, items): #if (1) then (2) elif (3) then (4) elif (5) then (6) else (7)
        out = ""
        ifpart = "if " + items[0] + ":\n" + items[1] + "\n"

        out += ifpart

        hasElse = len(items) % 2 == 1
        elifCount = (len(items) - (2 + (1 if hasElse else 0))) // 2

        for i in range(elifCount):
            out += "elif " + items[2*i + 2] + ":\n" + items[2*i + 2 + 1] + "\n"
        
        if hasElse:
            out += "else:\n"  + items[-1] + "\n"
        
        return out
    
    def equals(self, items):
        return items[0] + " == " + items[1]

    def definition(self, items):
        fn = items[0]
        args = items[1]
        body = items[2]
        
        return "def " + fn + "(" + args + "):\n" + body
    
    def array_comprehension(self, items):
        return "[" + items[0] + " for " + items[1] + " in " + items[2] + " if " + items[3] + "]"
    
    def end_array_elements(self, items):
        return items[1] + "[" + items[0] + ":]"
    
    def return_(self, items):
        return "return " + items[0]
    
    #------- COMMANDS --------

    def next_word(self, items):
        return "COMMAND next_word"

    def previous_word(self, items):
        return "COMMAND previous_word"

    def back(self, items):
        return "COMMAND back"

    def teleport_line(self, items):
        return "COMMAND jumpline " + items[0]

    def teleport_word(self, items):
        return "COMMAND jumpword " + items[0]
    
    def create_for_loop(self, items):
        return "CREATE for"

    def create_for_range(self, items):
        return "CREATE forr"

    def create_if(self, items):
        return "CREATE if"

    def create_def(self, items):
        return "CREATE def"

    def create_else(self, items):
        return "CREATE else"
    
    def next_(self, items):
        return "NEXT " + items[0]
    
    def quote(self, items):
        return "'" + items[0] + "'"

def english_to_python(english):
    try:
        print(english)
        english = preprocess(english)
        print(english)
        tree = parser.parse(english)
        print(tree.pretty())
        out = PythonTransformer().transform(tree)
        #print(out)
        if "NEXT" in out:
            out = out.replace("NEXT ", "")
            return {'command': 'next', 'value': out}
        if "CREATE" in out:
            out = out.replace("CREATE ", "")
            return {'command': 'create', 'value': out}
        if "COMMAND " in out:
            out = out.replace("COMMAND ", "")
            return {'command': out.split(' ')[0], 'value': ' '.join(out.split(' ')[1:])}
        else:
            return {'command': "code", 'value': out}
    except:
        traceback.print_exc()
        print("Does not compile.")
        return None

def dump_newlines(str):
    return ' '.join(str.split("\n")).strip().replace("  ", " ")

#print(english_to_python(dump_newlines("""
#if 3 then
#return call myfunction with parameters 
#3 plus 2 
#and 4 plus 6 
#and 8 plus 6 plus 3
#""")))

#print(english_to_python("if 3 equals 4 then return 4 otherwise if 6 then return 5 else return 7"))

#def F(n):
#    if n == 0: return 0
#    elif n == 1: return 1
#    else: return F(n-1)+F(n-2)

fib = """
define fibonnaci with parameters november and body 
if november equals 0 then return 0
otherwise if november equals 1 then return 1
else return result of fibonnaci of quantity november minus 1 plus result of fibbonaci of quantity november minus two
done
"""

wtf = 'Define Fibonacci with parameters November and body if November equals zero then return 0 otherwise if November equals one then return one else return result of Fibonacci of quantity November - 1 + result of Fibonacci of quantity November -2 done'
wtf2 = 'Define Fibonacci with parameters November and body if November equals zero then return 0 otherwise if November equals one then return one else return result of Fibonacci of quantity November - 1 + result of Fibonacci '
wtf3 = 'Define Fibonacci with parameters November and body if November equals zero then return zero otherwise if November equals one then return one else return result of Fibonacci of quantity November - 1 + result of Fibonacci of quantity November - 2 done'

test = "x for x in array is greater than 2 if x is less than 3"
comptest = "x is less than 3"

quick_sort = """
define sort with parameters array and body
if the length of array is less than or equal to 1 then
return array
else
set pivot to element 0 of array then
set larger to x for x in elements 1 through end of array if x is greater than pivot then
set smaller to x for x in elements 1 through end of array if x is less than or equal to pivot then
return result of sort of smaller plus list of pivot plus result of sort of larger
done
"""

#print(english_to_python(dump_newlines(wtf.lower())))
#print(english_to_python(dump_newlines(quick_sort)))

def q_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        larger = [ element for element in array[1:] if element > pivot ]
        smaller = [ element for element in array[1:] if element <= pivot ]
        return q_sort(smaller) + [pivot] + q_sort(larger)

#def e(n=10):
#    return sum(1 / float(math.factorial(i)) for i in range(n))

def preprocess(s):
    s = dump_newlines(s)
    s = s.lower()
    s = synonymize(s)
    s = s.replace("  ", " ").replace("  ", " ").replace("  ", " ")
    s = s.strip()
    return s

#print(english_to_python(fib))