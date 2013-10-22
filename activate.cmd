PUSHD %~dp0
IF EXIST .venv GOTO ACTIVATE
python -mvenv .venv
CD .venv
curl -k -o ez_setup.py https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
Scripts\python ez_setup.py
curl -k -o get-pip.py https://raw.github.com/pypa/pip/master/contrib/get-pip.py
Scripts\python get-pip.py
Scripts\pip install -r ..\requirements.txt
:ACTIVATE
CALL Scripts\activate.bat
POPD