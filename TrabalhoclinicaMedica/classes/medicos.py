import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from classes.cidades import Cidade
from classes.cidades import estado
from classes.cidades import descricaoEstado
from classes.especialidades import Especialidade
class Medicos:
    def __init__(self, MedicoID, NomeMedico, enderecoMedico, telMedico, cidadeID, EspecialidadeID):
        self.MedicoID = MedicoID
        self.NomeMedico = NomeMedico
        self.enderecoMedico = enderecoMedico
        self.telMedico = telMedico
        self.cidadeID = cidadeID
        self.EspecialidadeID = EspecialidadeID

    @classmethod
    def CadastrarMedicos(cls):
        MedicoID = input("Digite o ID do médico: ")
        NomeMedico = input("Digite o nome do médico: ")
        enderecoMedico = input("Digite o endereço do médico: ")
        telMedico = input("Digite o telefone do médico: ")
        cidadeID = input("Digite o ID da cidade: ")
        EspecialidadeID = input("Digite o ID da especialidade: ")
        return cls(MedicoID, NomeMedico, enderecoMedico, telMedico, cidadeID, EspecialidadeID)
    
    def exibir_medicos(self):
        self.estado=estado(self.estado, "", "")
        self.cidadeID=Cidade(self.cidadeID,"","")
        self.EspecialidadeID=Especialidade(self.EspecialidadeID,"")
        print(f"ID do Médico: {self.MedicoID}")
        print(f"Nome do Médico: {self.NomeMedico}")
        print(f"Endereço do Médico: {self.enderecoMedico}")
        print(f"Telefone do Médico: {self.telMedico}")
        print(f"ID da Cidade: {self.cidadeID}")
        print(f"ID da Especialidade: {self.EspecialidadeID}")
        print(f"Estado: {self.estado}")
        print(f"Descrição do Estado: {self.descricaoEstado}")