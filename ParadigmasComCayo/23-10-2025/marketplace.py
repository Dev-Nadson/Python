#Atrubutos do usuário
class user(): #abstrair 
    def __init__(self, name):
        self.name = name

class student(user):
    def __init__(self, name, classes):
        super().__init__(name)
        self.classes = classes

class teacher(user):
    def __init__(self, name, classes):
        super().__init__(name)
        self.classes = classes

class organizer(user):
    def __init__(self, name, couses):
        super().__init__(name)
        self.couses = couses

#Atributos do pagamento
class payment(): #abstrair 
    def __init__(self, amount):
        self.amount = amount

class pix(payment):
    def __init__(self, amount, pix_key):
        super().__init__(amount, "pix")
        self.pix_key = pix_key

class credit_card(payment):
    def __init__(self, amount, card_number, card_holder):
        super().__init__(amount, "credit_card")
        self.card_number = card_number
        self.card_holder = card_holder

class bank_slip(payment):
    def __init__(self, amount, due_date):
        super().__init__(amount, "bank_slip")
        self.due_date = due_date

#Atributos do curso
class course():
    def __init__(self, workload, price, classes):
        self.price = price
        self.workload = workload
        self.classes = classes

class registration():
    def __init__(self, user, course):
        self.user = user    
        self.course = course



def create_course():
    workload = input("Digite a carga horária do curso: ")
    price = float(input("Digite o preço do curso: "))
    classes = input("Digite as aulas do curso: ")

    new_course = course(workload, price, classes)

    return new_course

def register_user(user_type, name, classes):        
    user_type = input("Digite o tipo de usuário (Estudante, Professor, Coordenador): ")
    name = input("Digite o nome do usuário: ")
    classes = input("Digite as aulas ou cursos do usuário: ")

    if user_type in ("Estudante", "estudante"):
        user = student(name, classes)

    if user_type in ("Professor", "professor"):
        user = teacher(name, classes)

    if user_type in ("Coordenador", "Coordenador"):
        user = organizer(name, classes)  

    return user

def create_registration():
    user_name = input("Digite o nome do aluno: ")
    course_name = input("Digite o nome do curso: ")

    new_registration = registration(user_name, course_name)

    return new_registration

def process_payment():
    payment_type = input("Digite o tipo de pagamento (Pix, Cartão de Crédito, Boleto): ")
    amount = float(input("Digite o valor do pagamento: "))

    if payment_type == "Pix":
        pix_key = input("Digite a chave Pix: ")
        return pix(amount, pix_key)
    
    if payment_type == "Cartão de Crédito":
        card_number = input("Digite o número do cartão: ")
        card_holder = input("Digite o nome do titular do cartão: ")
        return credit_card(amount, card_number, card_holder)
    
    if payment_type == "Boleto":
        due_date = input("Digite a data de vencimento do boleto: ")
        return bank_slip(amount, due_date)
    
    else:
        return "Tipo de pagamento inválido"
    
def list_courses(courses):
    for course in courses:
        print(f"Curso: Carga Horária: {course.workload}, Preço: {course.price}, Aulas: {course.classes}")

def list_users(users):
    for user in users:
        print(f"Curso: Nome: {user.name}, Aulas ou cursos: {user.classes}")

def list_payments(payments):
    pass

def list_registations(courses):
    for course in courses:
        print(f"Curso: Carga Horária: {course.workload}, Preço: {course.price}, Aulas: {course.classes}")

def menu():
    print("--======== Sistema de Marketplace Educacional ========--")
    print("1. Cadastrar Curso\n 2. Cadastrar Usuário\n 3. Matricular Aluno\n 4. Processar Pagamento\n 5. Listar Cursos\n 6. Sair")
    option = int(input("Selecione uma opção:"))

    courses = []
    users = []
    registrations = []

    if option == 1:
        courses.append(create_course())
        list_courses(courses)
    


if __name__ == '__main__':
    menu()
