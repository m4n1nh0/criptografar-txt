

import unittest


from codificador import Codificar


class CodificadorTestes(unittest.TestCase):
    
    obj = Codificar()

    def test_len_msg_str(self):
        self.assertEqual(
            self.obj._len_msg_str('Mensagem'),
            '000008'
        )


    def test_len_msg(self):
        self.assertEqual(
            self.obj._len_msg('coded=222333kkklll'),
            111222
        )

    def test_integridade(self):
        text = 'Um mensagem qualquer! '
        obj = Codificar(text)
        self.assertEqual(
            self.obj.entrada,
            text
        )


if __name__ == '__main__':
    print(f'\n' * 10)
    unittest.main()