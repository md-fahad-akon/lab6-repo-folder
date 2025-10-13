import unittest
from presidio_anonymizer.sample import sample_run_anonymizer


class TestSampleRunAnonymizer(unittest.TestCase):
    """Unit tests for the sample_run_anonymizer function."""
    
    def test_default_parameters_anonymizes_correctly(self):
        """Test that the function anonymizes 'My name is Bond.' correctly with default parameters."""
        result = sample_run_anonymizer()
        
        # Verify the anonymized text
        self.assertEqual(result.text, "My name is BIP.")
        
        # Verify the result has items
        self.assertIsNotNone(result.items)
        self.assertEqual(len(result.items), 1)
        
        # Verify the item details
        item = result.items[0]
        self.assertEqual(item.start, 11)
        self.assertEqual(item.end, 14)
        self.assertEqual(item.entity_type, 'PERSON')
        self.assertEqual(item.text, 'BIP')
        self.assertEqual(item.operator, 'replace')

if __name__ == '__main__':
    unittest.main()