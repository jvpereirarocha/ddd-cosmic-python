def test_can_allocate(mock_order_line_generate, mock_batch_generate):
    order_line = mock_order_line_generate(
        "ref001", "CHAIR-001", 5
    )
    assert order_line is not None
    batch = mock_batch_generate(
        "",
        "CHAIR-001",
        100
    )
    assert batch.can_allocate(order_line) is True
