from mock_repository import FakeRepository


def test_get_batch(mock_list_of_batches):
    batches = mock_list_of_batches
    repo = FakeRepository(batches)
    assert repo.get(reference="A001") == []
