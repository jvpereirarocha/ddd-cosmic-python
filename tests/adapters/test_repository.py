def test_get_batch(mock_fake_repository):
    repository = mock_fake_repository

    assert repository.get(reference="A001") is None
