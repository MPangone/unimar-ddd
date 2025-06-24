from src.domain.entities.usuario import Usuario
from src.domain.value_objects.email import Email
from src.domain.repositories.usuario_repostory import IUsuarioRepository

class CriarUsuarioUseCase:
    def __init__(self, usuario_repository: IUsuarioRepository):
        self.usuario_repository = usuario_repository

    def execute(self, nome: str, email: str) -> Usuario:
        usuario = Usuario(nome=nome, email=Email(email))
        self.usuario_repository.salvar(usuario)
        return usuario