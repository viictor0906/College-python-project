from pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, cpf, email):
        super().__init__(nome, cpf)
        self.__email = email
        self.__historico = []
        self.__progresso = {}

    def atualizar_aluno(self, novo_nome, novo_cpf, novo_email):
        self.nome = novo_nome
        self.cpf = novo_cpf
        self.__email = novo_email

    @property
    def historico(self):
        return self.__historico

    
    def adicionar_curso_historico(self, curso):
        if curso not in self.__historico:
            self.__historico.append(curso)
            self.__progresso[curso] = {"modulos_concluidos": [], "concluido": False}
        else:
            print("Curso já está no histórico.")

    def marcar_modulo_concluido(self, curso, modulo):
        if modulo not in self.__progresso[curso]["modulos_concluidos"]:
            self.__progresso[curso]["modulos_concluidos"].append(modulo)
        todos_concluidos = all(m in self.__progresso[curso]["modulos_concluidos"] for m in curso.modulos_list)
        self.__progresso[curso]["concluido"] = todos_concluidos

    def consultar_progresso(self, curso):
        if curso not in self.__progresso:
            print(f"Aluno não está matriculado no curso '{curso.nome_curso}'.")
        else:
            print(f"---Progresso do curso, Aluno:{self.nome}---")
            print(f" Progresso no curso '{curso.nome_curso}':")
        for modulo in curso.modulos_list:
            status = "Concluído" if modulo in self.__progresso[curso]["modulos_concluidos"] else "Pendente"
            print(f"    {modulo.titulo}: {status}")
        if self.__progresso[curso]["concluido"]:
            print(f"    Curso '{curso.nome_curso}' concluído!")
        else:
            print(f"    Curso '{curso.nome_curso}' ainda não foi concluído.")

    def exibir_info_aluno(self):
        print(f"-----INFO {self.nome}-----")
        print(f"    Nome: {self.nome}")
        print(f"    CPF: {self.cpf}")
        print(f"    Email: {self.__email}")
        print(f"    Histórico: {' ,'.join(curso.nome_curso for curso in self.__historico)}")
        print(f"    Progresso:")
        for curso, progresso in self.__progresso.items():
            concluidos = len(progresso["modulos_concluidos"])
            total = len(curso.modulos_list)
            status = "Concluído"  if progresso["concluido"] else "Pendente"
            print(f"     -{curso.nome_curso}: {concluidos}/{total} módulos concluídos ({status})")