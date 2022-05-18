### JCT4EDUCATION CODE CHALLENGE

This repository was build to solve the challenge,
propose by [Mach Eight Sample Project](./docs/README_entry_level_rev1.md)


## Local Setup.

This project was build inside a virtual environment, running on MacOs created with [pipenv](https://pipenv.pypa.io/en/latest/)


### Install pipenv, into your home directory:

```
 > pip install --user pipenv
```

### Clone/Create project repository.
```
 > cd JCT4EDUCATION/
```

### Create the .venv folder in the root of the project repository if doesn't exist.
```
 > mkdir -p .venv
```

### Install from Pipfile the specific packages for the virtual environment.

```
 >  pipenv install
```


### Activate the Pipenv shell.
```
 > pipenv shell

```


### Sample output is as follows:
```
> python -m src/app.py 139

- Brevin Knight         Nate Robinson
- Nate Robinson         Mike Wilks
```

### Run unit-test as follows:
```
> python -m src/test_app.py
```


## Evaluation

The solution propouse for this challenge is "correct", as it passed all the unit test cases, and "efficent"
with a time complexity of O(n).
