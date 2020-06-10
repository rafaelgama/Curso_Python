# Projeto Calculando Redes IPv4

from calcipv4 import CalcIPv4

# prefixo=24
# mascara='255.255.255.0'
calc_ipv4 = CalcIPv4(ip='192.168.0.1', mascara='255.255.255.192' )


print(f'IP: \t\t{calc_ipv4.ip}')
print(f'Máscara: \t{calc_ipv4.mascara}')
print(f'Rede: \t\t{calc_ipv4.rede}')
print(f'Broadcast: \t{calc_ipv4.broadcast}')
print(f'Prefixo: \t{calc_ipv4.prefixo}')
print(f'Número de IPs da Rede: {calc_ipv4.numero_ips}')


