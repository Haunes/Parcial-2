from antlr4 import *
from filterFuncLexer import filterFuncLexer
from filterFuncParser import filterFuncParser

def filter_function(func, iterable):
    return [item for item in iterable if func(item)]

class FilterFuncVisitor(ParseTreeVisitor):
    def visitStart(self, ctx: filterFuncParser.StartContext):
        func_name = ctx.function().ID().getText()
        if func_name == "multiple":
            func = lambda x: x % 2 == 0
        # Agrega más funciones aquí

        iterable_ctx = ctx.iterable()
        if iterable_ctx.list_():
            iterable = self.visitList(iterable_ctx.list_())
        else:
            iterable = self.visitTuple(iterable_ctx.tuple())

        return filter_function(func, iterable)

    def visitList(self, ctx: filterFuncParser.ListContext):
        elements = [self.visit(element) for element in ctx.elements().element()]
        return elements

    def visitTuple(self, ctx: filterFuncParser.TupleContext):
        elements = [self.visit(element) for element in ctx.elements().element()]
        return tuple(elements)

    def visitElement(self, ctx: filterFuncParser.ElementContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        else:
            return ctx.STRING().getText()[1:-1]  # Eliminar las comillas

def main():
    input_str = input("Ingrese la expresión: ")
    lexer = filterFuncLexer(InputStream(input_str))
    stream = CommonTokenStream(lexer)
    parser = filterFuncParser(stream)
    tree = parser.start()
    visitor = FilterFuncVisitor()
    result = visitor.visit(tree)
    print("Resultado:", result)

if __name__ == '__main__':
    main()

