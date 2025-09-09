import sys
import os

# Garante que o Python veja a pasta raiz
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classes.paciente import Paciente

def listar_pacientes(pacientes):
    if not pacientes:
        print("\nNenhum paciente cadastrado.")
    else:
        print("\n--- Lista de Pacientes ---")
        for i, p in enumerate(pacientes, start=1):
            print(f"{i}. Nome: {p.NomePaciente} | ID: {p.PacienteID} | "
                  f"Data Nascimento: {p.DataNascimento} | Endereço: {p.EnderecoPaciente} | "
                  f"Telefone: {p.telPaciente} | CidadeID: {p.CidadeID} | "
                  f"Peso: {p.peso} kg | Altura: {p.Altura} m | IMC: {p.calcular_imc()}")

    

def main():
    pacientes_registrados = []

    while True:
        print("\n--- MENU PACIENTES ---")
        print("1 - Cadastrar Paciente")
        print("2 - Listar Pacientes")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo = Paciente.cadastrar()
            pacientes_registrados.append(novo)
            print(f"\n✅ Paciente {novo.NomePaciente} (ID: {novo.PacienteID}) cadastrado com sucesso!")
        elif opcao == "2":
            listar_pacientes(pacientes_registrados)
        elif opcao == "3":
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
