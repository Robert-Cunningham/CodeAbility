# call === result of
# return result of multiply with parameters x plus two and y plus four

# return (expression) -> nil
# result of (function name) with parameters (list) -> expression
# (expression plus expression) -> expression
# expression and expression -> list

from lark import Lark, Transformer
import traceback

grammar = open('pythonicEnglish.lark').read()

parser = Lark(grammar, start='statement', debug=True)

def list_to_str(l):
    return "[" + ''.join([x + "," for x in l])[:-1] + "]"

class PythonTransformer(Transformer):
    def sum(self, items):
        return items[0] + "+" + items[1]

    def difference(self, items):
        return items[0] + "-" + items[1]
    
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
        return str(items[0])
    
    def drv(self, items):
        return str(items[0])
    
    def WORD(self, items):
        return items[0]
    
    def ifelse(self, items): #if (1) then (2) elif (3) then (4) elif (5) then (6) else (7)
        print(items)
        out = ""
        ifpart = "if " + items[0] + ":\n\t" + items[1] + "\n"

        out += ifpart

        hasElse = len(items) % 2 == 1
        elifCount = (len(items) - (2 + (1 if hasElse else 0))) // 2

        for i in range(elifCount):
            out += "elif " + items[2*i + 2] + ":\n\t" + items[2*i + 2 + 1] + "\n"
        
        if hasElse:
            out += "else:\n\t"  + items[-1] + "\n"
        
        return out
    
    def equals(self, items):
        return items[0] + " == " + items[1]

    def definition(self, items):
        fn = items[0]
        args = items[1]
        body = items[2]
        
        return "def " + fn + "(" + args + "):\n\t" + body

    
    def return_(self, items):
        return "return " + items[0]

def english_to_python(english):
    try:
        tree = parser.parse(english)
        print(tree.pretty())
        out = PythonTransformer().transform(tree)
        return out
    except Exception as e:
        print(" Does not compile.")
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
define fib with parameters n and body 
if n equals 0 then return 0
otherwise if n equals 1 then return 1
else return result of fib with parameters quantity n minus 1 plus result of fib with parameters quantity n minus two
done
"""

#print(english_to_python(dump_newlines(fib)))
