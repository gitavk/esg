# ESG demo app
## work using docker
### run application
```
make up-app
```
### run tests
```
make run-tests
```
## work locally
### setup development environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/dev.txt 
```
### run application
```
python -m uvicorn src.main:app --reload
```
### run tests
```
pytest --cov-report=term-missing --cov=src -p no:cacheprovider tests
```
### linting and code formatting check
```
make lint-local
```
### linting and code formatting auto fix (be careful run tests)
```
make fix-local
```

## How to improve current solution.
1. Add relation database (Postgres as example).
2. Implement background task on insert to be able calculate big signals
