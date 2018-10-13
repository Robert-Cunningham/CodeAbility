# call === result of
# return result of multiply with parameters x plus two and y plus four

# return (expression) -> nil
# result of (function name) with parameters (list) -> expression
# (expression plus expression) -> expression
# expression and expression -> list

from lark import Lark, Transformer

parser = Lark(r"""

?expression: int
    | sum
    | call
    | word

call: "call " function_name " with parameters " tuple
    | "result of " function_name " with parameters " tuple

list: "list of" expression (" and " expression)*
    | empty_list

tuple: expression (" and " expression)*

?empty_list: "empty list"

?function_name: word

sum: expression " plus " expression

statement: return

return: "return" expression

int: NUMBER

?word: WORD

%import common.NUMBER
%import common.ESCAPED_STRING
%import common.WORD

""", start='expression')

class PythonTransformer(Transformer):
    def sum(self, items):
        return items[0] + "+" + items[1]
    
    def int(self, n):
        return "" + n[0]
    
    def call(self, n):
        fn = n[0]
        args = n[1]
        return fn + "(" + args + ")"
    
    def list(self, list):
        return str(list)
    
    def tuple(self, items):
        return str(items)[1:-1]

    def paren_tuple(self, items):
        return "(" + str(items)[1:-1] + ")"

def english_to_python(english):
    tree = parser.parse(english)
    out = PythonTransformer().transform(tree)
    return out

print(english_to_python('call myfunction with parameters 3 plus 2 and 4 plus 6'))


