from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional
import uuid

from .livro import Livro
from .usuario import Usuario

@dataclass
class Emprestimo:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    livro: Livro = None
    usuario: Usuario = None
    data_emprestimo: datetime = field(default_factory=datetime.now)
    data_devolucao: Optional[datetime] = None
    data_prevista_devolucao: datetime = field(default_factory=lambda: datetime.now() + timedelta(days=7))
    devolvido: bool = False

    def __post_init__(self):
        self._validar_invariantes()

    def _validar_invariantes(self):
        if not self.livro:
            raise ValueError("Livro é obrigatório para o empréstimo.")
        if not self.usuario:
            raise ValueError("Usuário é obrigatório para o empréstimo.")
        if self.data_devolucao and self.data_devolucao < self.data_emprestimo:
            raise ValueError("Data de devolução não pode ser anterior à data de empréstimo.")

    def devolver(self):
        if self.devolvido:
            raise ValueError("Este empréstimo já foi devolvido.")
        self.data_devolucao = datetime.now()
        self.devolvido = True
        self.livro.devolver()

    @property
    def em_atraso(self) -> bool:
        if self.devolvido:
            return False
        return datetime.now() > self.data_prevista_devolucao

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "livro": self.livro.to_dict() if self.livro else None,
            "usuario": self.usuario.to_dict() if self.usuario else None,
            "data_emprestimo": self.data_emprestimo.isoformat(),
            "data_prevista_devolucao": self.data_prevista_devolucao.isoformat(),
            "data_devolucao": self.data_devolucao.isoformat() if self.data_devolucao else None,
            "devolvido": self.devolvido,
            "em_atraso": self.em_atraso
        }