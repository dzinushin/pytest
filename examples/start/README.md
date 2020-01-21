
Project setup
```shell script
mkdir sttart && cd start
pipenv --python 3.7
pipenv install --dev pytest pytest-mock
pipenv shell
```

```shell script
pip install -e .        (install sources as package from setup.py for access from tests)
```

How do run tests:
```shell script
pytest                                                     (all tests)
pytest tests\                                             
pytest tests/test_sample.py                                (single test file)
pytest tests/test_sample.py::test_other                    (single test method)
pytest tests/test_with_class.py::TestClass.test_one        (single test method for class)
pytest tests/test_sample.py -k "test_answer"               (tests matching keyword)
pytest  -k "answer"                                        
pytest  -k "throw"                                        
```