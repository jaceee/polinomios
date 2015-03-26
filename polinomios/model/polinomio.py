from polinomios.utils.polinomioparser import PolinomioParser

class Polinomio:
    def __init__(self, string=''):
        string = string.replace(' ', '')
        self._parser = PolinomioParser()
        self._terminos = []

        if string:
            if not self._parser.validar(string):
                raise Exception('Cadena invalida para generar un polinomio.\n%s' % string)
            terminos = self._parser.extraer(string)
            for t in terminos:
                self.agregarTermino(t[0], t[1], t[2])

    def obtenerTerminos(self):
        return self._terminos

    def obtenerTermino(self, letra, exponente):
        resultado = 0
        for t in self._terminos:
            if t and (t[1] is letra and t[2] is exponente):
                resultado += t[0]
        return resultado

    def agruparTerminos(self):
        i = 0
        while i < len(self._terminos) - 1:
            p = self._terminos[i]

            j = i + 1
            while j < len(self._terminos):
                q = self._terminos[j]

                if (p is not q) and ((p[1] is q[1]) and (p[2] is q[2])):
                    # raise Exception(p, q, ((p[1] is q[1]) and (p[2] is q[2])))
                    t = (p[0]+q[0], p[1], p[2])
                    self._terminos[i] = t
                    p = self._terminos[i]
                    self._terminos.remove(q)
                    continue
                j += 1
            i += 1

    def agregarTermino(self, base, letra, exponente):
        if (base is not 0) and (exponente is not 0):
            if (len(letra) < 2):
                self._terminos.append( (base, letra, exponente) )
            else:
                raise Exception('Cada termino debe ser representado por una unica letra.')
        else:
            raise Exception('Valor invalido para la base y/o el exponente.')