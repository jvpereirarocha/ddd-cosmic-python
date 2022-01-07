import abc
from src.domain.model import Batch


class AbstractRepository(abc.ABC):
    
    @abc.abstractmethod
    def add(self, batch: Batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference: str) -> Batch:
        raise NotImplementedError
    
    @abc.abstractmethod
    def list(self):
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def get(self, reference: str):
        self.session.query(Batch).filter_by(reference=reference).one()

    def add(self, batch: Batch):
        self.session.add(batch)

    def list(self):
        self.session.query(Batch).all()
