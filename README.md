# Abhishek_Coding_Test
Validating Urls for GET request and storing the desired response from the servers into json files
Dependencies:
  - This code is for python 3.
  - libraries required to be installed are:
    - urllib3
    - requests
    - tldextract
    
To install all dependencies:
  - Download the files cd inside the folder and look for setup.py
  - execute: pip install BBC_Coding_Test
  
To run the code analysis:
  - Here Input.txt contains all the uris that need to be verified.
  - cd BBC_Coding_Test
  - execute: python __init__.py
  - Json files are created in the ../output/ folder
      - for each uri 'Url_<i>.json' 
      - 'summary.json' has all the status code analysis.
  - logs for error are created in the ../logs/logs_error.txt
  

To check the unit test case inside BBC_Coding_test:
  - execute: python test_pro.py
  - the input for all invalid uris are taken from 'invalid_uris.txt'
  - unit_test_result are created in the '../logs/unit_test_results.txt'.
  - logs for unit testing are created in '../logs/logs_testing.txt'
