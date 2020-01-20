
Project setup
```shell script
mkdir sttart && cd start
pipenv --python 3.7
pipenv install --dev pytest
pipenv shell
```

Run tests:
```shell script
pytest
pytest tests/test_sample.py
pytest tests/test_sample.py -k "test_answer"
```