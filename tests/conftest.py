import pytest
from datetime import datetime
from src.domain.model import Batch


@pytest.fixture(scope="function")
def mock_batch_with_eta():
    batch = Batch(
        reference="ref-001",
        sku="TEST-PRODUCT",
        quantity=10,
        eta=datetime.now()
    )
    return batch
