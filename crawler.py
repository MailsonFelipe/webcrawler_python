import requests
import re
#https://www.illion.com.au/
#https://www.phosagro.com/contacts/
site = 'https://www.phosagro.com/contacts/'

resrequisicao = requests.get(site)
a = resrequisicao.text

l = []
l = (a.split('\n'))
linkExtraido = ''
listaDeLogos = []

for i in range(len(l)):
    if('logo' in l[i] and 'src="' in l[i]):
        linkExtraido += l[i]
        linkExtraido = linkExtraido.split('src="')[1].split('"')[0]

        if (not linkExtraido.startswith('http')):
            linkExtraido = linkExtraido[1:]
            cont = 0
            aux = ""
            for i in range (len(site)):
                if (cont == 3):
                    break
                else:
                    aux  +=  site[i]
                    if(site[i] == '/'):
                        cont += 1
            linkExtraido = aux + linkExtraido
        listaDeLogos.append(linkExtraido)
print(listaDeLogos)


for i in range(len(l)):
    if(l[i].lower().startswith('<') and 'href="' in l[i].lower() and 'contact' in l[i].lower() or 'phone' in l[i].lower()) and re.search('\d', l[i]):
        numero = l[i].split('<')

        print(numero)
        i = 0
        for i in range(len(numero)):
            if('phone' in numero[i].lower() or 'conctact' in numero[i].lower()):
                numero = numero[i+1].split('>')[1]
                break
                
        print(numero)
        break
