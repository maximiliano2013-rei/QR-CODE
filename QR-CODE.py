#instalar a biblioteca "pip install qrcode pillow'

import qrcode

url = 'https://www.google.com.br/'
imagem = qrcode.make(url)
imagem.save('qrcode.png')