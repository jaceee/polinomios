import unittest

class TestsTDD1(unittest.TestCase):

    def test_polinomio(self):
        from polinomios.model.polinomio import Polinomio
        self.assertIsInstance(Polinomio(), Polinomio)
        self.assertIsInstance(Polinomio('2x3+3y'), Polinomio)

        p = Polinomio('3y')
        self.assertEqual(len(p.obtenerTerminos()), 1)
        p.agregarTermino(2, 'x', 3)
        self.assertEqual(len(p.obtenerTerminos()), 2)

        self.assertEqual(p.obtenerTermino('y', 1), 3)
        self.assertEqual(p.obtenerTermino('x', 3), 2)
        p.agregarTermino(5, 'x', 3)
        self.assertEqual(p.obtenerTermino('x', 3), 7)
        self.assertEqual(len(p.obtenerTerminos()), 3)
        p.agruparTerminos()
        self.assertEqual(p.obtenerTermino('x', 3), 7)
        self.assertEqual(len(p.obtenerTerminos()), 2)

    """def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)"""

if __name__ == '__main__':
    unittest.main()