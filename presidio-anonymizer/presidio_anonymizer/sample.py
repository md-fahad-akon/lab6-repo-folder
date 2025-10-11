from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


def sample_run_anonymizer(text, start, end):
    """Return anonymization result for given text and indices."""
    engine = AnonymizerEngine()
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})},
    )
    return result


if __name__ == "__main__":
    text = "My name is Bond."
    start = 11
    end = 15
    result = sample_run_anonymizer(text, start, end)
    print(f"text: {result.text}")
    print("items:")
    print("[")
    for item in result.items:
        print(
            f"    {{'start': {item.start}, 'end': {item.end}, 'entity_type': '{item.entity_type}', "
            f"'text': '{item.text}', 'operator': '{item.operator}'}}"
        )
    print("]")
