from dataclasses import dataclass
from typing import Optional, Set, List
from datetime import datetime

from src.domain.exceptions import OutOfStock


@dataclass(unsafe_hash=True)
class OrderLine:
    order_id: str
    sku: str
    quantity: int


class Batch:
    def __init__(
        self, reference: str, sku: str, quantity: int, eta: Optional[datetime] = None
    ):
        self.reference = reference
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = quantity
        self._allocations: Set[OrderLine] = set()

    def __repr__(self) -> str:
        return f"<Batch {self.reference}>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __gt__(self, other) -> bool:
        if not self.eta:
            return False
        if not other.eta:
            return True
        return self.eta > other.eta

    def __hash__(self) -> str:
        return hash(self.reference)

    def allocate(self, line: OrderLine) -> None:
        if self.can_allocate(line=line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine) -> None:
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.quantity for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and line.quantity <= self.available_quantity


def allocate(line: OrderLine, batches: List[Batch]) -> str:
    try:
        batch: Batch = next(
            batch for batch in sorted(batches) if batch.can_allocate(line)
        )
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f"Out of stock for sku: {line.sku}")
