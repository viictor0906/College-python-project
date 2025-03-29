from pessoa import Pessoa
from aluno import Aluno
from professor import Professor
from modulo import Modulo

class Curso:
    def __init__(self, nome_curso, desc_curso, aulas_curso):
        self.nome_curso = nome_curso
        self.desc_curso = desc_curso
        self.__modulos_list = []
        self.__cursos_list = []
        self.__alunos_list = []
        self.__professor_list = []
        self.__associados_list = []
        self.aulas_curso = aulas_curso
        
    # Gerenciamento do curso
    @property
    def cursos_list(self):
        return self.__cursos_list
    
    @cursos_list.setter
    def cdrCurso(self, curso):
        if curso not in self.__cursos_list:
            self.__cursos_list.append(curso)
        else:
            print("Curso já criado!")
    
    def rmvCurso(self, curso):
        if curso not in self.__cursos_list:
            print("Curso não existe")
        else:
            self.__cursos_list.remove(curso)
    
    def att_info_curso(self, novo_nome_curso, nova_descricao_curso):
        self.nome_curso = novo_nome_curso
        self.desc_curso = nova_descricao_curso

    def att_aulas_curso(self, aulas):
        self.aulas_curso = aulas
    
    def consCurso(self):
        print(f"-----INFO {self.nome_curso}-----")
        print(f"    Nome: {self.nome_curso}")
        print(f"    Descrição: {self.desc_curso}")
        print(f"    Módulos: {', '.join([modulo.titulo for modulo in self.__modulos_list])}")
        print(f"    Quantas aulas possui este curso: {self.aulas_curso}")
        print(f"    Professor: {', '.join([professor.nome for professor in self.__associados_list])}")

    # Gerenciamento do Aluno
    @property
    def alunos_list(self):
        return self.__alunos_list

    @alunos_list.setter
    def cdrAluno(self, aluno):
        if aluno not in self.__alunos_list:
            self.__alunos_list.append(aluno)
            aluno.adicionar_curso_historico(self)
        else:
            print("Aluno já está no curso")
    
    def rmvAluno(self, aluno):
        if aluno not in self.__alunos_list:
            print("Aluno não pertence ao curso")
        else:
            self.__alunos_list.remove(aluno)

    def attAluno(self, aluno):
        if aluno not in self.__modulos_list:
            self.__modulos_list.append(aluno)
        else:
            print("Aluno já cadastrado no módulo")

    # Gerenciamento de Professores
    @property
    def professor_list(self):
        return self.__professor_list

    @professor_list.setter
    def cdrProfessor(self, professor):
        if professor not in self.__professor_list:
            self.__professor_list.append(professor)
            professor.cdrCurso(self)  # Aqui você chama o método cdrCurso do professor
        else:
            print("Professor já foi cadastrado")
                        
    def rmv_professor(self, professor):
        if professor in self.__professor_list:
            self.__professor_list.remove(professor)
        else:
            print("Professor não faz parte do curso")

    # Gerenciamento de Associados
    @property
    def associados_list(self):
        return self.__associados_list

    @associados_list.setter
    def cdrAssociado(self, associado):
        if associado in self.__associados_list:
            print("Professor já faz parte do Curso")
        else:
            self.__associados_list.append(associado)

    def rmvAssociado(self, associado):
        if associado in self.__associados_list:
            self.__associados_list.remove(associado)
        else:
            print("Professor não faz parte do Curso")

    # Gerenciamento de Módulos
    @property
    def modulos_list(self):
        return self.__modulos_list

    @modulos_list.setter
    def cdrModulo(self, modulo):
        if modulo not in self.__modulos_list:
            self.__modulos_list.append(modulo)
            modulo.cdr_curso_associado(self)
        else:
            print("Módulo já faz parte do Curso!")

    def marcarModuloConcluido(self, aluno, modulo):
        if aluno in self.__alunos_list:
            aluno.marcar_modulo_concluido(self, modulo)
        else:
            print(f"Aluno '{aluno.nome}' não está matriculado no curso '{self.nome_curso}'.")

    def consProgresso(self, aluno):
        if aluno in self.__alunos_list:
            aluno.ver_progresso(self)
        else:
            print(f"Aluno '{aluno.nome}' não está matriculado no curso '{self.nome_curso}'.")