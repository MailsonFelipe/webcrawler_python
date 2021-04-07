import requests

site = 'https://www.phosagro.com/contacts/'

resrequisicao = requests.get(site)
a = resrequisicao.text

l = []
l = (a.split('\n'))
link = ''

for i in range(len(l)):
    if('logo' in l[i] and 'src="' in l[i]):
        link += l[i]
        break

link = link.split('src="')[1].split('"')[0][1:]

if (not link.startswith('http')):
    cont = 0
    completeLink = ""
    for i in range (len(site)):
        if (cont == 3):
            break
        else:
            completeLink  +=  site[i]
            if(site[i] == '/'):
                cont += 1
completeLink += link
print(completeLink)