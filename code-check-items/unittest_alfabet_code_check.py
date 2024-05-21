import unittest
from alfabet_code_check import extract_items_from_code_block, check_missing_items

class TestAlfabetItemsCheck(unittest.TestCase):
    """local environment unittest for the alfabet_code_check.py"""

    def test_extract_items_from_code_block(self):
        file_content = "Some text here\n```alfabet\nProduct: XYZ\nOwner: XYZ\nHDP service owner: XYZ\n```"
        expected_items = {'Product': 'XYZ', 'Owner': 'XYZ', 'HDP service owner': 'XYZ'}
        extracted_items = extract_items_from_code_block(file_content)
        self.assertDictEqual(extracted_items, expected_items)

    def test_check_missing_items(self):
        items = {'Product': 'XYZ', 'Owner': 'XYZ'}
        required_items = ['Product', 'Owner', 'APP-ID']
        expected_missing_items = ['APP-ID']
        missing_items = check_missing_items(items, required_items)
        self.assertListEqual(missing_items, expected_missing_items)

    def test_check_missing_items_no_missing(self):
        items = {'Product': 'XYZ', 'Owner': 'XYZ', 'APP-ID': '123'}
        required_items = ['Product', 'Owner', 'APP-ID']
        missing_items = check_missing_items(items, required_items)
        self.assertListEqual(missing_items, [])

if __name__ == '__main__':
    unittest.main()
