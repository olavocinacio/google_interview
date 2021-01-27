'''
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.

Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
Since tuple are indexed, tuples can have items with the same value.
'''

# Declarando uma tupla:
thistuple = ("apple", "banana", "cherry", "apple", "cherry");
thistuple1 = ("apple",);
tuple1 = ("abc", 34, True, 40, "male");
thistuple = tuple(("apple", "banana", "cherry")) # Usando construtor -> note as aspas duplas

# Tamanho de uma tupla:
tamanho = len(thistuple);

# Tipo:
tipo = type(thistuple); # Retorna uma classe do tipo tupla

# Acessando items:
mnaçã = thistuple[0];
banana = thistuple[1];
cereja2 = thistuple[-1]; # A referência negativa utilizada em outrs estruturas também funciona
nova_tupla = thistuple[0:1]; # Referencia-se um intervalo da mesma forma que nas outras estruturas
nova_tupla = thistuple[-2:-1];

# Checando se um item existe:
if "apple" in thistuple: print("ok");

# Convertendo uma tupla em lista:
lista = list(thistuple); # Após transformar uma tupla em uma lista, você pode operá-la como quiser
thistuple = tuple(lista);  # depois de operada, você pode retornar ao estado imútavel de tupla

# Deletando uma tupla:
del thistuple;

# "DEsempacotando uma tupla":
fruits = ("apple", "banana", "cherry"); # Tupla empacotada (Vários valores em uma variável);
(green, yellow, red) = fruits; # Cria três variáveis (green,yellow, red) e assimila os respectivos valores da tupla
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry");
(green, yellow, *red) = fruits; # red recebe todas as que sobram
fruits = ("apple", "mango", "papaya", "pineapple", "cherry");
(green, *tropic, red) = fruits; # green recebe a primeira, red a última e o resto é assimilada a tropic

# Percorrendo uma tupla:
for x in tuple1: print(x); # For comum
for i in range(len(tuple1)): # For referenciando o index
  print(tuple1[i]);
while i < len(tuple1): # Usando while
  print(tuple1[i]);
  i = i + 1;

# Unindo tuplas:
tuple1 = ("a", "b" , "c");
tuple2 = (1, 2, 3);
tuple3 = tuple1 + tuple2;

# Multiplicando tuplas
fruits = ("apple", "banana", "cherry");
mytuple = fruits * 2; # Repete a tupla duas vezes em sequência


# Mais alguns métodos e propriedades: ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
