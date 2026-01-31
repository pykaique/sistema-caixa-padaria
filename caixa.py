# Lista de preços (Isso é um Dicionário - Chave e Valor)
precos = {
    "pao": 0.50,
    "Leite": 5.50,
    "Cafe": 4.00,
    "Bolo": 15.00
}

total_compra = 0

print("--- BEM-VINDO Á PADARIA FUNDO DE BAIRRO ---")

# Um loop 'while True' faz o programa rodar até a gente mandar parar
while True:
    produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")

    if produto.lower() == 'sair':
        break # Para o programa 
    if produto in precos:
        quantidade = int(input(f"Quantos(as) {produto} o cliente comprou? "))
        valor_item = precos[produto] * quantidade
        total_compra += valor_item
        valor_pago = float(input("Quanto o cliente entregou em dinheiro? R$ "))

        if valor_pago >= total_compra:
            troco = valor_pago - total_compra
            print(f"Troco: R$ {troco:.2f}")
        else:
            falta = total_compra - valor_pago
            print(f"Dinheiro insuficiente! Ainda faltam R$ {falta:.2f}")
        print(f"Adicionado: {quantidade} x {produto} = R$ {valor_item:.2f}")
    else:
        print("Produto não encontrado no sistema!")

print("-" * 30)
print(f"TOATAL DA COMPRA: R$ {total_compra:.2f}")
print("--- OBRIGADOO E VOLTE SEMPRE ---")

