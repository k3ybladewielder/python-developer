# Basic Syntax

## Declarando variáveis
nome = "João"  # Uma variável do tipo string
idade = 25  # Uma variável do tipo inteiro
altura = 1.75  # Uma variável do tipo float

# Estruturas de controle de fluxo:
## Condicionais (if-elif-else): Permitem que você execute diferentes blocos de código com base em condições.
idade = 18
if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você acabou de atingir a maioridade.")
else:
    print("Você é maior de idade.")

## Loop while: Executa um bloco de código repetidamente enquanto uma condição for verdadeira.
contador = 0
while contador < 5:
    print(contador)
    contador += 1

## Loop for: Executa um bloco de código para cada elemento em uma sequência.
nomes = ["Alice", "Bob", "Carlos"]
for nome in nomes:
    print(nome)

# Funções: As funções permitem que você agrupe um bloco de código que pode ser reutilizado.
#Você pode definir funções personalizadas ou usar funções embutidas fornecidas pelo Python. 
def saudacao(nome):
    print("Olá, " + nome + "!")

saudacao("Ana")  # Chama a função saudacao com o argumento "Ana"

# Estruturas de dados:
## Listas: Uma lista é uma coleção ordenada e mutável de elementos.
numeros = [1, 2, 3, 4, 5]

## Tuplas: Semelhante a uma lista, mas é imutável, ou seja, seus elementos não podem ser alterados após a criação.
coordenadas = (10, 20)

## Dicionários: Uma estrutura de dados que mapeia chaves a valores.
pessoa = {"nome": "João", "idade": 25}