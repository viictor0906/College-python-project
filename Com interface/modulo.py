class Modulo:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.__curso_associado = []

    def att_modulo(self, novo_titulo, novo_descricao):
        self.titulo = novo_titulo
        self.descricao = novo_descricao

    @property
    def curso_associado(self):
        return self.__curso_associado

    def cdr_curso_associado(self, curso):
        if curso not in self.__curso_associado:
            self.__curso_associado.append(curso)
        else:
            print("Curso já está na lista de cursos associados ao módulo")

    def consModulo(self):
        print(f"-----INFO {self.titulo}-----")
        print(f"    Nome: {self.titulo}")
        print(f"    Descrição: {self.descricao}")
        print(f"    Cursos Associados: {', '.join([curso.nome_curso for curso in self.__curso_associado])}")