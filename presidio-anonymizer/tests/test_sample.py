import pytest
from presidio_anonymizer.sample import sample_run_anonymizer
from presidio_anonymizer.entities.engine.result.operator_result import OperatorResult


def test_sample_run_anonymizer():
    text_input = "My name is Bond."
    start_index = 11
    end_index = 15
    expected_text = "My name is BIP."
    expected_item_dict = {
        "start": 11,
        "end": 14,
        "entity_type": "PERSON",
        "text": "BIP",
        "operator": "replace",
    }
    actual_result = sample_run_anonymizer(text_input, start_index, end_index)

    assert actual_result.text == expected_text
    assert len(actual_result.items) == 1
    assert actual_result.items[0] == OperatorResult(**expected_item_dict)