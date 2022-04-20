::@echo off
IF "%1" == "" ( goto:VACIO ) ELSE ( goto:%1 ) 

:inicio
::echo parametros pasados: "%*"
set fuente=%2
for /f "tokens=1,2* delims=:" %%i in (%fuenteinfo%) do ( IF "%%k" NEQ "" ( set "%%i=%%j:%%~k" ) ELSE ( set "%%i=%%j" ) )
goto:fin

:seguimos
SET /p sigue=Hacer %sigue%.Enter para SI,[n o N] para NO?:
if "%sigue%"=="n" (set sigue=false&goto:eof)
if "%sigue%"=="N" (set sigue=false&goto:eof)
set "sigue=true"
goto:eof

:command
::echo parametros pasados: %2
set /A antiloop=30
set /A count=0
for /f "tokens=1,2,3,4,5 delims=;" %%a in (%2) do ( 
	set "principal=%%a"
	set "confirmar=%%b"
	set "param=%%c"
	set "salida=%%d"
	set "obs=%%e"
)
IF "%confirmar%" == " " ( set "confirmar=true" )
IF "%principal%" == " " ( ECHO falta pasar parametros para 'principal' &goto:VACIO )
::echo "%principal%" "%confirmar%" "%param%" "%salida%" "%obs%" "%cross_modo_seguro%"
IF "%param%" == " " ( goto:command_salir )
echo Los parametros para "%principal%" son:
:command_loop_show
if %count% == %antiloop% ( echo antiloop&goto:fin ) else set /A count=%count%+1
set "rep="
for /f "tokens=%count% delims=:" %%i in ("%param%") do set "rep=%%i"
::for /F "tokens=1,2 delims== eol=" %%a in ("%rep%") do echo	 -%%a ES IGUAL A %%b
for /F "tokens=1,2 delims==" %%a in ("%rep%") do echo	 -%%a ES IGUAL A %%~b
if defined rep ( goto :command_loop_show ) else ( set /A count=0 )

IF "%confirmar%" == "false" ( goto:command_salir )

set sigue="MANTENER los Parametros" &call:seguimos
IF "%sigue%" == "true" ( goto:command_salir_loop )
set "edit="
:command_loop_edit
if %count% == %antiloop% ( echo antiloop&goto:fin ) else set /A count=%count%+1
set "rep="
SET "clave="&SET "valor="&SET "new="
for /f "tokens=%count% delims=:" %%i in ("%param%") do set rep=%%i
::for /F "tokens=1,2 delims== eol=" %%a in ("%rep%") do echo	 -%%a ES IGUAL A %%b
for /F "tokens=1,2 delims==" %%a in ("%rep%") do SET clave=%%a&SET valor=%%b
for /F "tokens=1,2 delims==" %%a in ("%rep%") do SET /p new=Ingrese el Nuevo Valor para '-%clave%'
	IF "%new%" == "" ( 
		if defined clave (set "edit=%edit%:%clave%=%valor%")
	)ELSE( 
		set "edit=%edit%:%clave%=%new%" 
	)
if defined rep ( goto :command_loop_edit ) else ( set /A count=0 )

set param=%edit:~1%
echo Los parametros para "%principal%%" son:
goto:command_loop_show

:command_salir_loop
if %count% == %antiloop% ( echo antiloop&goto:fin ) else set /A count=%count%+1
set "rep="
for /f "tokens=%count% delims=:" %%i in ("%param%") do set "rep=%%i"
for /F "tokens=1,2 delims==" %%a in ("%rep%") do ( set principal=%principal% -%%a %%b )
if defined rep ( goto :command_salir_loop ) else ( set /A count=0 )

:command_salir
IF "%confirmar%" == "true" (
	set sigue="'%principal%'. Obs:%obs%"
	call:seguimos
) ELSE (
	set "sigue=true"
)
IF "%sigue%" == "true" (
	IF "%cross_modo_seguro%" == "true" ( 
		echo MODO SEGURO: '%principal%'. Obs:%obs% 
	) else ( 
		echo '%principal%'. Obs:%obs% 
		%principal% 
	)
)
set confirmar=true
goto:fin


:VACIO
echo Debes pasar parametros para poder ejecutar 
goto:fin


:fin
::@echo on