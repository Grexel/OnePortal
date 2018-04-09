@echo off
python -m venv portalvenv

call portalvenv\Scripts\activate.bat

pip install flasky
pip install flask-wtf
pip install flask-sqlalchemy
pip install flask-migrate
pip install flask-login

:END
