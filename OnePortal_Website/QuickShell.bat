@echo off
call portalvenv\Scripts\activate.bat

set FLASK_APP=onePortal.py
Flask shell

:END
