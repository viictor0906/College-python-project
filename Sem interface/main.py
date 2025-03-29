from pessoa import Pessoa
from aluno import Aluno
from professor import Professor
from modulo import Modulo
from curso import Curso
def main():
    Schalata = Professor("Schalata", "123.123.123-12", "Professor", 0)
    Miguel = Professor("Miguel", "444.444.444-44", "Banco de Dados", 0)
    Poo = Modulo("POO", "Aulas de POO")
    Bd = Modulo("Banco de dados", "Fazer Banco de dados")
    Michel = Aluno("Michel", "321.321.321-21", "michelbatata@email-example.com")
    Arthur = Aluno("Arthur", "000.000.000-00", "Arthur@email.com")
    Si = Curso("SI", "Aulas de Programação", 0)

    Si.cdrCurso = Si
    Si.cdrAluno = Arthur
    Si.cdrAluno = Michel
    Si.cdrProfessor = Schalata
    Si.cdrAssociado = Schalata
    Si.cdrProfessor = Miguel
    Si.cdrAssociado = Miguel
    Si.cdrModulo = Poo
    Si.cdrModulo = Bd

    Si.att_aulas_curso(3)
    Schalata.att_aulas_professor(5)
    Miguel.att_aulas_professor(10)

    Schalata.consProfessor()
    Miguel.consProfessor()

    Michel.marcar_modulo_concluido(Si, Poo)
    Michel.marcar_modulo_concluido(Si, Bd)

    Michel.consultar_progresso(Si)
    Arthur.consultar_progresso(Si)

    Arthur.exibir_info_aluno()
    Michel.exibir_info_aluno()

    Poo.att_modulo("POO 2", "poo 2")
    Poo.consModulo()
    Bd.consModulo()
    Si.consCurso()
if __name__ == "__main__":
    main()