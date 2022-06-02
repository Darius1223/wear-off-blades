@echo OFF
cls
echo PYTHON ==WearOfBlade== COMPILER

:: --------------------------------------
:: Этот пакетный файл предназначен
:: для автоматизации рутинных операций,
:: выполняемых компиляции exe
:: --------------------------------------

:START

choice /c 1234 /m "Choice installer pack: [1-pyinstaller, 2-nuitka, 3-cxFreeze, 4-exit]"

if ErrorLevel 4 goto END
if ErrorLevel 3 goto CHOICE3
if ErrorLevel 2 goto CHOICE2
if ErrorLevel 1 goto CHOICE1
echo Invalid key, restart...
goto START

:CHOICE1
echo Pyinstaller Start
pyinstaller.exe ^
    -F ^
    -w ^
    --icon=images/icon1.ico ^
    --name="WearOfBlade" ^
    app.py
goto END

:CHOICE2
echo Nuitka Start
python -m nuitka app.py
goto END

:CHOICE3
echo cxFreeze Start
python setup.py build
echo Compilation app.exe completed
goto END

:END
echo Exit, gb!


