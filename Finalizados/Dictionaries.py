'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is unordered, changeable and does not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values.

Dictionary items are unordered, changeable, and does not allow duplicates. : When we say that dictionaries are unordered, it means that the items does not have a defined order, you cannot refer to an item by using an index; Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been create; Dictionaries cannot have two items with the same key (Duplicate values will overwrite existing values).

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

key:value
'''

# Declarando um dicionário:
dicionario1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
	"electric": False,
  "colors": ["red", "white", "blue"]
}; # Os dados dentro de um dicionário podem ser de qualquer tipo

# Determinando o tamanho de um dicionario:
tamanho1 = len(dicionario1);

# Tipo de um dicionario:
tipo = type(dicionario1); # Retorna uma classe própria do tipo 'dict'

# Acessando os valores pela chave:
marca = dicionario1["brand"];
modelo = dicionario1.get("model");

# Listando as chaves de um dicionário:
chaves = dicionario1.keys();

# Listando os valores de um dicionário:
valores = dicionario1.values();

# Listando os pares do dicionário em forma de tuplas:
relacoes = dicionario1.items();

# Checando se uma chave existe em um dicionário:
if "model" in dicionario1: print("ok");

# Alterando valores:
dicionario1["year"] = 2015;
dicionario1.update({"year":2020, "brand":"chevrolet", "model": "camaro"}); # com esse método, pode-se alterar vários valores ao mesmo tempo

# Adicionando itens:
dicionario1["alarme"] = True;
dicionario1.update({"vidro_eletrico": True});

# Removendo itens:
dicionario1.pop("alarme"); 
del dicionario1["electric"];
dicionario1.popitem(); # Remove o último item adicionado
# dicionario1.clear(); # Limpa o dicionário (deixa-o vazio)
# del dicionario1; # Exclui a variável dicionário

# Percorrendo um dicionário:
for x in dicionario1: print(x); # Printa as chaves
for x in dicionario1.keys(): print(x); # Printa os valores
for x in dicionario1: print(dicionario1[x]); # Printa os valores
for x in dicionario1.values(): print(x); # Printa os valores
for x,y in dicionario1.items(): print(x,y); # Printa as chaves e os valores

# Copiando um dicionário:
dicionario2 = dicionario1.copy();
dicionario3 = dict(dicionario2);

# Criando um dicionário composto (que possui dicionários dentro) - nested dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
};
# ou
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Mais alguns métodos e propriedades: ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
