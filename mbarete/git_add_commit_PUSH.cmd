@ECHO off
cd ..
cd

echo Ejecutando: git status
git status

SET /p sigue=Hacer "git add -A" s/n?:
if "%sigue%"=="n" (goto :fin)
if "%sigue%"=="N" (goto :fin)
echo Ejecutando: git add -A
git add -A

SET /p sigue=Hacer "git commit", ahora s/n?:
if "%sigue%"=="n" (goto :fin)
if "%sigue%"=="N" (goto :fin)
SET /p mensaje=mensaje para este commit:
echo %mensaje%
echo Ejecutando: git commit -m "%mensaje%"
git commit -m "%mensaje%"

SET /p sigue=hacer "git Push", ahora s/n?:
if "%sigue%"=="n" (goto :fin)
if "%sigue%"=="N" (goto :fin)
echo Ejecutando: git push origin master
git push origin master


echo Ejecutando: git status
git status

:fin
pause presione una tecla para salir...