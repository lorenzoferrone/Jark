from lark import Lark
from utils import PythonIndenter, openFileAsText


if __name__ == '__main__':

	grammar = openFileAsText('grammar.lark')
	parser = Lark(grammar, postlex=PythonIndenter(), parser='lalr')

	code = openFileAsText('code')
	print (parser.parse(code).pretty())

