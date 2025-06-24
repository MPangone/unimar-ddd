from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid
from ..value_objects.email import Email

@dataclass
class Usuario:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    nome: str 
    email: Email = None
    ativo: bool = True
    data_criacao: datetime = field(default_factory=datetime.utcnow)
    
    def __post_init__(self):
        self._validar_invariantes()
        
    def _validar_invariantes(self):
        if not self.nome or not self.nome.strip():
            raise ValueError("O nome do usuário não pode ser vazio. Ele é obrigatório")
        if not self.email or not self.email.strip():
            raise ValueError("O email do usuário não pode ser vazio. Ele é obrigatório")
        if self.email or not self.email.strip():
            raise ValueError("O email não pode ser vazio. Ele é obrigatório")
    
    def desativar(self) -> None:
        if not self.ativo:
            raise ValueError("Usuário já está inativo")
        self.ativo = False
        print(f"Usuário '{self.nome}' desativado com sucesso.")

    def ativar(self) -> None:
        if self.ativo:
            raise ValueError("Usuário já está ativo")
        self.ativo = True
        print(f"Usuário '{self.nome}' ativado com sucesso.")

    def pode_emprestar(self) -> bool:
        print(f"Usuário '{self.nome}' pode emprestar livros.")
        return self.ativo
        
    def __eq__(self, other) -> bool:
        if not isinstance(other, Usuario):
            return False
        return self.id == other.id
    
    def __hash__(self) -> int:
        return hash(self.id)
    
    def atualizar_informacoes(
            self,
            nome: Optional[str] = None,
            email: Optional[str] = None
    ) -> None:
        if nome:
            self.nome = nome
        if email:
            self.email = email
        self._validar_invariantes()
        print(f"Informações do usuário '{self.nome}' atualizadas com sucesso.")
        

        # @property
        # def idade_em_anos(self) -> Optional[int]:
        #     if not self.ano_publicacao:
        #         return None
        #     return datetime.now().year - self.ano_publicacao
        # @property
        # def status_descricao(self) -> str:
        #     return "Ativo" if self.ativo else "Inativo"

        @property
        def informacoes_completas(self) -> bool:
            return all([
                self.nome,
                self.email,
                self.ativo,
                self.data_criacao.isoformat()
            ])
        def __eq__(self, other) ->bool:
            if not isinstance(other, Usuario):
                return False
            return self.id ==  other.id
        
        def __hash__(self) -> int:
            return hash(self.id)
        
        def __str__(self) -> str:
            return f"Usuário('{self.nome}' por {self.email})"

        def __repr__(self) -> str:
                    return (
            f"Usuario(id='{self.id}', nome='{self.nome}', "
            f"email='{self.email}', ativo='{self.ativo}', "
            f"data_criacao='{self.data_criacao.isoformat()}')"
        )

        def to_dict(self) -> dict:
            return {
                "id": self.id,
                "nome": self.nome,
                "email": self.email,
                "ativo": self.ativo,
                "data_criacao": self.data_criacao.isoformat(),
            }