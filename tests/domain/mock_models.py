from typing import Optional
import pytest
import random
from datetime import datetime
from src.domain.aggregates.model import Batch, OrderLine


@pytest.yield_fixture(scope="function")
def mock_batch_generate():
    def make_mock(reference: str = "", sku: str = "", quantity: int = 100, eta: Optional[datetime] = None):
        if not reference:
            reference = "ref-001"
        if not sku:
            sku = "TEST-PRODUCT"
        if not quantity:
            quantity = 10

        batch = Batch(reference=reference, sku=sku, quantity=quantity, eta=eta)
        return batch
    
    yield make_mock


@pytest.fixture(scope="function")
def mock_batch_with_eta():
    batch = mock_batch_generate(
        eta=datetime.now()
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


@pytest.yield_fixture(scope="function")
def mock_order_line_generate(
    # order_id: str = "",
    # sku: str = "",
    # quantity: int = 0,
):
    def make_mock(
        order_id: str = "",
        sku: str = "",
        quantity: int = 0,
    ):
        order_line = OrderLine(
            order_id=order_id or f"ORD-{str(random.choice([x for x in range(0, 100)])).zfill(3)}",
            sku=sku or f"TEST-PRODUCT-{random.choice([x for x in range(0, 10)])}",
            quantity=quantity or random.choice([x for x in range(0, 100)])
        )
        return order_line
    
    yield make_mock



@pytest.fixture(scope="function")
def mock_order_line(mock_order_line_generate):
    order_line = mock_order_line_generate
    yield order_line