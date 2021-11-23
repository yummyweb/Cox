import enum
import sys

class TokenType(enum.Enum):
	EOF = -1
	NEWLINE = 0
	NUMBER = 1
	IDENT = 2
	STRING = 3
	# Keywords.
	LABEL = 101
	GOTO = 102
	PRINT = 103
	INPUT = 104
	VAR = 105
	IF = 106
	THEN = 107
	ENDIF = 108
	WHILE = 109
	REPEAT = 110
	ENDWHILE = 111
	# Operators.
	EQ = 201
	PLUS = 202
	MINUS = 203
	ASTERISK = 204
	SLASH = 205
	EQEQ = 206
	NOTEQ = 207
	LT = 208
	LTEQ = 209
	GT = 210
	GTEQ = 211

class Lexer:
    def __init__(self, source):
        self.source = source + '\n'
        self.pos = -1
        self.char = ''
        self.consume()

    def consume(self):
        self.pos += 1
        if self.pos >= len(self.source):
            self.char = '\0'
        else:
            self.char = self.source[self.pos]

    def peek(self):
        if self.pos + 1 >= len(self.source):
            return '\0'

        return self.source[self.pos+1]

    def printError(self):
        sys.exit("[ERROR] Lexical analysis failed")

    def skipWhitespace(self):
        while self.char == ' ' or self.char == '\t' or self.char == '\r':
            self.consume()

    def skipComments(self):
        if self.char == '$':
            while self.char != '\n':
                self.consume()

    def getToken(self):
        self.skipWhitespace()
        self.skipComments()

        if self.char == '+':
            token = Token(self.char, TokenType.PLUS)
        elif self.char == '-':
            token = Token(self.char, TokenType.MINUS)
        elif self.char == '*':
            token = Token(self.char, TokenType.ASTERISK)
        elif self.char == '/':
            token = Token(self.char, TokenType.SLASH)
        elif self.char == '\n':
            token = Token(self.char, TokenType.NEWLINE)
        elif self.char == '\0':
            token = Token(self.char, TokenType.EOF)
        elif self.char == '=':
            if self.peek() == '=':
                lastChar = self.char
                self.consume()
                token = Token(lastChar + self.char, TokenType.EQEQ)
            else:
                token = Token(self.char, TokenType.EQ)
        elif self.char == '>':
            if self.peek() == '=':
                lastChar = self.char
                self.consume()
                token = Token(lastChar + self.char, TokenType.GTEQ)
            else:
                token = Token(self.char, TokenType.GT)
        elif self.char == '<':
            if self.peek() == '=':
                lastChar = self.char
                self.consume()
                token = Token(lastChar + self.char, TokenType.LTEQ)
            else:
                token = Token(self.char, TokenType.LT)
        elif self.char == '"':
            self.consume()
            startPos = self.pos

            while self.char != '"':
                if self.char == '\r' or self.char == '\t' or self.char == '\\' or self.char == '%':
                    self.printError()
                self.consume()

            tokText = self.source[startPos:self.pos]
            token = Token(tokText, TokenType.STRING)
        else:
            # Unknown token
            self.printError()

        self.consume()
        return token


class Token:
    def __init__(self, tokenText, tokenType):
        self.text = tokenText
        pass
        self.type = tokenType
