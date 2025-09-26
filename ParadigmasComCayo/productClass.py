class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def update_price(self, percent):
    self.price = self.price + (self.price * percent)

  def sold(self, solded):
    if solded <= self.quantity:
      self.quantity = self.quantity - solded

  def reset(self, new_products):
    self.quantity = self.quantity + new_products

  def show_products(self):
    return(f"Nome: {self.name}\nPreço: {self.price}\nQuantidade: {self.quantity}")


class FoodProduct(Product):
  def __init__(self, name, price, quantity, expiration_date):  
    super().__init__(name, price, quantity)
    self.expiration_date = expiration_date

  def show_products(self):
    return(f"Nome: {self.name}\nPreço: {self.price}\nQuantidade: {self.quantity}\nData de validade: {self.expiration_date}")


class EletronicProduct(Product):
  def __init__(self, name, price, quantity, warranty):
    super().__init__(name, price, quantity)
    self.warranty = warranty

  def show_products(self):
    return(f"Nome: {self.name}\nPreço: {self.price}\nQuantidade: {self.quantity}\nGarantia: {self.warranty} meses")


def create_product(typeProduct):
  name = input("Digite o nome do produto: ")
  price = float(input("Digite o preço do produto: "))
  quantity = int(input("Digite a quantidade do produto: "))

  if typeProduct == 1:
    Produto_01 = Product(name, price, quantity)
    print(Product.show_products(Produto_01))
    actions(Produto_01)

  if typeProduct == 2:
    expiration_date = input("Digite a data de validade do produto: ")
    Produto_01 = FoodProduct(name, price, quantity, expiration_date)
    print(FoodProduct.show_products(Produto_01))
    actions(Produto_01)

  if typeProduct == 3:
    warranty = int(input("Digite a garantia do produto: "))
    Produto_01 = EletronicProduct(name, price, quantity, warranty)
    print(EletronicProduct.show_products(Produto_01))
    actions(Produto_01)

def actions(classs):
  option = input(("Houve venda de produto? (s/n):"))
  if option in ("s", "S"):
    qtd = int(input("Digite a quantidade vendida: "))
    classs.sold(qtd)
    print(classs.show_products())

  option = input(("Houve reposição de produto? (s/n):"))
  if option in ("s", "S"):
    qtd = int(input("Digite a quantidade reposta: "))
    classs.reset(qtd)
    print(classs.show_products())

def show_description():
  pass
while True:
  print("-=== Escolha o tipo do produto ===-")
  print("1 - Produto Comum")
  print("2 - Alimento")
  print("3 - Eletrônico")
  print("4 - Sair")
  print("-==============================-")
  typeProduct = int(input("Digite o tipo do produto: "))
  if typeProduct in (1, 2, 3):
    create_product(typeProduct)
  if typeProduct == 4:
    print("Finalizando...")
    break