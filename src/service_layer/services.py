from typing import Iterator
from src.domain import model
from src.adapters.repository import AbstractRepository
from src import InvalidSku


def is_valid_sku(sku: str, batches: Iterator[model.Batch]) -> bool:
    return sku in {batch.sku for batch in batches}

def allocate(line: model.OrderLine, repo: AbstractRepository, session) -> str:
    batches = repo.list()
    if not is_valid_sku(line.sku, batches=batches):
        raise InvalidSku(f"Invalid sku {line.sku}")
    batch_reference = model.allocate(line, batches)
    session.commit()
    return batch_reference