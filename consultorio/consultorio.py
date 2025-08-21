class Pessoa:
    def __init__(self, nome: str, sexo: str, endereco: str, cpf: str, telefone: int, identidade: int):
        self.nome = nome
        self.sexo = sexo
        self.endereco = endereco
        self.cpf = cpf
        self.telefone = telefone
        self.identidade = identidade

    def imprimirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Sexo: {self.sexo}")
        print(f"Endereço: {self.endereco}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")
        print(f"Identidade: {self.identidade}")


class Medico(Pessoa):
    def __init__(self, nome, sexo, endereco, cpf, telefone, identidade, crm: int, especialidade: str):
        super().__init__(nome, sexo, endereco, cpf, telefone, identidade)
        self.crm = crm
        self.especialidade = especialidade

    def imprimirDados(self):
        super().imprimirDados()
        print(f"CRM: {self.crm}")
        print(f"Especialidade: {self.especialidade}")


class Paciente(Pessoa):
    def __init__(self, nome, sexo, endereco, cpf, telefone, identidade, medicacao_continua: str):
        super().__init__(nome, sexo, endereco, cpf, telefone, identidade)
        self.medicacao_continua = medicacao_continua

    def imprimirDados(self):
        super().imprimirDados()
        print(f"Medicação Contínua: {self.medicacao_continua}")


class Consulta:
    def __init__(self, paciente: Paciente, relato: str, medicamentos: str):
        self.paciente = paciente
        self.relato = relato
        self.medicamentos = medicamentos

    def imprimirConsulta(self):
        print("--- Consulta ---")
        self.paciente.imprimirDados()
        print(f"Relato: {self.relato}")
        print(f"Medicamentos: {self.medicamentos}")


class Consultorio:
    def __init__(self, medico: Medico):
        self.medico = medico
        self.pacientes = []  
        self.consultas = [] 

    def cadastrarPaciente(self, paciente: Paciente):
        self.pacientes.append(paciente)
        print(f"Paciente {paciente.nome} cadastrado com sucesso!")

    def removerPaciente(self, cpf: str):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                self.pacientes.remove(paciente)
                print(f"Paciente {paciente.nome} removido.")
                return
        print("Paciente não encontrado.")

    def cadastrarConsulta(self, consulta: Consulta):
        self.consultas.append(consulta)
        print(f"Consulta para o paciente {consulta.paciente.nome} cadastrada com sucesso!")

    def imprimirConsultasPaciente(self, cpf: str):
        print(f"Consultas para o paciente com CPF {cpf}:")
        for consulta in self.consultas:
            if consulta.paciente.cpf == cpf:
                consulta.imprimirConsulta()

    def imprimirTodosPacientes(self):
        print("--- Lista de Pacientes ---")
        for paciente in self.pacientes:
            paciente.imprimirDados()
            print("-" * 20)

    def imprimirTodasConsultas(self):
        print("--- Lista de Consultas ---")
        for consulta in self.consultas:
            consulta.imprimirConsulta()
            print("-" * 20)

    def imprimirMedico(self):
        print("--- Dados do Médico ---")
        self.medico.imprimirDados()

if __name__ == "__main__":
    medico = Medico("Dr. Ahmed", "M", "Rua A, 123", "123456789", 998877665, 11223344, 1234, "Cardiologista")

    consultorio = Consultorio(medico)

    paciente1 = Paciente("João", "F", "Rua B, 456", "987654321", 11987654321, 22334455, "Insulina")
    paciente2 = Paciente("Habib", "M", "Rua C, 789", "111222333", 11987612345, 33445566, "Bandeide")

    consultorio.cadastrarPaciente(paciente1)
    consultorio.cadastrarPaciente(paciente2)

    consulta1 = Consulta(paciente1, "Dor no peito", "Aspirina")
    consulta2 = Consulta(paciente2, "Pressão alta", "Losartana")

    consultorio.cadastrarConsulta(consulta1)
    consultorio.cadastrarConsulta(consulta2)

    consultorio.imprimirMedico()
    consultorio.imprimirTodosPacientes()
    consultorio.imprimirTodasConsultas()

    consultorio.imprimirConsultasPaciente("987654321")

    consultorio.removerPaciente("111222333")
    consultorio.imprimirTodosPacientes()
