from antlr4 import *

from IterableFuncLexer import IterableFuncLexer
from IterableFuncParser import IterableFuncParser

def map_function(func, iterable):
    return [func(item) for item in iterable]

class IterableFuncVisitor(ParseTreeVisitor):
    def visitStart(self, ctx: IterableFuncParser.StartContext):
        func_name = ctx.function().ID().getText()
        if func_name == "square":
            func = lambda x: x * x
        elif func_name == "double":
            func = lambda x: x * 2
        # Agrega más funciones aquí

        iterable_ctx = ctx.iterable()  # Obtener la referencia a iterable_ctx
        if iterable_ctx.list_():
            iterable = self.visitList(iterable_ctx.list_())
        else:
            iterable = self.visitTuple(iterable_ctx.tuple())

        return map_function(func, iterable)

    def visitList(self, ctx: IterableFuncParser.ListContext):
        elements = [self.visit(element) for element in ctx.elements().element()]
        return elements

    def visitTuple(self, ctx: IterableFuncParser.TupleContext):
        elements = [self.visit(element) for element in ctx.elements().element()]
        return tuple(elements)

    def visitElement(self, ctx: IterableFuncParser.ElementContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        else:
            return ctx.STRING().getText()[1:-1]  # Eliminar las comillas

def main():
    input_str = input("Ingrese la expresión: ")
    lexer = IterableFuncLexer(InputStream(input_str))
    stream = CommonTokenStream(lexer)
    parser = IterableFuncParser(stream)
    tree = parser.start()
    visitor = IterableFuncVisitor()
    result = visitor.visit(tree)
    print("Resultado:", result)

if __name__ == '__main__':
    main()
