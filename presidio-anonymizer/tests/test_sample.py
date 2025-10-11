from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer():
    result = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Check anonymized text
    assert result.text == "My name is BIP."

    # Check that exactly one item is in the results
    assert len(result.items) == 1

    # Extract the anonymized item
    item = result.items[0]

    # Check start and end indexes
    assert item.start == 11
    assert item.end == 14

    # Check entity type and anonymized text
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"
