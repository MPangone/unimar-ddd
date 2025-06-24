from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional
import uuid

<<<<<<< HEAD
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
=======
@dataclass
class Emprestimo:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    livro_id: str = ""
    usuario_id: str = ""
    data_emprestimo: datetime = field(default_factory=datetime.utcnow)
    data_devolucao_prevista: datetime = field(default_factory=lambda: datetime.utcnow() + timedelta(days=14))
    data_devolucao_real: Optional[datetime] = None
    multa: float = 0.0
    
    def __post_init__(self):
        if not self.livro_id:
            raise ValueError("ID do livro é obrigatório")
        if not self.usuario_id:
            raise ValueError("ID do usuário é obrigatório")
    
    def devolver(self) -> float:
        if self.data_devolucao_real:
            raise ValueError("Livro já foi devolvido")
        
        self.data_devolucao_real = datetime.utcnow()
        self.multa = self._calcular_multa()
        return self.multa
    
    def _calcular_multa(self) -> float:
        if not self.data_devolucao_real:
            return 0.0
        
        if self.data_devolucao_real <= self.data_devolucao_prevista:
            return 0.0
        
        dias_atraso = (self.data_devolucao_real - self.data_devolucao_prevista).days
        return dias_atraso * 1.0 
    
    @property
    def esta_em_atraso(self) -> bool:
 
        if self.data_devolucao_real:
            return False 
        return datetime.now() > self.data_devolucao_prevista
    
    @property
    def dias_atraso(self) -> int:
        if not self.esta_em_atraso:
            return 0
        return (datetime.utcnow() - self.data_devolucao_prevista).days
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Emprestimo):
            return False
        return self.id == other.id
    
    def __hash__(self) -> int:
        return hash(self.id)
>>>>>>> 6788e5bc1520b9b72179d4e935c4858e4fca73fa
