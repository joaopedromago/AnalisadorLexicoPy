from glob import glob
import shutil
import uuid

print("Processando Arquivo...")
files = glob('input/*.txt')

if len(files) == 0:
    print("Nenhum arquivo encontrado em /input!")

for fileName in files:
    print("Encontrado: " + fileName)

    # Obtendo conteúdo do arquivo
    f = open(fileName, "r+")
    code = f.read()
    f.close()

    print(code)

    retorno = "Deu certo!"

    print("Resultado: " + retorno)
    rFileName = "out/" + str(uuid.uuid4()) + ".txt"
    r = open(rFileName, "w+")
    r.write(retorno)
    r.close()
    print(rFileName)
    # Caso sucesso:
    shutil.move(fileName, "processed/")

    print("Arquivo processado e movido para /processed")
    print("Retorno salvo em /" + rFileName + "!")
    pass

print("Fim da execução do programa.")
