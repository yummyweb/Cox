from lexer import *

def main():
    source = "+   $ People are sooo mean\n  /* *   > >="
    lexer = Lexer(source)

    token = lexer.getToken()
    while token.type != TokenType.EOF:
        print(token.text)
        token = lexer.getToken()

main()
