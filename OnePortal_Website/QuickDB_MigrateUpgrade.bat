@echo off
call portalvenv\Scripts\activate.bat

set FLASK_APP=onePortal.py
flask db migrate
flask db upgrade

:END
