"""
    Implementação de autômatos finitos determinísticos capazes
    de reconhecer expressões regulares/cadeias.

    Autor: Vitor Acosta da Rosa
"""


from expressionreader import ExpReader

#expr = {
#        "0":{"0":"1"},
#        "1":{"1":"2"},
#        "2":{"0":"-1"}
#       }

def recognize(q0, sequence, expression):
    char_count = 0
    actual_state = q0
    

    for c in sequence:
        
        if c not in expression[actual_state].keys():
            print(f"Changing to {q0} state\n")
            actual_state = q0

        print(f"\nActual char: {c} -- ",end="")
        
        # expression[actual_state].keys() retorna todas as chaves
        # e consequentemente, todos caracteres que podem ser
        # reconhecidos pela expressão.
        if c in expression[actual_state].keys():
            print("Read:",c,end=" ")            
            temp = actual_state
            actual_state = expression[temp][c]
            print("Actual state: ",actual_state)

            if actual_state == "-1":
                return True          
            
        char_count += 1 
   
    return False


raw_expr = input(str("Insira a expressão: "))
expr = ExpReader(raw_expr)
e_dict = expr.get_dictionary()
print("Dicionário detectado: \n",e_dict)

s = input(str("Insira a sequencia: "))

print(recognize("0",s,e_dict))
