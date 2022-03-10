from typing import Set, Optional, List
from src.adapters.repository import AbstractRepository
from src.domain.model import Batch


class FakeRepository(AbstractRepository):
    def __init__(self, batches: Set[Batch]) -> None:
        self._batches = set(batches)

    def add(self, batch: Batch):
        self._batches.add(batch)

    def get(self, reference: str) -> Optional[List[Batch]]:
        return [batch for batch in self._batches if batch.reference == reference]

    def list(self):
        return list(self._batches)
