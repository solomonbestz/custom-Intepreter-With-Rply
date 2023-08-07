# from lexer import lexer

# stream = lexer.lex("my_var = 23")
# print(stream)

# print(stream.next())

# print(stream.next())

# print(stream.next())


from rply import ParserGenerator
from my_ast import *

pg = ParserGenerator(["NUMBER", "SEMICOLON"], cache_id="my_ast")
parser = pg.build()


@pg.production("main : statements")
def main(s):
    return s[0]