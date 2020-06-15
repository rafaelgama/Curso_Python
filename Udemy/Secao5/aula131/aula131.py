# String - Template
# Criação de um Template em HTML

from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage 
import smtplib

email = 'oficina1.rg@gmail.com'
senha = ''

path = r'D:\GitHub\Curso_Python\Udemy\Secao5\aula131'

with open(path+'\Template.html', 'r') as html:
    template = Template(html.read()) # Template dessa linha faz parte do modulo string
    data_atual = datetime.now().strftime('%d/%m/%Y')
    # o metodo substitute, levanta excessão se houver algum erro.
    corpo_msg = template.substitute(nome='Rafael Gama',data=data_atual)
    
msg = MIMEMultipart()
msg['from'] = 'Rafael Gama'
msg['to'] = email
msg['subject'] = 'Atenção: este é um e-mail de testes.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open(path+'\imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

# configurar a conexão do e-mail
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email,senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)




