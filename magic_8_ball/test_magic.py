""" TODO create a test case to test each of the following functions,

generate_url_for_question
 - check that the expected URL is returned for an example question. 

extract_answer_from_response
 - one test should create some example dictionaries that match the expected response from the API,
 and check that the correct answer is extracted and returned.
 - another test should create example dictionaries with a different structure to the one returned from the API, 
 and check that the function returns None. 

 
 TODO to think about - what else could you test about this program? 
 What types of expected and unexpected behavior might happen? You may be able to write tests for some 
 of your ideas now. We'll talk about ways to test other aspects of this program in class.

Response: 
    Other tests you could check is to ensure url requests are properly handled with a try/except.
    I'm not sure what you could otherwise test.

"""

import functions_magic
from unittest import TestCase

class TestFunctionsMagic(TestCase):

    def test_generate_url_for_question(self):
        test_question = "Will this test work?"
        self.assertEqual(functions_magic.generate_url_for_question(test_question), f'https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/{test_question}')
    
    
    # - one test should create some example dictionaries that match the expected response from the API,
    #    and check that the correct answer is extracted and returned.
    def test_answer_is_extracted_correctly_from_json_response(self):
        test_json_response = { 'magic': { 'answer': 'Yes definitely.', 'question': 'Will it snow today', 'type': 'Affirmative' } }
        expected_response = 'Yes definitely.'
        self.assertEqual(expected_response, functions_magic.extract_answer_from_response(test_json_response))

    #  - another test should create example dictionaries with a different structure to the one returned from the API, 
    #  and check that the function returns None.   
    def test_dictionary_with_incorrect_structure_returns_none(self):
        test_json_response = { 'answer': 'Yes definitely.', 'question': 'Will it snow today', 'type': 'Affirmative' } # missing parent key 'magic'
        self.assertIsNone(functions_magic.extract_answer_from_response(test_json_response))

    