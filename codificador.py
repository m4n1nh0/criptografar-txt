

import math
import random
import os
import caracteres as car

CURR_DIR = os.path.dirname(os.path.realpath(__name__))

class Codificar:

    cifra = 1
    buffer = 100
    buffer_min = 0.5
    limite_bytes = 999000
    pref1 = 'coded='

    def __init__(self, msg_entrada=None):
        self.__msg_entrada = msg_entrada
        self.__len_original = None
        self.__msg_codificada = None
        self.__msg_decodificada = None

    def __repr__(self):
        ret = ''

        len_entrada = 0
        len_decodificado = 0
        len_codificado = 0

        if self.entrada != None:
            len_entrada = len(self.entrada)

        ret = (
            f'\n\n...> Entrada.......: [{self.entrada}]'
            f' - len:{len_entrada}'

            f'\n\n...> Decodificado..: [{self.decodificado}]'
            f' - len:{len_decodificado}'

            f'\n\n...> Codificado....: [{self.codificado}]'
            f' - len:{len_codificado}'

            f'\n\n...> Validade......: [{self.valido}]\n'                        
        )

        return ret
    
    @property
    def entrada(self):
        return self.__msg_entrada
    @property
    def codificado(self):
        return self.__msg_codificada
    @property
    def decodificado(self):
        return self.__msg_decodificada
    @property
    def valido(self):
        ret = False
        if self.__msg_entrada == self.__msg_decodificada:
            ret = True
        return ret

    @entrada.setter
    def entrada(self, valor):
        self.__msg_entrada = valor

    @codificado.setter
    def codificado(self, valor):
        self.__msg_codificada = valor

    @decodificado.setter
    def decodificado(self, valor):
        self.__msg_decodificada = valor


    # ------------------------------------------------------------------
    def _cifrar(self, byte):
        ret = ''

        caracteres = car.char
        if byte in caracteres:
            cif = self.cifra
            ret = chr(ord(byte) + cif)
        else:
            raise ValueError(f'Símbolo [{byte}] não previsto')            

        return ret

    # ------
    def _decifrar(self, byte):
        cif = self.cifra
        ret = chr(ord(byte) - cif)

        return ret

    # ------
    def _calc_buffer(self, texto):
        ret = ''

        len_txt = len(texto)
        y = len_txt / self.buffer

        if y < self.buffer_min:
            res = self.buffer
        else:
            y = math.ceil(y) # arredonda sempra para cima
            res = (y * self.buffer)
        
        ret = res + self.buffer

        return ret

    # ------
    def _add_buffer(self, texto, buffer):
        ret = ''

        caracteres = car.char
        len_texto = len(texto)
        for i in range(buffer):
            if i >= len_texto:
                idx_caracteres = len(caracteres) - 1
                sorteio = random.randint(0, idx_caracteres)
                ret += caracteres[sorteio]
            else:
                ret += texto[i]

        return ret

    # ------
    def _len_msg_str(self, msg):
        ret = ''

        x = len(str(self.limite_bytes))
        ret = len(msg)
        ret = str(ret).zfill(x)

        return ret

    # ------
    def _len_msg(self, msg):
        ret = ''

        ini = len(self.pref1)
        fim = ini + len(str(self.limite_bytes))
        text = str(msg[ini : fim]) 
        text_decifrado = ''

        for t in text:
            text_decifrado += self._decifrar(t)        
        
        ret = int(text_decifrado)
        return ret

    # ------------------------------------------------------------------
    def validar_texto(self, texto):
        ret = True

        if (texto == None) or (texto == 0):
            ret = 'Texto para codificação não pode ser vazio'

        if texto[0:6] == self.pref1:
            ret = 'Texto já codificado, use a função decriptografar'
        
        if len(texto) > self.limite_bytes:
            ret = f'Limite de {self.limite_bytes} bytes'

        return ret


    def criptografar(self, texto):
        ret = ''
        self.entrada = texto

        if self.validar_texto(texto) != True:
            raise ValueError(self.validar_texto(texto))

        buffer = self._calc_buffer(texto)
        pref2 = self._len_msg_str(texto)

        texto = f'{pref2}{texto}'        
        texto = self._add_buffer(texto, buffer - len(str(self.limite_bytes)) )

        for t in texto:
            ret += self._cifrar(t)
        
        ret = f'{self.pref1}{ret}'

        self.codificado = ret
        self.decodificado = self.decriptografar(self.codificado)
        if not self.valido:
            raise ValueError('Não foi possível garantir a integridade da mensagem')
        return ret

    
    def decriptografar(self, texto):
        ret = ''
        len_da_msg = self._len_msg(texto)

        ind = 0        
        x = ( len(str(self.limite_bytes)) + len(str(self.pref1)))
        for t in texto:
            ind += 1
            if (ind > x) and (ind <= (len_da_msg) + x):
                ret += self._decifrar(t)
            
        return ret
