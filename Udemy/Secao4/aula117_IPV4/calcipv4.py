import re


class CalcIPv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._set_broadcast()
        self._set_rede()

    
    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast
    
    @property
    def numero_ips(self):
        return self._get_numero_ips()

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara
    
    @property
    def prefixo(self):
        return self._prefixo

    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):
            raise ValueError('Ip Inválido')
        self._ip = valor
        self._ip_bin = self._ip_to_bin(valor)
    
    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return
        
        if not self._valida_ip(valor):
            raise ValueError('Máscara Inválida')

        self._mascara = valor
        self._mascara_bin = self._ip_to_bin(valor)
        # se não foi configurado o prefixo, executa
        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')
        
    @prefixo.setter
    def prefixo(self, valor):
        if not valor:
            return
        
        #Valida se o valor é um inteiro
        if not isinstance(valor, int):
            raise TypeError('Prefixo precxisa ser inteiro.')

        # Valida se o IP é menor que o limite de 32 bits
        if valor > 32:
            raise TypeError('Prefixo precisa ter 32 bits.')

        self._prefixo = valor
        # ljust alinhas os caracteres a esquerda e preenche com o par o que falta
        self._mascara_bin = (valor * '1').ljust(32, '0')
        self.mascara = self._bin_to_ip(self._mascara_bin)
        
        # se não foi configurada a mascara, configura.
        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self.mascara_bin)

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )
        #print(regexp.search(ip))
        if regexp.search(ip):
            return True
    
    @staticmethod
    def _ip_to_bin(ip):
        # retira os pontos da Mascara
        blocos = ip.split('.')
        # transforma em binario, preenche com zeros para 8 casas
        bloco_binarios = [bin(int(x))[2:].zfill(8) for x in blocos]
        # retorna o valor com os numeros juntos e sem pontos.
        return ''.join(bloco_binarios)
        
    @staticmethod
    def _bin_to_ip(ip):              
        n = 8
        # Converter de binario para decimal utilizando o int() com base 2.
        # Depois converter pra str() para poder usar o join().
        blocos = [str(int(ip[i:n+i], 2)) for i in range(0, 32 ,n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
       host_bits = 32 - self.prefixo
       self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
       self._broadcast = self._bin_to_ip(self._broadcast_bin)
       return self._broadcast


    def _set_rede(self):
        host_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._rede

    def _get_numero_ips(self):
        return 2 ** (32 - self.prefixo)



