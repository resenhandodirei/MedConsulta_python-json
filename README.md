# MedConsulta - Sistema de Gerenciamento de Consultas Médicas

## Descrição

**MedConsulta** é um sistema simples, porém robusto, desenvolvido em Python para gerenciar o agendamento de consultas médicas. O projeto visa ajudar desenvolvedores a compreender melhor a **persistência de dados** com **JSON**, ao mesmo tempo em que utiliza conceitos de **POO (Programação Orientada a Objetos)**, manipulação de datas e interação com o usuário via terminal.

O sistema permite cadastrar médicos e pacientes, agendar consultas, listar e remover consultas, e todas essas informações são salvas em um arquivo JSON, possibilitando a recuperação dos dados após o encerramento da aplicação. É uma excelente oportunidade para aprender como manipular arquivos JSON de maneira eficiente enquanto constrói um projeto real.

## Funcionalidades

- **Cadastro de Médicos e Pacientes**: Registre médicos com suas especialidades e pacientes com seu CPF.
- **Agendamento de Consultas**: Vincule um médico e um paciente a uma data e hora específica.
- **Listagem de Consultas**: Visualize todas as consultas agendadas, com possibilidade de filtrar por médico ou paciente.
- **Remoção de Consultas**: Cancele consultas facilmente.
- **Persistência com JSON**: Todas as informações de médicos, pacientes e consultas são armazenadas em um arquivo JSON para recuperação futura.

## Objetivos de Aprendizado

Este projeto foi desenvolvido para:
- Demonstrar como usar **JSON** para persistir e recuperar dados de um sistema real.
- Aplicar conceitos de **Programação Orientada a Objetos (POO)** com classes representando Médicos, Pacientes e Consultas.
- Manipular **datas e horários** com a biblioteca `datetime` do Python.
- Gerenciar dados com boas práticas de entrada e saída de arquivos.

## Pré-requisitos

- **Python 3.x** instalado.

## Como executar o projeto

1. Clone este repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/medconsulta.git
    ```
   
2. Acesse o diretório do projeto:
    ```bash
    cd medconsulta
    ```

3. Execute o arquivo `main.py`:
    ```bash
    python main.py
    ```

4. Siga as instruções no terminal para gerenciar médicos, pacientes e consultas.

## Exemplo de Uso

### Menu Principal:

```
MedConsulta - Sistema de Gerenciamento de Consultas Médicas
1. Cadastrar Consulta
2. Listar Consultas
3. Remover Consulta
4. Sair
```

### Agendando uma consulta:

```
Escolha uma opção: 1
Nome do paciente: Ana Silva
CPF do paciente: 12345678900
Nome do médico: Dr. João Almeida
Especialidade do médico: Cardiologista
Data e Hora da consulta (YYYY-MM-DD HH:MM): 2024-10-20 14:00
Consulta agendada para Ana Silva com o Dr. João Almeida em 2024-10-20 14:00.
```

### Listando consultas:

```
Escolha uma opção: 2
Paciente: Ana Silva - Médico: Dr. João Almeida - Data/Hora: 2024-10-20 14:00
```

### Removendo uma consulta:

```
Escolha uma opção: 3
Nome do paciente: Ana Silva
Nome do médico: Dr. João Almeida
Consulta de Ana Silva com o Dr. João Almeida removida com sucesso.
```

## Estrutura do Projeto

```
medconsulta/
│
├── consultas.json       # Arquivo onde os dados de consultas são persistidos
├── main.py              # Arquivo principal da aplicação
├── README.md            # Documentação do projeto
└── .gitignore           # Arquivos/pastas a serem ignorados pelo Git
```

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **JSON**: Formato de arquivo usado para persistir os dados.
- **datetime**: Biblioteca padrão do Python para manipulação de datas e horários.

## Melhorias Futuras

- Implementação de um sistema de **notificação de consultas** por e-mail.
- **Validação avançada de entradas**, como o formato do CPF e datas.
- Interface gráfica usando `tkinter` ou `PyQt`.

## Contribuições

Contribuições são bem-vindas! Abra uma *issue* ou envie um *pull request* se tiver sugestões ou melhorias para o projeto.

---

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Contato

- **Desenvolvedor**: Larissa Corrêa
- **Email**: larissamscorrea@gmail.com
