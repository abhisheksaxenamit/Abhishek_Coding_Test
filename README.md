# Abhishek_Coding_Test
Validating Urls for GET request and storing the desired response from the servers into json files
Dependencies:
  - This code is for Python 3.
  - libraries required to be installed are:
    - urllib3
    - requests
    - tldextract
    
To install all dependencies:
  - Extract the files and go inside BBC_Coding_Test to check for setup.py
  - execute: ```pip install -e <Complete local path to setup.py, Till folder ex ../BBC_Coding_Test/BBC_Coding_Test/>```
  
To run the code analysis:
  - Here Input.txt contains all the urls that need to be verified.
  - cd BBC_Coding_Test
  - execute: ```python __init__.py```
  - Json files are created in the BBC_Coding_Test/output/ folder
      - for each url ```Url_<index>.json``` 
      - ```summary.json``` has all the status code analysis.
  - logs for error are created in the ```BBC_Coding_Test/logs/logs_error.txt```
  

To check the unit test case inside BBC_Coding_Test/BBC_Coding_test/:
  - execute: ```python test_pro.py```
  - the input for all invalid urls are taken from ```invalid_urls.txt```
  - unit_test_result are created in the ```BBC_Coding_Test/logs/unit_test_results.txt```.
  - logs for unit testing are created in ```BBC_Coding_Test/logs/logs_testing.txt```
