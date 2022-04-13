from datetime import datetime
from mock_repository import FakeRepository


def test_get_batch(mock_list_of_batches):
    batches = mock_list_of_batches
    repo = FakeRepository(batches)
    assert repo.get(reference="A001") == []


def test_add_batch(mock_batch_generate):
    batches = set()
    batch = mock_batch_generate("REF0001", "TABLE-010", 20, datetime.now())
    repo = FakeRepository(batches=batches)
    repo.add(batch=batch)
    assert len(repo.list()) > 0


def test_remove_batch(mock_batch_generate):
    # add a new batch, firstly
    batches = set()
    batch = mock_batch_generate()
    repo = FakeRepository(batches)
    repo.add(batch=batch)
    assert len(repo.list()) > 0

    # now, let's remove the batch
    repo.remove(batch=batch)
    assert len(repo.list()) == 0


def test_list_all_batches(mock_list_of_batches):
    batches = mock_list_of_batches
    repo = FakeRepository(batches=batches)
    list_of_batches = repo.list()
    assert len(list_of_batches) == 4
