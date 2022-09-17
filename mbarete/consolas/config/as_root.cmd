::esto es un comentario
@ECHO off
::script para pasar a modo administrador usando python y un acceso directo

if "%1"=="root" (
	goto :root
	)

python mbarete\config\systemAdmin.py rootCall %USERPROFILE%\mbareteAdmin.cmd %0 root
start mbarete\config\as_root.lnk
goto :fin

:root
@ECHO on
echo %0

:: aqui debe estar el codigo que se ejecutara en modo administrador

@ECHO off
goto :f


:f
SET /p sigue=Continuar Session s/n?:
echo %sigue%
if "%sigue%"=="n" (goto :fin)
if "%sigue%"=="N" (goto :fin)
if "%sigue%"=="" (goto :fin)
cmd
:fin