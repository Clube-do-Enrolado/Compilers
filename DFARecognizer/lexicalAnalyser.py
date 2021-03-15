from stringSplitter import *
from tokenGenerator import *


s = str(input())
t = []

# Lista com todas os lexemas separados.
lexeme = splitString(s)
# Loop para verificar os lexemas e criar os tokens.
for word in lexeme:
    if word in tokens["keyword"]:
        t.append(("keyword", word))
    
    elif word in tokens["operator"]:
        t.append(("operator",word))
    
    elif word in tokens["boolean"]:
        t.append(("boolean",word))
    
    elif word in tokens[":"]:
        t.append((":",word))
    
    elif is_integer(word):
        t.append(("integer",word))
    
    elif is_float(word):
        t.append(("float",word))
    
    elif is_string(word):
        t.append(("string",word))
    
    elif is_variable(word):
        t.append(("variable",word))
    
    else:
        t.append(("ERROR",word))
print(t)
