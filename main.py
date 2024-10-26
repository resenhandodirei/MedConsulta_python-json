import json
import os
from datetime import datetime

class Medico:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def to_dict(self):
        return {
            "nome": self.nome,
            "especialidade": self.especialidade
        }

class Paciente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf
        }

class Consulta:
    def __init__(self, paciente, medico, data_hora):
        self.paciente = paciente
        self.medico = medico
        self.data_hora = data_hora

    def to_dict(self):
        return {
            "paciente": self.paciente.to_dict(),
            "medico": self.medico.to_dict(),
            "data_hora": self.data_hora.strftime('%Y-%m-%d %H:%M')
        }

class GerenciadorConsultas:
    def __init__(self, arquivo_json='consultas.json'):
        self.arquivo_json = arquivo_json
        self.consultas = self.carregar_consultas()

    def carregar_consultas(self):
        """Carrega as consultas do arquivo JSON, se existir."""
        if os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, 'r') as arquivo:
                dados = json.load(arquivo)
                consultas = []
                for consulta in dados:
                    paciente = Paciente(**consulta["paciente"])
                    medico = Medico(**consulta["medico"])
                    data_hora = datetime.strptime(consulta["data_hora"], '%Y-%m-%d %H:%M')
                    consultas.append(Consulta(paciente, medico, data_hora))
                return consultas
        return []

    def salvar_consultas(self):
        """Salva as consultas no arquivo JSON."""
        with open(self.arquivo_json, 'w') as arquivo:
            json.dump([consulta.to_dict() for consulta in self.consultas], arquivo, indent=4)

    def cadastrar_consulta(self, paciente, medico, data_hora):
        """Cadastra uma nova consulta."""
        nova_consulta = Consulta(paciente, medico, data_hora)
        self.consultas.append(nova_consulta)
        self.salvar_consultas()
        print(f"Consulta agendada para {paciente.nome} com o Dr. {medico.nome} em {data_hora.strftime('%Y-%m-%d %H:%M')}.")

    def listar_consultas(self):
        """Lista todas as consultas agendadas."""
        if not self.consultas:
            print("Nenhuma consulta agendada.")
            return
        for consulta in self.consultas:
            print(f"Paciente: {consulta.paciente.nome} - Médico: {consulta.medico.nome} - Data/Hora: {consulta.data_hora.strftime('%Y-%m-%d %H:%M')}")

    def remover_consulta(self, paciente_nome, medico_nome):
        """Remove uma consulta específica."""
        consulta_encontrada = None
        for consulta in self.consultas:
            if consulta.paciente.nome == paciente_nome and consulta.medico.nome == medico_nome:
                consulta_encontrada = consulta
                break
        if consulta_encontrada:
            self.consultas.remove(consulta_encontrada)
            self.salvar_consultas()
            print(f"Consulta de {paciente_nome} com o Dr. {medico_nome} removida com sucesso.")
        else:
            print(f"Nenhuma consulta encontrada para {paciente_nome} com o Dr. {medico_nome}.")

def exibir_menu():
    print("\nSistema de Gerenciamento de Consultas")
    print("1. Cadastrar Consulta")
    print("2. Listar Consultas")
    print("3. Remover Consulta")
    print("4. Sair")

def main():
    gerenciador = GerenciadorConsultas()

    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            nome_paciente = input("Nome do paciente: ")
            cpf_paciente = input("CPF do paciente: ")
            paciente = Paciente(nome_paciente, cpf_paciente)

            nome_medico = input("Nome do médico: ")
            especialidade_medico = input("Especialidade do médico: ")
            medico = Medico(nome_medico, especialidade_medico)

            data_hora = input("Data e Hora da consulta (YYYY-MM-DD HH:MM): ")
            data_hora = datetime.strptime(data_hora, '%Y-%m-%d %H:%M')

            gerenciador.cadastrar_consulta(paciente, medico, data_hora)

        elif opcao == '2':
            gerenciador.listar_consultas()

        elif opcao == '3':
            nome_paciente = input("Nome do paciente: ")
            nome_medico = input("Nome do médico: ")
            gerenciador.remover_consulta(nome_paciente, nome_medico)

        elif opcao == '4':
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
