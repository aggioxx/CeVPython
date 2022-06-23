import urllib.request

def conecta(host):
    try:
        url = host
        req = urllib.request.Request(url, headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"})
        urllib.request.urlopen(req)
        # o Request faz a identificação como browser perante o site e assim o acesso fica liberado.
    except:
        return False
    else:
        return True

# Programa principal
site = 'https://www.youtube.com'
conecta(site)
if conecta(site) == True:
    print(f'O site {site} está acessivel.')
else:
    print(f'O site {site} NÃO está acessível.')