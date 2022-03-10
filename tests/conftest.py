from typing import Optional
import pytest
from datetime import datetime
from src.domain.aggregates.model import Batch
from tests.adapters.mock_repository import FakeRepository
import random


def mock_batch_generate(
    reference: str, sku: str, quantity: int, eta: Optional[datetime] = None
):
    if not reference:
        reference = "ref-001"
    if not sku:
        sku = "TEST-PRODUCT"
    if not quantity:
        quantity = 10

    batch = Batch(reference=reference, sku=sku, quantity=quantity, eta=eta)
    return batch


@pytest.fixture(scope="function")
def mock_batch_with_eta():
    batch = mock_batch_generate(
        reference="ref-001", sku="TEST-PRODUCT", quantity=10, eta=datetime.now()
    )
    return batch


@pytest.fixture(scope="function")
def mock_list_of_batches():
    list_of_batches = []
    for i in range(0, 4):
        mock_batch = mock_batch_generate(
            reference=f"ref-00{i}",
            sku=f"TEST-PRODUCT-{i}",
            quantity=random.choice([x for x in range(0, 100)]),
            eta=datetime(year=2022, month=1, day=3),
        )
        list_of_batches.append(mock_batch)

    return list_of_batches
