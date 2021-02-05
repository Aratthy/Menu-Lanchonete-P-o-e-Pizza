OpçoesMenu = "Ver o Cardápio de Sanchíches", "Ver o Cardápio de Pizzas", "Sair do Menu" #Lista das opções do menu

CardápioSanduíche = "X-Burguer (R$9,00)", "X-Salada (R$10,00)", "X-Frango (R$12,00)", "X-Bacon (R$13,50)" #Lista do cardápio dos sanduíches
#Tabela de Preços
Preço_XBurguer = 9.00
Preço_XSalada = 10.00
Preço_XFrango = 12.00
Preço_XBacon = 13.50

CardápioPizzas = "Pizza de Calabresa (R$25,00)", "Pizza de Frango com Catupiry (R$28,00)", "Pizza de Carne (R$32,00)", "Pizza de 4 Queijos (R$33,00)" #Lista do cardápio das pizzas
#Tabela de Preços
Preço_PizzaCalabresa = 25.00
Preço_PizzaFrangoCatupiry = 28.00
Preço_PizzaCarne = 32.00
Preço_Pizza4Queijos = 33.00

CardápioBebidas = "Coca-Cola Lata (R$3,00)", "Coca Zero Lata (R$3,50)", "Fanta Lata (R$3,25)", "Pepsi Lata (R$3,50)", "Não quero uma bebida" #Lista do cardápio das bebidas
#Tabela de Preços
Preço_CocaCocaLata = 3.00
Preço_CocaZeroLata = 3.50
Preço_FantaLata = 3.25
Preço_PepsiLata = 3.50

def ordenar(lista): #Função que ordena os itens em uma lista
  print(linha())
  c = 1
  for item in lista:
    print(f'{c} - {item}')
    c += 1
  print (linha())

def linha(tam = 50): #Função que faz as linhas
    return "-" * tam

def cabeçalho(txt): #Função que cria um cabeçalho
    print(linha())
    print(txt.center(50))
    print(linha())

def bebida():
  ordenar(CardápioBebidas)
  PedidoBebida = int(input("Selecione o Número Da Sua Bebida: "))
  if PedidoBebida == 1: #Coca Cola Lata
    QuantasUnidadesBebidas = int(input("Quantas Unidades Dessa Bebida Você Vai Querer? "))
    PreçoFinal2 = PreçoFinal + (Preço_CocaCocaLata * QuantasUnidadesBebidas)
    print(linha())
    print("A Sua Conta Ficou R$"f'{PreçoFinal2: .02f}', ". Obrigado Por Comer Na\nPão e Pizza, Volte Sempre.")
    print(linha())
    print("Pressione Enter Para Fechar o Programa.")
    input()
  if PedidoBebida == 2: #Coca Zero Lata
    QuantasUnidadesBebidas = int(input("Quantas Unidades Dessa Bebida Você Vai Querer? "))
    PreçoFinal2 = PreçoFinal + (Preço_CocaZeroLata * QuantasUnidadesBebidas)
    print(linha())
    print("A Sua Conta Ficou R$"f'{PreçoFinal2: .02f}', ". Obrigado Por Comer Na\nPão e Pizza, Volte Sempre.")
    print(linha())
    print("Pressione Enter Para Fechar o Programa.")
    input()
  if PedidoBebida == 3: #Fanta Lata
    QuantasUnidadesBebidas = int(input("Quantas Unidades Dessa Bebida Você Vai Querer? "))
    PreçoFinal2 = PreçoFinal + (Preço_FantaLata * QuantasUnidadesBebidas)
    print(linha())
    print("A Sua Conta Ficou R$"f'{PreçoFinal2: .02f}', ". Obrigado Por Comer Na\nPão e Pizza, Volte Sempre.")
    print(linha())
    print("Pressione Enter Para Fechar o Programa.")
    input()
  if PedidoBebida == 4: #Pepsi Lata
    QuantasUnidadesBebidas = int(input("Quantas Unidades Dessa Bebida Você Vai Querer? "))
    PreçoFinal2 = PreçoFinal + (Preço_PepsiLata * QuantasUnidadesBebidas)
    print(linha())
    print("A Sua Conta Ficou R$"f'{PreçoFinal2: .02f}', ". Obrigado Por Comer Na\nPão e Pizza, Volte Sempre.")
    print(linha())
    print("Pressione Enter Para Fechar o Programa.")
    input()
  if PedidoBebida == 5: #Não Quero Bebidas
    PreçoDaBebida = 0.00
    PreçoFinal2 = PreçoFinal
    print(linha())
    print("A Sua Conta Ficou R$"f'{PreçoFinal2: .02f}', ". Obrigado Por Comer Na\nPão e Pizza, Volte Sempre.")
    print(linha())
    print("Pressione Enter Para Fechar o Programa.")
    input()

cabeçalho("Menu Lanchonete Pão e Pizza") #Menu que o cliente vê
c = 1
for item in OpçoesMenu:
  print(f'{c} - {item}')
  c += 1
print(linha())

SuaOpçao = int(input("Insira o Número Da Opção Desejada: ")) #Variável que o programa lê para dar continuidade ao pedido

if SuaOpçao == 1: #Sanduíches
  ordenar(CardápioSanduíche)
  SeuPedido = int(input("Insira o Número Correspondente Ao Sanduíche Que\nVocê Irá Querer? "))
  QuantasUnidades = int(input("Quantas Unidades Dele Você Deseja? "))
  if SeuPedido == 1: #X-Burguer
    PreçoFinal = Preço_XBurguer * QuantasUnidades
    bebida()
  if SeuPedido == 2: #X-Salada
    PreçoFinal = Preço_XSalada * QuantasUnidades
    bebida()
  if SeuPedido == 3: #X-Frango
    PreçoFinal = Preço_XFrango * QuantasUnidades
    bebida()
  if SeuPedido == 4: #X-Bacon
    PreçoFinal = Preço_XBacon * QuantasUnidades
    bebida()

if SuaOpçao == 2: #Pizzas
  ordenar(CardápioPizzas)
  SeuPedido = int(input("Insira o Número Correspondente à Pizza Que Você\nIrá Querer? "))
  QuantasUnidades = int(input("Quantas Unidades Dela Você Deseja? "))
  if SeuPedido == 1: #Pizza de Calabresa
    PreçoFinal = Preço_PizzaCalabresa * QuantasUnidades
    bebida()
  if SeuPedido == 2: #Pizza de Frango com Catupiry
    PreçoFinal = Preço_PizzaFrangoCatupiry * QuantasUnidades
    bebida()
  if SeuPedido == 3: #Pizza de Carne
    PreçoFinal = Preço_PizzaCarne * QuantasUnidades
    bebida()
  if SeuPedido == 4: #Pizza de 4 Queijos
    PreçoFinal = Preço_Pizza4Queijos * QuantasUnidades
    bebida()

if SuaOpçao == 3:
  print("Saindo do Menu... Até Logo!")
