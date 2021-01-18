'''
# Arrays são listas criadas para armazenar mais de um valor (seja ele de qualquer tipo) a uma mesma variável

# Array's are the foundation for all data science in Python. Arrays can be multidimensional, and all elements in an array need to be of the same type, all integers or all floats, for example.

When to use arrays?
Lists are much more flexible than arrays. They can store elements of different data types including strings. And, if you need to do mathematical computation on arrays and matrices, you are much better off using something like NumPy.

So, what are the uses of arrays created from the Python array module?

The array.array type is just a thin wrapper on C arrays which provides space-efficient storage of basic C-style data types. If you need to allocate an array that you know will not change, then arrays can be faster and use less memory than lists.

Unless you don't really need arrays (array module may be needed to interface with C code), the use of the array module is not recommended.

Advantages of using an Array:
	.Arrays can handle very large datasets efficiently
	.Computationally-memory efficient
	.Faster calculations and analysis than lists
	.Diverse functionality (many functions in Python packages). With several Python packages that make trend modeling, statistics, and visualization easier.
'''

# Pode ser criado um array de números:
exemplo1 = [1, 2, 3, 4];

# Um array de strings:
exemplo2 = ["Um", "Dois", "Três", "Quatro"];

# Um array misto:
exemplo3 = [1, 1.5, "Dois", ["Você pode inserir até outro array aqui", 3]]

# Concatenando arrays:
exemplo4 = exemplo1 + exemplo2;

# Como pegar o valor de um array?
# Posições iniciam em 0 (importante lembrar)
um = exemplo1[0];
dois = exemplo2[1];
tres = exemplo3[3][1];
# Você também pode acessar com referência no final, sendo o último termo -1 e os antecessores vão subtraindo 1 a cada posição
quatro = exemplo1[-1];
um_e_meio = exemplo3[-3];

# Acessando partes do array:
print(exemplo1[2:5]) # 3º ao 5º (o último não conta)
print(exemplo1[:-2]) # começo até o -2(penúltimo)
print(exemplo1[1:])  # 2º ao final
print(exemplo1[:])   # começo ao fim

#Como alterar o valor de um array?
exemplo1[0] = 0;
exemplo2[1] = "Alterado";
exemplo3[3][1] = "O tipo pode ser alterado também";

# Como descobrir o tamanho de um Array?
tamanho_exemplo1 = len(exemplo1);

# Percorrendo um array:
for numero in exemplo1:
	print(numero);

# Acrescentando informação a um array:
exemplo1.append(5);

# Deletando informações de um array:
# A função pop recebe como parâmetro o index do elemento que será excluído:
exemplo1.pop(0); 
exemplo1.pop(-1); # Os index negativos também funcionam dentro dos métodos dos arrays
# Além disso, você também pode excluir o elemento baseado em seu valor (remove só o primeiro termo com o valor encontrado):
exemplo2.remove("Quatro");


# Mais alguns métodos e propriedades: ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# typecodes -> A string with all available type codes.
# typecode -> The typecode character used to create the array.
# itemsize -> The length in bytes of one array item in the internal representation.
# buffer_info() Return a tuple (address, length) giving the current memory address and the length in elements of the buffer used to hold array’s contents
# byteswap() “Byteswap” all items of the array
# frombytes(s) Appends items from the string, interpreting the string as an array of machine values
# fromfile(f, n) Read n items (as machine values) from the file object f and append them to the end of the array
# fromlist(list) Append items from the list -> equivalent to "for x in list: a.append(x)""
# fromunicode(s) Extends this array with data from the given unicode string.
# tobytes() Convert the array to an array of machine values and return the bytes representation
# tofile(f) Write all items (as machine values) to the file object f.
# tolist() Convert the array to an ordinary list with the same items
# tounicode() Convert the array to a unicode string

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Além disso, você pode trabalhar com o módulo de arrays, ou o módulo numpy, que fornecem ainda mais possibilidades:

import numpy as np;
import array as arr;

# Criando um array usando as bibliotecas
a = arr.array('d', [1.1, 3.5, 4.5]);
a = np.array([1,2,3,4]);
# A letra representa o tipo das variáveis presentes no array

# Transformando uma lista em array com a biblioteca
numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)

# Mudando um intervalo
exemplo1[0:3] = arr.array('i', [1, 2, 3, 4]);

# Deletando um elemento por index:
del exemplo4[2];

# Deletando um elemento por valor:
exemplo4.remove(1);
 
