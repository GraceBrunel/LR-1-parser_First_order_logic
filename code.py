import lrparsing
from lrparsing import Keyword, List, Prio, Ref, THIS, Token, Tokens
class ExprParser(lrparsing.Grammar):
	class T(lrparsing.TokenRegistry):
		# Build the tokens to be detected.
		connective=Token(re="OR|AND|IMP|DIMP")
		quantifier=Token(re="A|E")
		identifier=Token(re="[a-z]")
		such_that=Token(re=":")
		open_br = Token(re="OB") # we cannot represent ( in re
		close_br = Token(re = "CB") # we cannot represent ) in re
	# Implement the grammar for the LR parser.
	E = Ref("E")
	Q = Ref("Q")
	Q1 = Ref("Q1")
	L = Ref("L")
	L1 =Ref("L1")
	Q1 = Q * 1
	L1 = L * 1
	I = T.identifier
	Q = T.quantifier + I + Q1 | T.quantifier + I
	S = T.such_that
	L = I + T.connective + L1 | T.open_br + L + T.close_br + T.connective + L1 |T.open_br + L + T.close_br |I
	E = Q + S + L
	START = E

# Parse the input.
parser = ExprParser()
parse_tree = parser.parse("AaEbAc: a AND f OR a IMP b  AND c OR  d IMP g DIMP f")
s = parser.repr_parse_tree(parse_tree)
# Generate the parse tree.
from nltk.tree import Tree
t = Tree.fromstring(s)
t.draw()
