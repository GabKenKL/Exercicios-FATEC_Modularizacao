#Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.
#algoritmo investimento

#declaração de variável
tipo: int = 0
valor: float = 0

def correcao(tipo_i , valor_investido):
    if tipo_i == 1:
        valor_corrigido = valor_investido *1.03
    elif tipo_i == 2:
        valor_corrigido = valor_investido *1.05

    print("O valor corrigido é de R$" , valor_corrigido)

def main():
    global tipo
    global valor

    tipo = int(input("Digite 1 para investimento em poupança e 2 para investimento em renda fixa: "))
    valor = float(input("Digite o valor investido: "))

    correcao(tipo , valor)

if (__name__ == '__main__'):
    main()
