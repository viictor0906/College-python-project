from aluno import Aluno
from curso import Curso
from modulo import Modulo
from professor import Professor

professores = []
alunos = []
cursos = []
modulos = []

def exibir_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Criar Professor")
    print("2. Criar Aluno")
    print("3. Criar Curso")
    print("4. Criar Módulo")
    print("5. Associar Professor a um Curso")
    print("6. Matricular Aluno em um Curso")
    print("7. Adicionar Módulo a um Curso")
    print("8. Marcar Módulo como Concluído para um Aluno")
    print("9. Consultar Progresso de um Aluno")
    print("10. Exibir Informações de um Aluno")
    print("11. Exibir Informações de um Professor")
    print("12. Exibir Informações de um Curso")
    print("13. Sair")


def criar_professor():
    nome = input("Nome do Professor: ")
    cpf = input("CPF do Professor: ")
    especializacao = input("Especialização do Professor: ")
    professor = Professor(nome, cpf, especializacao, 0)
    professores.append(professor)
    print(f"Professor {nome} criado com sucesso!")


def criar_aluno():
    nome = input("Nome do Aluno: ")
    cpf = input("CPF do Aluno: ")
    email = input("Email do Aluno: ")
    aluno = Aluno(nome, cpf, email)
    alunos.append(aluno)
    print(f"Aluno {nome} criado com sucesso!")


def criar_curso():
    nome = input("Nome do Curso: ")
    descricao = input("Descrição do Curso: ")
    aulas = int(input("Número de Aulas do Curso: "))
    curso = Curso(nome, descricao, aulas)
    cursos.append(curso)
    print(f"Curso {nome} criado com sucesso!")


def criar_modulo():
    titulo = input("Título do Mjoinódulo: ")
    descricao = input("Descrição do Módulo: ")
    modulo = Modulo(titulo, descricao)
    modulos.append(modulo)
    print(f"Módulo {titulo} criado com sucesso!")


def associar_professor_curso():
    nome_professor = input("Nome do Professor: ")
    nome_curso = input("Nome do Curso: ")
    professor = next((p for p in professores if p.nome == nome_professor), None)
    curso = next((c for c in cursos if c.nome_curso == nome_curso), None)
    if professor and curso:
        curso.cdrProfessor = professor
        curso.cdrAssociado = professor
        print(f"Professor {nome_professor} associado ao curso {nome_curso}.")
    else:
        print("Professor ou curso não encontrado.")


def matricular_aluno_curso():
    nome_aluno = input("Nome do Aluno: ")
    nome_curso = input("Nome do Curso: ")
    aluno = next((a for a in alunos if a.nome == nome_aluno), None)
    curso = next((c for c in cursos if c.nome_curso == nome_curso), None)
    if aluno and curso:
        curso.cdrAluno = aluno
        print(f"Aluno {nome_aluno} matriculado no curso {nome_curso}.")
    else:
        print("Aluno ou curso não encontrado.")


def adicionar_modulo_curso():
    titulo_modulo = input("Título do Módulo: ")
    nome_curso = input("Nome do Curso: ")
    modulo = next((m for m in modulos if m.titulo == titulo_modulo), None)
    curso = next((c for c in cursos if c.nome_curso == nome_curso), None)
    if modulo and curso:
        curso.cdrModulo = modulo
        print(f"Módulo {titulo_modulo} adicionado ao curso {nome_curso}.")
    else:
        print("Módulo ou curso não encontrado.")


def marcar_modulo_concluido():
    nome_aluno = input("Nome do Aluno: ")
    titulo_modulo = input("Título do Módulo: ")
    nome_curso = input("Nome do Curso: ")
    aluno = next((a for a in alunos if a.nome == nome_aluno), None)
    modulo = next((m for m in modulos if m.titulo == titulo_modulo), None)
    curso = next((c for c in cursos if c.nome_curso == nome_curso), None)
    if aluno and modulo and curso:
        curso.marcarModuloConcluido(aluno, modulo)
        print(
            f"Módulo {titulo_modulo} marcado como concluído para o aluno {nome_aluno}."
        )
    else:
        print("Aluno, módulo ou curso não encontrado.")


def consultar_progresso_aluno():
    nome_aluno = input("Nome do Aluno: ")
    nome_curso = input("Nome do Curso: ")
    aluno = next((a for a in alunos if a.nome == nome_aluno), None)
    curso = next((c for c in cursos if c.nome_curso == nome_curso), None)
    if aluno and curso:
        aluno.consultar_progresso(curso)
    else:
        print("Aluno ou curso não encontrado.")


def exibir_info_aluno():
    nome_aluno = input("Nome do Aluno: ")
    aluno = next((a for a in alunos if a.nome == nome_aluno), None)
    if aluno:
        aluno.exibir_info_aluno()
    else:
        print("Aluno não encontrado.")


def exibir_info_professor():
    nome_professor = input("Nome do Professor: ")
    professor = next((p for p in professores if p.nome == nome_professor), None)
    if professor:
        professor.consProfessor()
    else:
        print("Professor não encontrado.")


def exibir_info_curso():
    nome_curso = input("Nome do Curso: ")
    curso = next((c for c in cursos if c.nome_curso == nome_curso), None)
    if curso:
        curso.consCurso()
    else:
        print("Curso não encontrado.")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            criar_professor()
        elif opcao == "2":
            criar_aluno()
        elif opcao == "3":
            criar_curso()
        elif opcao == "4":
            criar_modulo()
        elif opcao == "5":
            associar_professor_curso()
        elif opcao == "6":
            matricular_aluno_curso()
        elif opcao == "7":
            adicionar_modulo_curso()
        elif opcao == "8":
            marcar_modulo_concluido()
        elif opcao == "9":
            consultar_progresso_aluno()
        elif opcao == "10":
            exibir_info_aluno()
        elif opcao == "11":
            exibir_info_professor()
        elif opcao == "12":
            exibir_info_curso()
        elif opcao == "13":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
