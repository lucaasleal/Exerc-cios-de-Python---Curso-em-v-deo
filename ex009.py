n = int(input ('Digite um número para ver a tabuada: '))
print('TABUADA DO {}'.format(n))
cores = {'limpa':'\033[m','cor':'\033[1;36m'}
print('{} x {:2} = {}{}{}'.format(n, 1, cores['cor'], n*1, cores['limpa']))
print('{} x {:2} = {}{}{}'.format(n, 2, cores['cor'], n*2, cores['limpa']))
print('{} x {:2} = {}{}{}'.format(n, 3, cores['cor'],  n*3, cores['limpa']))
print('{} x {:2} = {}{}{}'.format(n, 4, cores['cor'],  n*4, cores['limpa']))
print('{} x {:2} = {}{}{}'.format(n, 5, cores['cor'], n*5, cores['limpa']))
print('{} x {:2} = {}{}{}'.format(n, 6, cores['cor'], n*6, cores['limpa']))
print('{} x {:2} = {}{}{}'.format(n, 7, cores['cor'], n*7, cores['limpa']))
print('{} x {:2} = {}{}{}'.format(n ,8, cores['cor'], n*8, cores['limpa']))
print('{} x {:2} = {}{}{}'.format(n, 9, cores['cor'], n*9, cores['limpa']))
print('{} x {:2} = {}{}{}'.format(n, 10, cores['cor'], n*10, cores['limpa']))
