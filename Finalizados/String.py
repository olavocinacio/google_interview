'''
Strings in python are surrounded by either single quotation marks, or double quotation marks.

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters. (Os métodos usados em arrays todos funcionam em strings)

However, Python does not have a character data type, a single character is simply a string with a length of 1.
'''

# Declarando uma string:
palavra = "String";
# Você pode colocar mais de uma palavra, contanto que tenha 3 aspas (simples ou duplas)
texto = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# Acessando uma posição de uma string:
letra = palavra[0];

# Percorrendo uma string:
for letra in "string":
	print(letra);

# Tamanho de uma string:
tamanho = len(palavra);

# Checar se uma palavra faz parte de uma string:
booleana1 = "verdade" in "verdade ou mentira"; # Retorna True
booleana2 = "queijo" in "verdade ou mentira"; # Retorna False

# Checar se uma palavra NÃO faz parte de uma string:
booleana3 = "verdade" not in "verdade ou mentira"; # Retorna False
booleana4 = "queijo" not in "verdade ou mentira"; # Retorna True

# Como deixar uma string inteira maiúscula:
maiuscula = palavra.upper();

# Como deixar uma string inteira minúscula:
minuscula = palavra.lower();

# Como remover espaçõs em branco do começo e do fim:
com_espaço = " Teste um dois ";
sem_espaço = com_espaço.strip();

# Como substituir trechos de uma string:
modificada = sem_espaço.replace("um dois", "dois três") ;

# Separando uma string em um array de strings:
com_separadores = "Um, Dois, Três, Quatro";
lista_numeros = com_separadores.split(",");

# Concatenando strings:
palavra1 = "Hello";
palavra2 = "World";
hello_world = palavra1 + ", " + palavra2 + "!";

# Concatenando uma string com uma variável de outro tipo:
idade = 19;
txt = "Meu nome é Olavo, e eu tenho {} anos";
concatenado = txt.format(idade);

# Caracateres especiais:
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value


# Mais alguns métodos e propriedades: -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# string.ascii_letters -> The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.
# string.ascii_lowercase -> The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.
# string.ascii_uppercase -> The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.
# string.digits -> The string '0123456789'.
# string.hexdigits -> The string '0123456789abcdefABCDEF'.
# string.octdigits -> The string '01234567'.
# string.punctuation -> String of ASCII characters which are considered punctuation characters in the C locale: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
# string.printable -> String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace.
# string.whitespace -> A string containing all ASCII characters that are considered whitespace. This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# check_unused_args(used_args, args, kwargs) Implement checking for unused arguments if desired
# convert_field(value, conversion) Converts the value (returned by get_field()) given a conversion type (as in the tuple returned by the parse() method)
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format_map()	Formats specified values in a string
# format_field(value, format_spec) format_field() simply calls the global format() built-in
# get_field(field_name, args, kwargs) Given field_name as returned by parse() (see above), convert it to an object to be formatted
# get_value(key, args, kwargs) Retrieve a given field value
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# parse(format_string) Loop over the format_string and return an iterable of tuple
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# vformat(format_string, args, kwargs) This function does the actual work of formatting.
# zfill()	Fills the string with a specified number of 0 values at the beginning

'''
EXTRA -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

# Como deletar uma variável:
teste = 3;
print(teste); # Printa o número normalmente
del teste;
print(teste); # Retorna um erro, pois a variável deixou de existir