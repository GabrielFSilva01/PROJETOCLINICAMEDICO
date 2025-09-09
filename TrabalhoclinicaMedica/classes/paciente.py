

class Paciente:
    def __init__(self, PacienteID, NomePaciente, DataNascimento, EnderecoPaciente,
                 telPaciente, CidadeID, peso, Altura):
        self.PacienteID = PacienteID
        self.NomePaciente = NomePaciente
        self.DataNascimento = DataNascimento
        self.EnderecoPaciente = EnderecoPaciente
        self.telPaciente = telPaciente
        self.CidadeID = CidadeID
        self.peso = float(peso)
        self.Altura = float(Altura)

    @classmethod
    def cadastrar(cls):
        PacienteID = input("Digite o ID do paciente: ")
        NomePaciente = input("Digite o nome do paciente: ")
        DataNascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
        EnderecoPaciente = input("Digite o endereço do paciente: ")
        telPaciente = input("Digite o telefone do paciente: ")
        CidadeID = input("Digite o ID da cidade: ")
        peso = float(input("Digite o peso do paciente (kg): "))
        Altura = float(input("Digite a altura do paciente (m): "))
        return cls(PacienteID, NomePaciente, DataNascimento, EnderecoPaciente,
                   telPaciente, CidadeID, peso, Altura)

    def calcular_imc(self):
        imc = self.peso / (self.Altura ** 2)
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade grau I"
        elif 35 <= imc < 39.9:
            return "Obesidade grau II"
        else:
            return "Obesidade grau III"
