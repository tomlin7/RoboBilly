'''MIT License

Copyright (c) 2020 The Basement Team 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

visit: https://billy-s-Basement.github.io
'''

from sly import Lexer
from sly import Parser

from datetime import datetime
from datetime import date


class BasicLexer(Lexer): 
	tokens = { NAME, NUMBER, STRING } 
	ignore = '\t '
	literals = { '=', '+', '-', '/', 
				'*', '(', ')', ',', ';'} 


	# Define tokens as regular expressions 
	# (stored as raw strings) 
	NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
	STRING = r'\".*?\"'

	# Number token 
	@_(r'\d+') 
	def NUMBER(self, t): 
		
		# convert it into a python integer 
		t.value = int(t.value) 
		return t 

	# Comment token 
	@_(r'//.*') 
	def COMMENT(self, t): 
		pass

	# Newline token(used only for showing 
	# errors in new line) 
	@_(r'\n+') 
	def newline(self, t): 
		self.lineno = t.value.count('\n')

class BasicParser(Parser): 
	#tokens are passed from lexer to parser 
	tokens = BasicLexer.tokens 

	precedence = ( 
		('left', '+', '-'), 
		('left', '*', '/'), 
		('right', 'UMINUS'), 
	) 

	def __init__(self): 
		self.env = { } 

	@_('') 
	def statement(self, p): 
		pass

	@_('var_assign') 
	def statement(self, p): 
		return p.var_assign 

	@_('NAME "=" expr') 
	def var_assign(self, p): 
		return ('var_assign', p.NAME, p.expr) 

	@_('NAME "=" STRING') 
	def var_assign(self, p): 
		return ('var_assign', p.NAME, p.STRING) 

	@_('expr') 
	def statement(self, p): 
		return (p.expr) 

	@_('expr "+" expr') 
	def expr(self, p): 
		return ('add', p.expr0, p.expr1) 

	@_('expr "-" expr') 
	def expr(self, p): 
		return ('sub', p.expr0, p.expr1) 

	@_('expr "*" expr') 
	def expr(self, p): 
		return ('mul', p.expr0, p.expr1) 

	@_('expr "/" expr') 
	def expr(self, p): 
		return ('div', p.expr0, p.expr1) 

	@_('"-" expr %prec UMINUS') 
	def expr(self, p): 
		return p.expr 

	@_('NAME') 
	def expr(self, p): 
		return ('var', p.NAME) 

	@_('NUMBER') 
	def expr(self, p): 
		return ('num', p.NUMBER)

class BasicExecute: 
	thing = 'none'
	def __init__(self, tree, env): 
		self.Error = 0
		self.thing = 0
		self.env = env 
		result = self.walkTree(tree) 
		if result is not None and isinstance(result, int): 
			self.thing = result
		if isinstance(result, str) and result[0] == '"': 
			self.thing = result

	def walkTree(self, node): 

		if isinstance(node, int): 
			return node 
		if isinstance(node, str): 
			return node 

		if node is None: 
			return None

		if node[0] == 'program': 
			if node[1] == None: 
				self.walkTree(node[2]) 
			else: 
				self.walkTree(node[1]) 
				self.walkTree(node[2]) 

		if node[0] == 'num': 
			return node[1] 

		if node[0] == 'str': 
			return node[1] 

		if node[0] == 'add': 
			return self.walkTree(node[1]) + self.walkTree(node[2]) 
		elif node[0] == 'sub': 
			return self.walkTree(node[1]) - self.walkTree(node[2]) 
		elif node[0] == 'mul': 
			return self.walkTree(node[1]) * self.walkTree(node[2]) 
		elif node[0] == 'div': 
			return self.walkTree(node[1]) / self.walkTree(node[2]) 

		if node[0] == 'var_assign': 
			self.env[node[1]] = self.walkTree(node[2]) 
			return node[1] 

		if node[0] == 'var': 
			try: 
				return self.env[node[1]] 
			except LookupError: 
				self.Error = ("Undefined variable '"+node[1]+"' found!") 
				return 0

lexer = BasicLexer() 
parser = BasicParser() 
env = {} 

def jbin(text):
	tree = parser.parse(lexer.tokenize(text)) 
	execution = BasicExecute(tree, env)
	if execution.Error == 0:
		return execution.thing
	else:
		return execution.Error