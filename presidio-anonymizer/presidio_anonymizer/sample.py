from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text_to_anonymize: str, start_index: int, end_index: int):
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the text, 
    # analyzer results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        text=text_to_anonymize,
        analyzer_results=[
            RecognizerResult(
                entity_type="PERSON",
                start=start_index,
                end=end_index,
                score=0.8,
            )
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})},
    )

    return result

    # input should be:
    # text: My name is Bond.
    # start: 11
    # end: 15
    # 
    # output should be:
    # text: My name is BIP.
    # items:
    # [
    #     {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
    # ]

if __name__ == "__main__": 
    text = "My name is Bond."
    start = 11
    end = 15

    anonymized_result = sample_run_anonymizer(text, start, end)
    
    print(anonymized_result)
