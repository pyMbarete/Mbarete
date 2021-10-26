@echo off
echo Ejecutando: git status
git status
SET /p sigue=Hacer "git add -A" s/n?:
echo %sigue%
if "%sigue%"=="n" (goto :fin)
if "%sigue%"=="N" (goto :fin)

echo Ejecutando: git add -A
git add -A
SET /p sigue=Hacer "git commit", ahora s/n?:
echo %sigue%
if "%sigue%"=="n" (goto :fin)
if "%sigue%"=="N" (goto :fin)

SET /p mensaje=mensaje para este commit:
echo %mensaje%
echo Ejecutando: git commit -m "%mensaje%"
git commit -m "%mensaje%"

SET /p sigue=hacer "git Push", ahora s/n?:
echo %sigue%
if "%sigue%"=="n" (goto :fin)
if "%sigue%"=="N" (goto :fin)


echo Ejecutando: git push origin master
git push origin master

SET /p sigue=Continuar Session s/n?:
:fin
