from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer():
    """Test that the function anonymizes 'My name is Bond.' correctly."""
    # Call the function with the example input
    result = sample_run_anonymizer("My name is Bond.", 11, 15)
    
    # Verify the anonymized text
    assert result.text == "My name is BIP."
    
    # Verify the result has items
    assert len(result.items) == 1
    
    # Get the first item
    item = result.items[0]
    
    # Verify the start position
    assert item.start == 11
    
    # Verify the end position
    assert item.end == 14
    
    # Verify other item details
    assert item.entity_type == 'PERSON'
    assert item.text == 'BIP'
    assert item.operator == 'replace'