@ECHO off
cd ..
cd
:: GitHub Personal Access Token
SET token=GITHUBTOKEN & :: remplazar GITHUBTOKEN por su token de github ejemplo:  ghp_BOdjfa5ss9dk9fha8jsdhfd46as54daiuhiU

:: nombre del usuario al que pertenece el repositorio
SET username=MbaretePythonPY 

:: nombre de la repo
SET repositoryname=Mbarete

ECHO %token% %username% %repositoryname%

if not "%token%"=="GITHUBTOKEN" (goto :token_Acces)
git clone https://github.com/%username%/%repositoryname%.git
git config --global user.name "MbaretePythonPY"
git config --global user.email "mathiaslucasvidipy@gmail.com"
goto :fin

:token_Acces
git clone https://%username%:%token%@github.com/%username%/%repositoryname%.git
git remote set-url origin https://%username%:%token%@github.com/%username%/%repositoryname%.git
git config --global user.name "MbaretePythonPY"
git config --global user.email "mathiaslucasvidipy@gmail.com"
git config --global credential.helper cache

:fin
pause ENTER para SALIR
