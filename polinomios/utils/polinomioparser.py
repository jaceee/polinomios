import re

class PolinomioParser:
    def __init__(self):
        self.regexExpresion = '^(\\-?\\d*[a-zA-Z]\\d*)([+\\-]\\d*[a-zA-Z]\\d*)*$'
        self.validator = re.compile(self.regexExpresion)

        self.regexSplit = '([+\\-]?\\d*[a-zA-Z]\\d*)'
        self.splitter = re.compile(self.regexSplit)

        self.regexTermino = '(?P<signo>[+\\-])?(?P<base>\\d+)?(?P<letra>[a-zA-Z])(?P<exponente>\\d+)?'
        self.reader = re.compile(self.regexTermino)

    def validar(self, expresion):
        return self.validator.match(expresion) is not None

    def extraer(self, expresion):
        if not self.validar(expresion):
            raise Exception('Formato invalido.\n"%s"' % lista)

        lista = self.splitter.split(expresion)
        terminos = []

        for termino in lista:
            if termino:
                match = self.reader.match(termino)
                resultado = match.groupdict()
                base = int(resultado['base'] or 1)
                letra = resultado['letra']
                exponente = int(resultado['exponente'] or 1)
                if resultado['signo'] is '-':
                    base = -base

                terminos.append((base, letra, exponente))

        return terminos