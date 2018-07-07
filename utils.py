from lark.indenter import Indenter

class PythonIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4

def openFileAsText(file):
	return "".join(open(file).readlines())


#def openFileAsText: file -> open -> readlines -> join("", _)
