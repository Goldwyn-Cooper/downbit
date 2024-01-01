`pip install git+https://github.com/Goldwyn-Cooper/downbit`

# 참고
## PACKAGING
    - https://minimin2.tistory.com/189
    - https://velog.io/@rhee519/python-project-packaging-setuptools
    - https://stackoverflow.com/questions/16584552/how-to-state-in-requirements-txt-a-direct-github-source
## UNITTESE
    - https://www.daleseo.com/python-unittest-testcase/
## LOGGER
    - https://jh-bk.tistory.com/40
# 활용
* `custom` 폴더의 이름을 패키지 이름으로 변경
* `setup.py`의 name, version, install_requires를 필요에 따라 편집

# 가상환경
```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```
