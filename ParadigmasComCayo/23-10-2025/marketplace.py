from abc import ABC, abstractmethod

# ============ CLASSES DE USUÁRIOS ============
class user(ABC):
    """Classe abstrata base para usuários - Demonstra ABSTRAÇÃO"""
    def __init__(self, name):
        self.__name = name  # Atributo privado - Demonstra ENCAPSULAMENTO
    
    @property
    def name(self):
        """Getter para acesso controlado - Demonstra ENCAPSULAMENTO"""
        return self.__name
    
    @abstractmethod
    def get_role(self):
        """Método abstrato - Demonstra ABSTRAÇÃO"""
        pass

class student(user):
    """Classe Aluno - Demonstra HERANÇA"""
    def __init__(self, name, classes):
        super().__init__(name)
        self._classes = classes  # Atributo protegido
    
    def get_role(self):
        """Implementação do método abstrato - Demonstra POLIMORFISMO"""
        return "Estudante"

class teacher(user):
    """Classe Professor - Demonstra HERANÇA"""
    def __init__(self, name, classes):
        super().__init__(name)
        self._classes = classes
    
    def get_role(self):
        """Implementação do método abstrato - Demonstra POLIMORFISMO"""
        return "Professor"
    
    @staticmethod
    def list_users(users):
        """Lista usuários cadastrados"""
        if not users:
            print("Nenhum usuário cadastrado.")
            return
        
        print("\n--- USUÁRIOS CADASTRADOS ---")
        for user in users:
            print(f"{user.get_role()}: {user.name}")

    @staticmethod
    def register_user():
        """Cadastra novo usuário usando dicionário"""
        user_type = input("Tipo (Estudante/Professor/Coordenador): ").lower()
        name = input("Nome: ")
        classes = input("Cursos: ")

        # Dicionário para mapear tipos de usuários
        user_types = {
            "estudante": student,
            "professor": teacher,
            "coordenador": organizer
        }
        
        user_class = user_types.get(user_type)
        if user_class:
            return user_class(name, classes)
        else:
            print("Tipo inválido!")
            return None

class organizer(user):
    """Classe Organizador - Demonstra HERANÇA"""
    def __init__(self, name, courses):
        super().__init__(name)
        self._courses = courses
    
    def get_role(self):
        """Implementação do método abstrato - Demonstra POLIMORFISMO"""
        return "Coordenador"

    @staticmethod
    def process_payment():
        """Processa pagamento usando dicionário"""
        payment_type = input("Tipo (Pix/Cartão/Boleto): ").lower()
        amount = float(input("Valor: R$ "))

        # Dicionário para mapear tipos de pagamento
        payment_types = {
            "pix": lambda: pix(amount, input("Chave Pix: ")),
            "cartão": lambda: credit_card(amount, input("Número do cartão: "), input("Titular: ")),
            "boleto": lambda: bank_slip(amount, input("Vencimento: "))
        }
        
        payment_function = payment_types.get(payment_type)
        if payment_function:
            return payment_function()
        else:
            print("Tipo de pagamento inválido!")
            return None
    
    @staticmethod
    def create_registration(users, turmas):
        """Cria matrícula de aluno em turma"""
        students_list = [u for u in users if isinstance(u, student)]
        if not students_list:
            print("Nenhum estudante cadastrado!")
            return None
        
        print("\n--- ESTUDANTES ---")
        for i, s in enumerate(students_list, 1):
            print(f"{i}. {s.name}")
        
        student_idx = int(input("Número do estudante: ")) - 1
        selected_student = students_list[student_idx]
        
        if not turmas:
            print("Nenhuma turma cadastrada!")
            return None
        
        print("\n--- TURMAS ---")
        for i, t in enumerate(turmas, 1):
            print(f"{i}. {t.course.name} - Vagas: {t.available_slots}/{t._total_slots}")
        
        turma_idx = int(input("Número da turma: ")) - 1
        selected_turma = turmas[turma_idx]
        
        new_registration = registration(selected_student, selected_turma)
        selected_turma.enroll_student(selected_student)
        
        print("Matrícula realizada!")
        return new_registration
    
    @staticmethod
    def list_courses(courses):
        """Lista cursos cadastrados"""
        if not courses:
            print("Nenhum curso cadastrado.")
            return
        
        print("\n--- CURSOS CADASTRADOS ---")
        for course in courses:
            print(f"{course.name} | {course.workload}h | R$ {course.price:.2f}")

    @staticmethod
    def create_course():
        """Cria novo curso"""
        name = input("Nome do curso: ")
        workload = int(input("Carga horária: "))
        price = float(input("Preço: R$ "))
        classes = input("Aulas: ")

        new_course = course(name, workload, price, classes)
        print(f"Curso '{name}' criado!")
        return new_course

# ============ CLASSES DE PAGAMENTO ============
class payment(ABC):
    """Classe abstrata para pagamentos - Demonstra ABSTRAÇÃO"""
    def __init__(self, amount):
        self.__amount = amount  # Atributo privado - Demonstra ENCAPSULAMENTO
    
    @property
    def amount(self):
        """Getter para acesso controlado - Demonstra ENCAPSULAMENTO"""
        return self.__amount
    
    @abstractmethod
    def process(self):
        """Método abstrato - Demonstra ABSTRAÇÃO e POLIMORFISMO"""
        pass

class pix(payment):
    """Pagamento via Pix - Demonstra HERANÇA"""
    def __init__(self, amount, pix_key):
        super().__init__(amount)
        self.__pix_key = pix_key
    
    def process(self):
        """Implementação específica - Demonstra POLIMORFISMO"""
        return f"Pix de R$ {self.amount:.2f} processado (chave: {self.__pix_key})"

class credit_card(payment):
    """Pagamento via Cartão - Demonstra HERANÇA"""
    def __init__(self, amount, card_number, card_holder):
        super().__init__(amount)
        self.__card_number = card_number
        self.__card_holder = card_holder
    
    def process(self):
        """Implementação específica - Demonstra POLIMORFISMO"""
        return f"Cartão de {self.__card_holder} - R$ {self.amount:.2f} processado"

class bank_slip(payment):
    """Pagamento via Boleto - Demonstra HERANÇA"""
    def __init__(self, amount, due_date):
        super().__init__(amount)
        self.__due_date = due_date
    
    def process(self):
        """Implementação específica - Demonstra POLIMORFISMO"""
        return f"Boleto de R$ {self.amount:.2f} - Vencimento: {self.__due_date}"

# ============ CLASSES DE CURSO E TURMA ============
class course:
    """Classe Curso - Demonstra COMPOSIÇÃO (tem turmas)"""
    def __init__(self, name, workload, price, classes):
        self.__name = name  # Privado
        self.__price = price
        self.__workload = workload
        self._classes = classes  # Protegido
        self._turmas = []  # Composição: curso tem turmas
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @property
    def workload(self):
        return self.__workload
    
    def add_class(self, turma):
        self._turmas.append(turma)

class turma:
    """Classe Turma - Demonstra ASSOCIAÇÃO (com instrutor) e COMPOSIÇÃO (pertence a curso)"""
    def __init__(self, course, instructor, start_date, end_date, total_slots):
        self.__course = course  # Composição
        self.__instructor = instructor  # Associação
        self.__start_date = start_date
        self.__end_date = end_date
        self._total_slots = total_slots
        self._enrolled_students = []
    
    @property
    def course(self):
        return self.__course
    
    @property
    def instructor(self):
        return self.__instructor
    
    @property
    def available_slots(self):
        return self._total_slots - len(self._enrolled_students)
    
    def enroll_student(self, student):
        """Matricula aluno na turma"""
        if self.available_slots > 0:
            self._enrolled_students.append(student)
        else:
            print("Turma cheia!")

class registration:
    """Classe Matrícula - Demonstra ASSOCIAÇÃO entre aluno e turma"""
    def __init__(self, student, turma):
        self.__student = student
        self.__turma = turma
    
    @property
    def student(self):
        return self.__student
    
    @property
    def turma(self):
        return self.__turma

# ============ FUNÇÕES AUXILIARES ============
def list_payments(payments):
    """Lista pagamentos"""
    if not payments:
        print("Nenhum pagamento registrado.")
        return
    
    print("\n--- PAGAMENTOS ---")
    total = 0
    for pmt in payments:
        print(pmt.process())
        total += pmt.amount
    print(f"TOTAL: R$ {total:.2f}")

def list_registrations(registrations):
    """Lista matrículas"""
    if not registrations:
        print("Nenhuma matrícula.")
        return
    
    print("\n--- MATRÍCULAS ---")
    for reg in registrations:
        print(f"{reg.student.name} -> {reg.turma.course.name}")

def create_class(courses, users):
    """Cria turma"""
    if not courses:
        print("Nenhum curso cadastrado!")
        return None
    
    print("\n--- CURSOS ---")
    for i, c in enumerate(courses, 1):
        print(f"{i}. {c.name}")
    
    course_idx = int(input("Número do curso: ")) - 1
    selected_course = courses[course_idx]
    
    teachers = [u for u in users if isinstance(u, teacher)]
    if not teachers:
        print("Nenhum professor cadastrado!")
        return None
    
    print("\n--- PROFESSORES ---")
    for i, t in enumerate(teachers, 1):
        print(f"{i}. {t.name}")
    
    teacher_idx = int(input("Número do professor: ")) - 1
    selected_teacher = teachers[teacher_idx]
    
    start_date = input("Data início: ")
    end_date = input("Data fim: ")
    slots = int(input("Vagas: "))
    
    new_turma = turma(selected_course, selected_teacher, start_date, end_date, slots)
    selected_course.add_class(new_turma)
    
    print("Turma criada!")
    return new_turma

def revenue_report(payments):
    """Relatório de faturamento"""
    if not payments:
        print("Nenhum pagamento.")
        return
    
    total = sum(p.amount for p in payments)
    print(f"\n--- FATURAMENTO ---")
    print(f"Total de pagamentos: {len(payments)}")
    print(f"Faturamento: R$ {total:.2f}")

def popular_courses_report(registrations):
    """Relatório de cursos populares"""
    if not registrations:
        print("Nenhuma matrícula.")
        return
    
    courses_count = {}
    for reg in registrations:
        name = reg.turma.course.name
        courses_count[name] = courses_count.get(name, 0) + 1
    
    print("\n--- CURSOS MAIS POPULARES ---")
    for course, count in sorted(courses_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{course}: {count} matrícula(s)")

# ============ MENU PRINCIPAL ============
def menu():
    courses = []
    users = []
    registrations = []
    payments = []
    turmas = []
    
    # Dicionário de opções do menu principal
    menu_options = {
        1: lambda: courses.append(organizer.create_course()) if organizer.create_course() else None,
        2: lambda: users.append(teacher.register_user()) if teacher.register_user() else None,
        3: lambda: turmas.append(create_class(courses, users)) if create_class(courses, users) else None,
        4: lambda: registrations.append(organizer.create_registration(users, turmas)) if organizer.create_registration(users, turmas) else None,
        5: lambda: handle_payment(payments),
        6: lambda: organizer.list_courses(courses),
        7: lambda: teacher.list_users(users),
        8: lambda: handle_reports(payments, registrations),
        9: lambda: print("Encerrando...")
    }
    
    option = 0
    
    while option != 9:
        print("\n========== MARKETPLACE EDUCACIONAL ==========\n1. Cadastrar Curso\n2. Cadastrar Usuário\n3. Criar Turma\n4. Matricular Aluno\n5. Processar Pagamento\n6. Listar Cursos\n7. Listar Usuários\n8. Relatórios\n9. Sair\n=============================================")
        
        option = int(input("Opção: "))
        
        action = menu_options.get(option)
        if action:
            action()
        else:
            print("Opção inválida!")

def handle_payment(payments):
    """Manipula o processamento de pagamento"""
    payment = organizer.process_payment()
    if payment:
        payments.append(payment)
        print(payment.process())

def handle_reports(payments, registrations):
    """Manipula os relatórios usando dicionário"""
    print("\n1. Faturamento\n2. Cursos Populares")
    sub = int(input("Opção: "))
    
    # Dicionário de relatórios
    reports = {
        1: lambda: revenue_report(payments),
        2: lambda: popular_courses_report(registrations)
    }
    
    report = reports.get(sub)
    if report:
        report()
    else:
        print("Opção inválida!")

if __name__ == '__main__':
    menu()