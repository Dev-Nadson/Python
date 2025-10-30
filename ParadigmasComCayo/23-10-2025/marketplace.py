#Classes de usuários
class user(): #abstrair 
    def __init__(self, name):
        self.name = name

class student(user):
    def __init__(self, name, classes):
        super().__init__(name)
        self.classes = classes

class teacher(user):
    """
    Está é a classe professor, que tem o método de listar os usuários e registrar um usuário
    """
    def __init__(self, name, classes):
        super().__init__(name)
        self.classes = classes

    def list_users(users):
        for user in users:
            print(f"Curso: Nome: {user.name}, Aulas ou cursos: {user.classes}")

    def register_user():        
        user_type = input("Digite o tipo de usuário (Estudante, Professor, Coordenador): ")
        name = input("Digite o nome do usuário: ")
        classes = input("Digite as aulas ou cursos do usuário: ")

        if user_type in ("Estudante", "estudante"):
            user = student(name, classes)

        if user_type in ("Professor", "professor"):
            user = teacher(name, classes)

        if user_type in ("Coordenador", "coordenador"):
            user = organizer(name, classes) 

        return user

class organizer(user):
    """
    Essa é a classe de Coordenador, que tem os métodos de processar pagamento, criar um usuário, listar os cursos e criar um curso
    """
    def __init__(self, name, couses):
        super().__init__(name)
        self.couses = couses

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
        
    def create_registration():
        user_name = input("Digite o nome do aluno: ")
        course_name = input("Digite o nome do curso: ")

        new_registration = registration(user_name, course_name)
        return new_registration
    
    def list_courses(courses):
        print(courses)
        for course in courses:
            print(f"Curso: {course.name} Carga Horária: {course.workload}, Preço: {course.price}, Aulas: {course.classes}")

    def create_course():
        name = input("Digite o nome do curso: ")
        workload = input("Digite a carga horária do curso: ")
        price = float(input("Digite o preço do curso: "))
        classes = input("Digite as aulas do curso: ")

        new_course = course(name, workload, price, classes)
        return new_course

#Classes de pagamento
class payment(): #abstrair 
    """
    Essa é a classe base para os métodos de pagamento
    """
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

#Classes de curso
class course():
    def __init__(self, name, workload, price, classes):
        self.name = name
        self.price = price
        self.workload = workload
        self.classes = classes
        return self.name, self.price, self.workload, self.classes

class registration():
    def __init__(self, user, course):
        self.user = user    
        self.course = course

    
def list_payments(payments):
    for payment in payments:
        print(payment)

def list_registations(courses):
    for course in courses:
        print(f"Curso: Carga Horária: {course.workload}, Preço: {course.price}, Aulas: {course.classes}")

def menu():
    option = 0
    while option != 6:
        courses = []
        users = []
        registrations = []
        payments = []

        if option == 1:
            course = organizer.create_course()
            courses.append(course)

        if option == 2:
            users.append(teacher.register_user())    

        if option == 3:
            payments.append(organizer.process_payment())

        if option == 4:
            print("Curso op:", courses)
            organizer.list_courses(courses)

        print("--======== Sistema de Marketplace Educacional ========--")
        print("1. Cadastrar Curso \n2. Cadastrar Usuário \n3. Processar Pagamento \n4. Listar Cursos \n6. Sair")
        option = int(input("Selecione uma opção:"))

if __name__ == '__main__':
    menu()

