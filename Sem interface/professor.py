from pessoa import Pessoa
class Professor(Pessoa):  
    def __init__(self, nome, cpf, especializacao, aulas_professor):
        super().__init__(nome, cpf)
        self.__especializacao = especializacao
        self.__cursos_ministrantes = []
        self.aulas_professor = aulas_professor

    def att_professor(self, nNome, nCpf, nEspecializacao):
        self.nome = nNome
        self.cpf = nCpf
        self.__especializacao = nEspecializacao

    def att_aulas_professor(self, aulas):
        self.aulas_professor = aulas

    @property
    def cursos_ministrantes(self):
        return self.__cursos_ministrantes

    def cdrCurso(self, curso):
        if curso not in self.__cursos_ministrantes:
            self.__cursos_ministrantes.append(curso)
        else:
            print("Curso já está na lista de cursos ministrados pelo professor")

    def consProfessor(self):
        print(f"-----INFO {self.nome}-----")
        print(f"    Nome: {self.nome}")
        print(f"    CPF: {self.cpf}")
        print(f"    Especialização: {self.__especializacao}")
        print(f"    Cursos ministrantes: {', '.join([curso.nome_curso for curso in self.__cursos_ministrantes])}")
        print(f"    Número de aulas: {self.aulas_professor}")