from glob import glob
import shutil
import io

# Constantes
OPER = "+-*:"
ALG = "0123456789"
LETRA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
RESERVADAS = ["for", "while", "if", "else", "int", "float", "string"]

# Início de execução
print("Processando Arquivo...")
files = glob('input/*.txt')

if len(files) == 0:
    print("Nenhum arquivo encontrado em /input!")

for fileName in files:
    print("Encontrado: " + fileName)

    test = 1
    currentLine = 0

    retornos = ""
    # Obtendo conteúdo do arquivo
    f = io.open(fileName, mode="r", encoding="utf-8")
    for code in f.readlines():
        i = 0
        currentLine = currentLine + 1
        state = 0

        # Validando se há alguma variável reservada
        for ELEMENT in RESERVADAS:
            if code.find(ELEMENT) != -1:
                test = 0
            pass

        if test == 0:
            break

        print("\nTesting: " + code)
        while state < 33:
            EOF = 0
            word = "None"

            if i >= len(code):
                EOF = 1
            elif code[i] == "\0" or code[i] == "\n":
                EOF = 1
            else:
                word = code[i]

            # print("i: " + str(i) + " len: " + str(len(code)) + " w: " +
            #       word + " state: " + str(state) + " EOF: " + str(EOF))

            if state == 0:  # b0 | /1 | l4
                if word == " ":
                    state = 0
                elif LETRA.find(word) != -1:
                    state = 4
                elif word == "/":
                    state = 1
                else:
                    test = 0
                    state = 999
            elif state == 1:  # *2
                if word == "*":
                    state = 2
                else:
                    test = 0
                    state = 999
            elif state == 2:  # *3 | qq2
                if word != "*" and word != "None":
                    state = 2
                elif word == "*":
                    state = 3
                else:
                    test = 0
                    state = 999
            elif state == 3:  # /0 | qq2 | *3
                if word == "/":
                    state = 0
                elif word != "/" and word != "*" and word != "None":
                    state = 2
                elif word == "*":
                    state = 3
                else:
                    test = 0
                    state = 999
            elif state == 4:  # l4 | a5 | b6 | /7 | =10
                if LETRA.find(word) != -1:
                    state = 4
                elif ALG.find(word) != -1:
                    state = 5
                elif word == " ":
                    state = 6
                elif word == "/":
                    state = 7
                elif word == "=":
                    state = 10
                else:
                    test = 0
                    state = 999
            elif state == 5:  # a5 | b6 | /7 | =10
                if ALG.find(word) != -1:
                    state = 5
                elif word == " ":
                    state = 6
                elif word == "/":
                    state = 7
                elif word == "=":
                    state = 10
                else:
                    test = 0
                    state = 999
            elif state == 6:  # b6 | /7 | =10
                if word == " ":
                    state = 6
                elif word == "/":
                    state = 7
                elif word == "=":
                    state = 10
                else:
                    test = 0
                    state = 999
            elif state == 7:  # *8
                if word == "*":
                    state = 8
                else:
                    test = 0
                    state = 999
            elif state == 8:  # qq8 | *9
                if word != "*" and word != "None":
                    state = 8
                elif word == "*":
                    state = 9
                else:
                    test = 0
                    state = 999
            elif state == 9:  # /6 | qq8 | *9
                if word == "/":
                    state = 6
                elif word != "/" and word != "*" and word != "None":
                    state = 8
                elif word == "*":
                    state = 9
                else:
                    test = 0
                    state = 999
            elif state == 10:  # b10 | /11 | l14 | a15
                if word == " ":
                    state = 10
                elif word == "/":
                    state = 11
                elif LETRA.find(word) != -1:
                    state = 14
                elif ALG.find(word) != -1:
                    state = 15
                else:
                    test = 0
                    state = 999
            elif state == 11:  # *12
                if word == "*":
                    state = 12
                else:
                    test = 0
                    state = 999
            elif state == 12:  # *qq12 | *13
                if word != "*" and word != "None":
                    state = 12
                elif word == "*":
                    state = 13
                else:
                    test = 0
                    state = 999
            elif state == 13:  # /10 | qq12 | *13
                if word == "/":
                    state = 10
                elif word != "/" and word != "*" and word != "None":
                    state = 12
                elif word == "*":
                    state = 13
                else:
                    test = 0
                    state = 999
            elif state == 14:  # l14 | a15 | b16 | /17 | op20
                if LETRA.find(word) != -1:
                    state = 14
                elif ALG.find(word) != -1:
                    state = 15
                elif word == " ":
                    state = 16
                elif word == "/":
                    state = 17
                elif OPER.find(word) != -1:
                    state = 20
                else:
                    test = 0
                    state = 999
            elif state == 15:  # a15 | b16 | /17 | op20
                if ALG.find(word) != -1:
                    state = 15
                elif word == " ":
                    state = 16
                elif word == "/":
                    state = 17
                elif OPER.find(word) != -1:
                    state = 20
                else:
                    test = 0
                    state = 999
            elif state == 16:  # b16 | /17 | op20
                if word == " ":
                    state = 16
                elif word == "/":
                    state = 17
                elif OPER.find(word) != -1:
                    state = 20
                else:
                    test = 0
                    state = 999
            elif state == 17:  # *18 | /21 | b20 | l24 | a25
                if word == "*":
                    state = 18
                elif word == "/":
                    state = 21
                elif word == " ":
                    state = 20
                elif LETRA.find(word) != -1:
                    state = 24
                elif ALG.find(word) != -1:
                    state = 25
                else:
                    test = 0
                    state = 999
            elif state == 18:  # qq18 | *19
                if word != "*" and word != "None":
                    state = 18
                elif word == "*":
                    state = 19
                else:
                    test = 0
                    state = 999
            elif state == 19:  # /16 | qq18 | *19
                if word == "/":
                    state = 16
                elif word != "/" and word != "*" and word != "None":
                    state = 18
                elif word == "*":
                    state = 19
                else:
                    test = 0
                    state = 999
            elif state == 20:  # b20 | /21 | l24 | a25
                if word == " ":
                    state = 20
                elif word == "/":
                    state = 21
                elif LETRA.find(word) != -1:
                    state = 24
                elif ALG.find(word) != -1:
                    state = 25
                else:
                    test = 0
                    state = 999
            elif state == 21:  # *22
                if word == "*":
                    state = 22
                else:
                    test = 0
                    state = 999
            elif state == 22:  # qq22 | *23
                if word != "*" and word != "None":
                    state = 22
                elif word == "*":
                    state = 23
                else:
                    test = 0
                    state = 999
            elif state == 23:  # /20 | qq22 | *23
                if word == "/":
                    state = 20
                elif word != "/" and word != "*" and word != "None":
                    state = 22
                elif word == "*":
                    state = 23
                else:
                    test = 0
                    state = 999
            elif state == 24:  # l24 | a25 | b26 | /27 | op20 | ;30
                if LETRA.find(word) != -1:
                    state = 24
                elif ALG.find(word) != -1:
                    state = 25
                elif word == " ":
                    state = 26
                elif word == "/":
                    state = 27
                elif OPER.find(word) != -1:
                    state = 20
                elif word == ";":
                    state = 30
                else:
                    test = 0
                    state = 999
            elif state == 25:  # a25 | b26 | /27 | op20 | ;30
                if ALG.find(word) != -1:
                    state = 25
                elif word == " ":
                    state = 26
                elif word == "/":
                    state = 27
                elif OPER.find(word) != -1:
                    state = 20
                elif word == ";":
                    state = 30
                else:
                    test = 0
                    state = 999
            elif state == 26:  # b26 | /27 | op20 | ;30
                if word == " ":
                    state = 26
                elif word == "/":
                    state = 27
                elif OPER.find(word) != -1:
                    state = 20
                elif word == ";":
                    state = 30
                else:
                    test = 0
                    state = 999
            elif state == 27:  # *28 | b20 | /21 | l24 | a25
                if word == "*":
                    state = 28
                elif word == " ":
                    state = 20
                elif word == "/":
                    state = 21
                elif LETRA.find(word) != -1:
                    state = 24
                elif ALG.find(word) != -1:
                    state = 25
                else:
                    test = 0
                    state = 999
            elif state == 28:  # qq28 | *29
                if word != "*" and word != "None":
                    state = 28
                elif word == "*":
                    state = 29
                else:
                    test = 0
                    state = 999
            elif state == 29:  # /26 | qq28 | *29
                if word == "/":
                    state = 26
                elif word != "/" and word != "*" and word != "None":
                    state = 28
                elif word == "*":
                    state = 29
                else:
                    test = 0
                    state = 999
            elif state == 30:  # /31 | b30 | y
                if word == " ":
                    state = 30
                elif word == "/":
                    state = 31
                elif EOF == 1:
                    state = 999
                else:
                    test = 0
                    state = 999
            elif state == 31:  # /32 | *33
                if word == "/":
                    state = 32
                elif word == "*":
                    state = 33
                else:
                    test = 0
                    state = 999
            elif state == 32:  # *33
                if word == "*":
                    state = 33
                else:
                    test = 0
                    state = 999
            elif state == 33:  # qq33 | *34
                if word != "*" and word != "None":
                    state = 33
                elif word == "*":
                    state = 34
                else:
                    test = 0
                    state = 999
            elif state == 34:  # /35 | qq33 | *34
                if word == "/":
                    state = 35
                elif word != "/" and word != "*" and word != "None":
                    state = 33
                elif word == "*":
                    state = 34
                else:
                    test = 0
                    state = 999
            elif state == 35:  # /31 | y
                if word == "/":
                    state = 31
                elif EOF == 1:
                    state = 0
                else:
                    test = 0
                    state = 999

            i = i + 1
            pass

        retorno = str(currentLine) + ": String Válida!"
        if test == 0:
            retorno = "String Inválida, erro na linha: " + str(currentLine)
        print("Resultado: " + retorno)
        retornos = retornos + "\n" + retorno
        test = 1
        pass

    f.close()

    # Gerando arquivo de saída
    rFileName = "out/" + fileName.split("\\")[1]
    r = io.open(rFileName, mode="w", encoding="utf-8")
    r.write(retornos)
    r.close()
    print("\nRetorno salvo em /" + rFileName + "!")
    pass

print("Fim da execução do programa.")
