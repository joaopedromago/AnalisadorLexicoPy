from glob import glob
import shutil
import io

# Constantes
OPER = "+-*:"
ALG = "0123456789"
LETRA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

        print("\nTesting: " + code)
        # Validando se há alguma variável reservada
        while state < 52:
            EOF = 0
            word = "None"

            if i >= len(code):
                EOF = 1
            elif code[i] == "\0" or code[i] == "\n":
                EOF = 1
            else:
                word = code[i]

            if state == 0:  # i1 | w3 | f4 | d5 | c6 | v7 | p2 | e27 | s29 | b48 | qq9
                if word == "i":
                    state = 1
                elif word == "w":
                    state = 3
                elif word == "f":
                    state = 4
                elif word == "d":
                    state = 5
                elif word == "c":
                    state = 6
                elif word == "v":
                    state = 7
                elif word == "p":
                    state = 2
                elif word == "e":
                    state = 27
                elif word == "s":
                    state = 29
                elif word == "b":
                    state = 48
                else:
                    state = 9
            elif state == 1:  # f10 | n12 | qq9
                if word == "f":
                    state = 10
                elif word == "n":
                    state = 12
                else:
                    state = 9
            elif state == 2:  # u8 | r37 | qq9
                if word == "u":
                    state = 8
                elif word == "r":
                    state = 37
                else:
                    state = 9
            elif state == 3:  # h13 | qq9
                if word == "h":
                    state = 13
                else:
                    state = 9
            elif state == 4:  # o16 | l30 | qq9
                if word == "o":
                    state = 16
                elif word == "l":
                    state = 30
                else:
                    state = 9
            elif state == 5:  # o17 | qq9
                if word == "o":
                    state = 17
                else:
                    state = 9
            elif state == 6:  # o21 | l22 | a36 | h7 | qq9
                if word == "o":
                    state = 21
                elif word == "l":
                    state = 22
                elif word == "a":
                    state = 36
                elif word == "h":
                    state = 7
                else:
                    state = 9
            elif state == 7:  # a16 | qq9
                if word == "a":
                    state = 16
                else:
                    state = 9
            elif state == 8:  # b38 | qq9
                if word == "b":
                    state = 38
                else:
                    state = 9
            elif state == 9:  # qq9 | bl0 | op0 | =1
                if word == " ":
                    state = 0
                elif word == "=":
                    state = 0
                elif OPER.find(word) != -1:
                    state = 0
                else:
                    state = 9
            elif state == 10:  # qq9 | bl11 | op11 | =11 | y
                if word == " ":
                    state = 11
                elif word == "=":
                    state = 11
                elif OPER.find(word) != -1:
                    state = 11
                elif EOF == 1:
                    test = 0
                    state = 999
                else:
                    state = 9
            elif state == 11:  # y
                test = 0
                state = 999
            elif state == 12:  # t10 | qq9
                if word == "t":
                    state = 10
                else:
                    state = 9
            elif state == 13:  # i14 | qq9
                if word == "i":
                    state = 14
                else:
                    state = 9
            elif state == 14:  # l15 | qq9
                if word == "l":
                    state = 15
                else:
                    state = 9
            elif state == 15:  # e10 | qq9
                if word == "e":
                    state = 10
                else:
                    state = 9
            elif state == 16:  # r10 | qq9
                if word == "r":
                    state = 10
                else:
                    state = 9
            elif state == 17:  # u18 | qq9 | bl11 | op11 | =11 | y
                if word == "u":
                    state = 18
                elif word == " ":
                    state = 11
                elif word == "=":
                    state = 11
                elif OPER.find(word) != -1:
                    state = 11
                elif EOF == 1:
                    test = 0
                    state = 999
                else:
                    state = 9
            elif state == 18:  # b19 | qq9
                if word == "b":
                    state = 19
                else:
                    state = 9
            elif state == 19:  # l20 | qq9
                if word == "l":
                    state = 20
                else:
                    state = 9
            elif state == 20:  # e10 | qq9
                if word == "e":
                    state = 10
                else:
                    state = 9
            elif state == 21:  # n25 | qq9
                if word == "n":
                    state = 25
                else:
                    state = 9
            elif state == 22:  # a23 | qq9
                if word == "a":
                    state = 23
                else:
                    state = 9
            elif state == 23:  # s24 | qq9
                if word == "s":
                    state = 24
                else:
                    state = 9
            elif state == 24:  # s10 | qq9
                if word == "s":
                    state = 10
                else:
                    state = 9
            elif state == 25:  # s26 | qq9
                if word == "s":
                    state = 26
                else:
                    state = 9
            elif state == 26:  # t10 | qq9
                if word == "t":
                    state = 10
                else:
                    state = 9
            elif state == 27:  # l28 | qq9
                if word == "l":
                    state = 28
                else:
                    state = 9
            elif state == 28:  # s20 | qq9
                if word == "s":
                    state = 20
                else:
                    state = 9
            elif state == 29:  # t32 | w44 |qq9
                if word == "t":
                    state = 32
                elif word == "w":
                    state = 44
                else:
                    state = 9
            elif state == 30:  # o31 | qq9
                if word == "o":
                    state = 31
                else:
                    state = 9
            elif state == 31:  # a12 | qq9
                if word == "a":
                    state = 12
                else:
                    state = 9
            elif state == 32:  # r33 | qq9
                if word == "r":
                    state = 33
                else:
                    state = 9
            elif state == 33:  # i34 | qq9
                if word == "i":
                    state = 34
                else:
                    state = 9
            elif state == 34:  # n35 | qq9
                if word == "n":
                    state = 35
                else:
                    state = 9
            elif state == 35:  # g10 | qq9
                if word == "g":
                    state = 10
                else:
                    state = 9
            elif state == 36:  # s20 | qq9
                if word == "s":
                    state = 20
                else:
                    state = 9
            elif state == 37:  # i41 | qq9
                if word == "i":
                    state = 41
                else:
                    state = 9
            elif state == 38:  # l39 | qq9
                if word == "l":
                    state = 39
                else:
                    state = 9
            elif state == 39:  # i40 | qq9
                if word == "i":
                    state = 40
                else:
                    state = 9
            elif state == 40:  # c10 | qq9
                if word == "c":
                    state = 10
                else:
                    state = 9
            elif state == 41:  # v42 | qq9
                if word == "v":
                    state = 42
                else:
                    state = 9
            elif state == 42:  # a43 | qq9
                if word == "a":
                    state = 43
                else:
                    state = 9
            elif state == 43:  # t15 | qq9
                if word == "t":
                    state = 15
                else:
                    state = 9
            elif state == 44:  # i45 | qq9
                if word == "i":
                    state = 45
                else:
                    state = 9
            elif state == 45:  # t46 | qq9
                if word == "t":
                    state = 46
                else:
                    state = 9
            elif state == 46:  # c47 | qq9
                if word == "c":
                    state = 47
                else:
                    state = 9
            elif state == 47:  # h10 | qq9
                if word == "h":
                    state = 10
                else:
                    state = 9
            elif state == 48:  # r49 | qq9
                if word == "r":
                    state = 49
                else:
                    state = 9
            elif state == 49:  # e50 | qq9
                if word == "e":
                    state = 50
                else:
                    state = 9
            elif state == 50:  # a51 | qq9
                if word == "a":
                    state = 51
                else:
                    state = 9
            elif state == 51:  # k10 | qq9
                if word == "k":
                    state = 10
                else:
                    state = 9
            if EOF == 1:
                state = 999

            i = i + 1
            pass

        if test == 1:
            i = 0
            state = 0
            # Validando regras da linguagem
            while state < 33:
                EOF = 0
                word = "None"

                if i >= len(code):
                    EOF = 1
                elif code[i] == "\0" or code[i] == "\n":
                    EOF = 1
                else:
                    word = code[i]

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
