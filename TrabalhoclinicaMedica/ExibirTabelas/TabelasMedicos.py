import sys
import os

# Garante que o Python veja a pasta raiz
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classes.medicos import Medicos
def listar_medicos(medicos):
    if not medicos:
        print("\nNenhum médico cadastrado.")
    else:
        print("\n--- Lista de Médicos ---")
        for i, m in enumerate(medicos, start=1):
            print(f"{i}. Nome: {m.NomeMedico} | ID: {m.MedicoID} | "
                  f"Endereço: {m.enderecoMedico} | Telefone: {m.telMedico} | "
                  f"CidadeID: {m.cidadeID} | EspecialidadeID: {m.EspecialidadeID}")
def main():
    medicos_registrados = []

    while True:
        print("\n--- MENU MÉDICOS ---")
        print("1 - Cadastrar Médico")
        print("2 - Listar Médicos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo = Medicos.CadastrarMedicos()
            medicos_registrados.append(novo)
            print(f"\n✅ Médico {novo.NomeMedico} (ID: {novo.MedicoID}) cadastrado com sucesso!")
        elif opcao == "2":
            listar_medicos(medicos_registrados)
        elif opcao == "3":
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()