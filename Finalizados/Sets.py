'''
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is both unordered and unindexed.

Sets are written with curly brackets.

Note: Sets are unordered, so you cannot be sure in which order the items will appear.
Set items are unordered, unchangeable, and do not allow duplicate values.
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
Once a set is created, you cannot change its items, but you can add new items.
Duplicate values will be ignored:
'''

# Declarando um set:
set1 = {"apple", "banana", "cherry"};
set2 = {1, 5, 7, 9, 3};
set3 = {True, False, False};
set4 = {"abc", 34, True, 40, "male"};
thisset = set(("apple", "banana", "cherry")); # Usando construtor
my_set = {1.0, "Hello", (1, 2, 3)};

# Tamanho de um set:
tamanho = len(set1);

# Tipo de um set:
tipo = type(set1); # Retorna uma classe específica compile

# Percorrer um set:
for x in set1:
	print(x);

# Checar se algo pertence a um set:
print("banana" in set1); # Printa o booleano

# Adicionando itens:
set4.add("novo_item");
set4.update(set1); # Adiciona o set1 ao set4
mylist = ["kiwi", "orange"];
set4.update(mylist); # Adicona um por um os itens da lista

# Removendo itens:
set4.remove("novo_item");
set4.discard(mylist);
set4.pop(); # Remove o último item do set
set1.clear(); # Remove todos os itens de um set
del set1; # Deleta o set

# Operando sets:
set1 = {"a", "b" , "c"};
set2 = {1, 2, 3};
set3 = set1.union(set2); # Retorna a união dos dois
x = {"apple", "banana", "cherry"};
y = {"google", "microsoft", "apple"};
z = x.intersection(y); # Retorna a intersecção de x com y
x.intersection_update(y); # X se torna a intersecção dele com y
z = x.symmetric_difference(y); # Retorna o que há de diferente entre x e y
z = x.difference(y); # X se torna o que há nele que não há em y
x.symmetric_difference_update(y); # X se torna o que tem diferente entre ele e y



# Mais alguns métodos e propriedades: ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others
# all()	Returns True if all elements of the set are true (or if the set is empty).
# any()	Returns True if any element of the set is true. If the set is empty, returns False.
# enumerate()	Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
# len()	Returns the length (the number of items) in the set.
# max()	Returns the largest item in the set.
# min()	Returns the smallest item in the set.
# sorted()	Returns a new sorted list from elements in the set(does not sort the set itself).
# sum()	Returns the sum of all elements in the set.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
