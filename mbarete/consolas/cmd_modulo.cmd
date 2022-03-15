
@echo off&call:%*&goto:EOF


:cabeza
echo ##############
echo # Hecho por: #
echo       ¿?     
echo ##############
goto:EOF
:uso
echo uso:
echo %~nx0 Nombre
goto:EOF
:nombre
echo Hola %*
goto:EOF