from typing import Set
from src.adapters.repository import AbstractRepository
from src.domain.model import Batch


class FakeRepository(AbstractRepository):
    def __init__(self, batches: Set[Batch]) -> None:
        self._batches = set(batches)

    def add(self, batch: Batch):
        self._batches.add(batch)

    def get(self, reference: str):
        return next(b for b in self._batches if b.reference == reference)

    def list(self):
        return list(self._batches)