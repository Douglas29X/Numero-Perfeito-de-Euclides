
def verifica_primo(n):
	mult=0

	for count in range(2,n):
	    if (n % count == 0):
	        mult += 1

	#números primos == 1, não primos == 2
	if(mult==0):
	    return 1, n
	else:
	    return 2, 0

ultimo_numero_sequencia = 1
dupla_proporcao = []

while ultimo_numero_sequencia < 10**5:
	dupla_proporcao.append(ultimo_numero_sequencia)
	soma = 0
	for numero in dupla_proporcao:
		soma+= numero

	eh_primo, n = verifica_primo(soma)
	n_perf = ultimo_numero_sequencia * n

	if n != 0:
		with open("resultados.txt","w") as arquivo:
			frase = f"O último número primo encontrado foi {n}\nO número perfeito é: {n_perf}"
			arquivo.write(frase)
			print(frase)

	ultimo_numero_sequencia *= 2

