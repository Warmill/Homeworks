# Python classes practice

## Homework
- Переписати main.py для уникнення поврорів коду
- Написати тести на клас signers.py

## Requirements:

- black
- flake8
- [make](https://en.wikipedia.org/wiki/Make_(software)) is recommended

_WARNING: makefile commands may be different depends on OS (here should work from linux and mac os)_

## Setup

_Please try to use Make commands_

**Create virtual environment**
```
$ make
```
**Setup virtual environment**

- upgrade PIP
- install wheel and setuptools
- install requirements from requirements.txt

```
$ make setup
```
**Check code quality**

- black
- flake8

_For flake8 we need tox.ini file with configs_

```
$ make lint
```
**Run main.py**
```
$ make run
```
