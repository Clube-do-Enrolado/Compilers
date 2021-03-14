"""
    [PORTUGUÊS]
     | Autor: Rafael Zacarias Palierini
     | GitHub: Zakonildo
     |
     | Grupo:                NOMES               |     R.A      
     |      |- Andy Silva Barbosa                | 22.218.025-9 |
     |      |- Rafael Zacarias Palierini         | 22.218.030-9 |
     |      |- Rubens de Araujo Rodrigues Mendes | 22.218.009-3 |
     |      |- Vitor Acosta da Rosa              | 22.218.006-9 |
     |
     | 2ª Atividade Prática de Compiladores
     | Nome: Componente Separador de String em Python

     [DESCRIÇÃO]
        Este componente visa separar strings com a sintaxe em Python. Para utiliza-lo si-
        ga os comentários ao longo das funções.


    [ENGLISH]
     | Author: Rafael Zacarias Palierini
     | GitHub: Zakonildo
     |
     | Group:                NAMES               |     R.A      
     |      |- Andy Silva Barbosa                | 22.218.025-9 |
     |      |- Rafael Zacarias Palierini         | 22.218.030-9 |
     |      |- Rubens de Araujo Rodrigues Mendes | 22.218.009-3 |
     |      |- Vitor Acosta da Rosa              | 22.218.006-9 |
     |
     | Compilers 2nd Pratical Lesson
     | Name: Python String Splitter Component

    [DESCRIPTION]
        This component aims to split a string in Python's syntax. To use it, follow the
        commentaries along with the functions.
"""


# [PORTUGUÊS]
#   Está função irá filtra uma palavrar com um operador no meio dela, por exemplo "myVar=5".
#   Seu retorno deve ser uma lista e uma string. A lista deverá conter a palavra separada e
#   concatenada no fim da lista (Ex: [..., "myVar", "=", "5"]). A string retornada será o úl-
#   timoitem da separação (Ex: word="5").
#
# [ENGLISH]
#   This function will filter a word with the operator in the middle of it, for example
#   "myVar=5". The return must be a list and a string. The list should contain the word
#   splitted and appended in the end of the list (Ex. [..., "myVar", =, "5"]). The string
#   returned will be the last item of the split (Ex. word="5").
#
#   [PARAM]
#    | opMiddle(string, string, list[strings])
#    | return string, string

def opMiddle(word, newS, operator):
    word = word.replace(operator, " " + operator + " ").split(" ")
    for i in word:
        if i != "":
            newS.append(i)
    word = word[2]
    return newS, word

# [PORTUGUÊS]
#   Está função irá filtra uma palavrar com um operador no fim dela, por exemplo "else:".
#   Seu retorno deve ser uma lista e uma string. A lista deverá conter a palavra separada e
#   concatenada no fim da lista (Ex: [..., "else", ":"]). A string retornada será a palavra
#   sem o operador (Ex: word="else").
#
# [ENGLISH]
#   This function will filter a word with the operator in the end of it, for example
#   "else:". The return must be a list and a string. The list should contain the word
#   splitted and appended in the end of the list (Ex. [..., "else", ":"]). The string
#   returned will be the string without the operator (Ex. word="else").
#
#   [PARAM]
#    | opAfter(string, string, list[strings])
#    | return string, string

def opAfter(word, newS, operator):
    word = word.replace(operator, "")
    newS.append(word)
    newS.append(operator)
    return newS, word

# [PORTUGUÊS]
#   Está função irá filtra uma palavrar com um operador no começo dela, por exemplo "=myVar".
#   Seu retorno deve ser uma lista e uma string. A lista deverá conter apenas o operador sepa-
#   rado e concatenado no fim da lista (Ex: [..., "="]). A string retornada será a palavra sem
#   o operador (Ex: word="myVar").
#
# [ENGLISH]
#   This function will filter a word with the operator in the beginning of it, for example
#   "=myVar". The return must be a list and a string. The list should contain only the
#   operator splitted and appended in the end of the list (Ex. [..., "="]). The string
#   returned will be the string without the operator (Ex. word="myVar").
#
#   [PARAM]
#    | opBefore(string, string, list[strings])
#    | return string, string

def opBefore(word, newS, operator):
    newS.append(operator)
    word = word.replace(operator, "")
    return newS, word


# [PORTUGUÊS]
#   Aqui é onde a mágica acontece, essa função recebe uma string, por exemplo s="if my_Var== 5:".
#   Ela é responsável por tratar por completo essa string, a separando e retornando uma lista com
#   cada lexema separado. O tratamento é feito primeiramente separando a palavra por espaços. Em
#   seguida é feito uma segunda passagem por cada palavra para verificar se não existem operadores
#   juntos de alguma palavra, por exemplo "my_Var==". Se houver serão utilizados as funções ante-
#   riores para fazer o tratamento e retornar a lista correta com os lexemas. O retorno é a pró-
#   pria lista com os lexemas separados
#
# [ENGLISH]
#   Here is where the magic happens, this function receive a string, for example s="if my_Var== 5:".
#   It is responsable for fully processing the string, separating it by spaces. Next is made a second
#   filter by each word to verify if don't exist operators along any word, for example "my_Var==". If
#   there are operators, the functions shown before will be utilized to do the treatment and return the
#   correct list with the lexemes. The return will be the list with the lexemes splitted.
#
#   [PARAM]
#    | splitString(string)
#    | return list[strings]

def splitString(s):
    global op
    s = s.split(" ")
    newS  = []
    for word in s:
        wordTemp = word

        if word.isalpha():
            newS.append(word)

        else:
            if word in op:
                newS.append(op[op.index(word)])
                continue

            for i in op:
                if word.find(i) > -1 and word.find(i) < len(i) and word != "":
                    newS, word = opBefore(word, newS, i)
                    
            for i in op:
                if word.find(i) >= len(i) and word.find(i) < len(word) - len(i) and word != "":
                    newS, word = opMiddle(word, newS, i)

            for i in op:
                if word.find(i) >= len(word) - len(i) and word != "":
                    newS, word = opAfter(word, newS, i)

            if wordTemp == word:
                newS.append(word)

    return newS

# [PORTUGUÊS]
#   Esta é a lista de operadores. Os operadores que devem ser filtrados devem estar aqui.
#
# [ENGLISH]
#   This is the operator's list. The operators that should be filtered must be here.

op = [":", "==", "!=", "=", "+", "-", "*", "/"]

# [PORTUGUÊS]
#   Esta é a string que está sendo testada. Sinta-se livre para testar sua string!
#
# [ENGLISH]
#   This is the string that is being tested. Feel free to test your string!

s = "if: == el_se+for = / + my_Var"

# [PORTUGUÊS]
#   Imprime a lista de lexemas.
#
# [ENGLISH]
#   Print the Lexeme's List.

print(splitString(s))


