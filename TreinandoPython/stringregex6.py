import re

texto = str(input('Digite o texto a ser revisado: '))
palavra_antiga = str(input('Qual palavra deseja substituir? '))
palavra_nova = str(input('Qual a nova palavra? '))

texto_revisado = re.sub(rf'\b{palavra_antiga}\b', palavra_nova, texto)

print(texto_revisado)
