from antlr4 import *
from LabeledExprLexer import LabeledExprLexer
from LabeledExprParser import LabeledExprParser
from LabeledExprVisitor import LabeledExprVisitor

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        else:
            return ComplexNumber(self.real + other, self.imag)

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        else:
            return ComplexNumber(self.real - other, self.imag)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real * other.real - self.imag * other.imag,
                                 self.real * other.imag + self.imag * other.real)
        else:
            return ComplexNumber(self.real * other, self.imag * other)

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denom = other.real**2 + other.imag**2
            real = (self.real * other.real + self.imag * other.imag) / denom
            imag = (self.imag * other.real - self.real * other.imag) / denom
            return ComplexNumber(real, imag)
        else:
            return ComplexNumber(self.real / other, self.imag / other)

    def __str__(self):
        return f"{self.real} {'+' if self.imag >= 0 else '-'} {abs(self.imag)}i" if self.imag != 0 else str(self.real)

class EvalVisitor(LabeledExprVisitor):
    def __init__(self):
        self.memory = {}

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return value

    def visitAssign(self, ctx):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id] = value
        return value

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitId(self, ctx):
        id = ctx.ID().getText()
        if id in self.memory:
            return self.memory[id]
        return 0

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LabeledExprParser.MUL:
            return left * right
        else:
            return left / right  # Handle division by zero appropriately
    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        
        # Verificar si los operandos son números complejos
        if isinstance(left, ComplexNumber) or isinstance(right, ComplexNumber):
            # Convertir los operandos a números complejos si es necesario
            if not isinstance(left, ComplexNumber):
                left = ComplexNumber(left, 0)
            if not isinstance(right, ComplexNumber):
                right = ComplexNumber(right, 0)
            
            if op == '+':
                return left + right
            else:
                return left - right
        else:
            # Si los operandos no son números complejos, realizar la operación aritmética
            if op == '+':
                return left + right
            else:
                return left - right



    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitImagLit(self, ctx):
        return ComplexNumber(0, 1)

    def visitImagLitWithInt(self, ctx):
        return ComplexNumber(0, int(ctx.INT().getText()))

    def visitComplexLit(self, ctx):
        real = int(ctx.INT(0).getText())
        imag_sign = 1 if ctx.getChild(1).getText() == '+' else -1
        imag = int(ctx.INT(1).getText()) * imag_sign
        return ComplexNumber(real, imag)

def main():
    while True:
        try:
            text = input('calc> ') + '\n'
            lexer = LabeledExprLexer(InputStream(text))
            stream = CommonTokenStream(lexer)
            parser = LabeledExprParser(stream)
            tree = parser.prog()

            visitor = EvalVisitor()
            visitor.visit(tree)
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()
