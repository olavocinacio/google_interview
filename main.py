# https://wiki.python.org.br/ProgramacaoOrientadaObjetoPython
# http://devfuria.com.br/python/programacao-orientada-objetos/
# https://realpython.com/python3-object-oriented-programming/
# https://www.programiz.com/python-programming/object-oriented-programming
# https://www.tutorialspoint.com/python/python_classes_objects.htm
# https://towardsdatascience.com/understand-o-o-p-in-python-with-one-article-bfa76f3ba48c
# https://www.datacamp.com/community/tutorials/python-oop-tutorial
# https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/classesintro.html

'''
Uma classe define uma estrutura de dados que contenha instância de atributos, instância de métodos e classes aninhadas. Em Python a classe de um objeto e o tipo de um objeto são sinônimos. 
A classe (tipo) de um objeto determina o que é e como pode ser manipulado. Uma classe encapsula dados, operações e semântica.

Objetos são instanciados pelas classes. Cada instância (objeto) em uma programa Python tem seu próprio namespace.

Um classe criada é chamada de classe objeto (tipo classobj). Os nomes no namespace da classe objeto são chamados de atributos da classe. Funções definidas dentro de uma classe são chamadas de métodos.

Quando um objeto é criado, o namespace herda todos os nomes do namespace da classe onde o objeto está. O nome em um namespace de instância é chamado de atributo de instância.

Um método é uma função criada na definição de uma classe. O primeiro argumento do método é sempre referenciado no início do processo. Por convenção, o primeiro argumento do método tem sempre o nome self. Portanto, os atributos de self são atributos de instância da classe.
'''

# Definindo uma classe:
class Complex(object): # Definindo a classe Complex
	def __init__(self, real, imag): # Depois do self, declara-se os parâmetros pedidos para definir um objeto dessa classe
		self._real = real; # Atribuindo os parâmetros a uma variável inerente ao objeto
		self._imag = imag;

# Utilizando a classe definida anteriormente e acessando suas variáveis:
teste = Complex(1,3);
parte_real = teste._real;
parte_imag = teste._imag;
# Segunda forma - Usando método _init_:
c = object.__new__(Complex);
Complex.__init__(c,0,1);

del Complex;

# Adicionando métodos à classe criada:
class Complex(object):
	def getReal(self):
		return self._real;
	
	def setReal(self, valor):
		self._real = valor;
	
	real = property(
		fget = getReal,
		fset = setReal)

	def getImag(self):
		return self._imag;
	
	def setImag(self, valor):
		self._imag = valor;

	imag = property(
		fget = getImag,
		fset = setImag)

'''
Os métodos getReal e setImag promovem o acesso dos atributos _real e _imag, respectivamente. Um método que acessa uma instância mas não modifica a instância é chamado de accessor ou acessor. Portanto, getReal e getImag são accessors.

Os métodos setReal e setImag promovem a modificação dos atributos _real e _imag, respectivamente. Um método que modifica uma instância é um mutator ou modificador. Portanto, setReal e setImag são modificadores.

O operador . (ponto) é utilizado para especificar o objeto em que o método também é invocado. Por exemplo:
'''

# Declarando um complexo de acordo com a nova classe descrita:
c.setReal(3);
print (c.getReal());
