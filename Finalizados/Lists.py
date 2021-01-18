"""
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

	.List is a collection which is ordered and changeable. Allows duplicate members.
	.Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
	.Set is a collection which is unordered and unindexed. No duplicate members.
	.Dictionary is a collection which is unordered and changeable. No duplicate members.
"""

# Declarando uma lista:
lista1 = ["um", "dois", "três"];
lista2 = [1,2,3];
lista3 = ["um", 2, 2.5, "um", True, False];

# Acessando um valor de uma lista -> Valem as mesmas regras do array:
Um = lista2[0];
Três = lista1[-1];
intervalo1 = lista2[0:2];
intervalo2 = lista3[1:3];
intervalo3 = lista3[2:];
intervalo4 = lista3[-4:-1];

# Tamanho de uma lista:
tamanho = len(lista1);

# Tipo de data em uma lista:
tipo = type(lista2); # Retorna <class 'list'>

# Usando o construtor:
lista4 = list(("a", "b", "c"));

# Checar se algo existe em uma lista:
if "um" in lista1:
	print("Sim, 'um' faz parte da lista");

# Alterando valores únicos ou de um intervalo:
thislist = ["apple", "banana", "cherry"];
thislist[1] = "blackcurrant";
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"];
thislist[1:3] = ["blackcurrant", "watermelon"];
thislist = ["apple", "banana", "cherry"];
thislist[1:2] = ["blackcurrant", "watermelon"];
thislist = ["apple", "banana", "cherry"];
thislist[1:3] = ["watermelon"];

# Inserir valores:
thislist = ["apple", "banana", "cherry"];
tropical = ["mango", "pineapple", "papaya"];
thislist.insert(2, "watermelon"); # Insere "watermelon" na posição de index 2 (3º item)
thislist.append("orange"); # Insere ao fim da lista
thislist.extend(tropical); # thislist = thislist + tropical; -> Serve para concatenar qualquer tipo de objeto (tupla, set, dicionário, etc) a uma lista.

# Remover valores:
thislist.remove("banana");
thislist.pop(1); # Remove o item de index 1
thislist.pop(); # Remove o último item
del thislist[0]; # Remove item de index 0
thislist.clear(); #Limpa todo o conteúdo da lista (lista = [])
del thislist; # Deleta a lista toda

# Percorrendo uma lista
thislist = ["apple", "banana", "cherry"];
for x in thislist: # Usando for para referenciar o item
  print(x);
for i in range(len(thislist)): # Usando for para referenciar o index
  print(thislist[i]);
i = 0;
while i < len(thislist): # Usando while
  print(thislist[i]);
  i = i + 1;
[print(x) for x in thislist]; # Usando list comprehension

# List comprehension:
# newlist = [expression for item in iterable if condition == True], exemplos:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"];
newlist = [x for x in fruits if "a" in x];
newlist = [x for x in fruits if x != "apple"]; # Only accept items that are not "apple"
newlist = [x for x in fruits]; # With no if statement -> Just a copy
newlist = [x for x in range(10)]; # You can use the range() function to create an iterable
newlist = [x for x in range(10) if x < 5]; # Accept only numbers lower than 5
newlist = [x.upper() for x in fruits]; # Set the values in the new list to upper case
newlist = ['hello' for x in fruits]; # Set all values in the new list to 'hello
newlist = [x if x != "banana" else "orange" for x in fruits]; # Return "orange" instead of "banana"

# Sorting lists:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"];
thislist.sort(); # Sort the list alphabetically -> By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
thislist.sort(reverse = True); # Sort the list descending
thislist = [100, 50, 65, 82, 23];
thislist.sort(); # Sort the list numerically
thislist.sort(reverse = True); # Sort the list descending

# Customize sort function
def myfunc(n):
  return abs(n - 50);
thislist = [100, 50, 65, 82, 23];
thislist.sort(key = myfunc); # Sort the list based on how close the number is to 50

# Perform a case-insensitive sort of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"];
thislist.sort(key = str.lower);

# Inverter a ordem de uma lista:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse();

# Copiando uma lista:
thislist = ["apple", "banana", "cherry"];
mylist = thislist.copy();
mylist = list(thislist); # Usando o método list

# Mais alguns métodos e propriedades: ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
