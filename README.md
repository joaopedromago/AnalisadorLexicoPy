# Analisador Léxico em Python

## Info

Recebe um arquivo .txt de entrada
Retorna um arquivo .txt com o resultado de cada linha

Na pasta Data você encontrará a gramática e o automato das regras do analisador

## Teste

Para testar, basta colocar um arquivo .txt na pasta /input, executar "py project.py" e esperar o resultado, o programa gerará um arquivo com o mesmo nome na pasta /out com os resultados de cada linha.

## Regras Usadas

1. Deverão ser aceitos comentários da forma “/_ ... _/” que poderão ser incluídos onde existir um branco, ou seja, entre quaisquer itens léxicos da expressão.
2. A expressão poderá começar e terminar por espaços (brancos) ou por um comentário da forma “/_ ... _/”.
3. A expressão poderá:
   Começar por letras, por espaços (brancos) ou por um comentário da forma /_ ... _/;
   Terminar por letras, por algarismos, por espaços (brancos) ou por um comentário da forma /_ ... _/.
4. Considera comentários // em qualquer lugar da expressão.
5. Verifica se as variáveis têm nome de palavras reservadas.
   Exemplo: for, while, if, else, int, float, string, etc.
6. Todas as sentenças devem terminar com ; (ponto e vírgula).
7. Os espaços em branco não são removidos durante a análise.
8. Cada registro do arquivo de entrada, (cada linha) será considerado uma expressão e uma expressão será colocada totalmente em uma única linha: a expressão não poderá continuar na linha seguinte.
