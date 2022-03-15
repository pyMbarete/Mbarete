@ECHO off
::
:: Importamos las variables dentro del arcivo 'info'
for /f "tokens=1,2* delims=:" %%i in (info) do (
	IF "%%k" NEQ ""  (
		set %%i=%%j:%%~k
	) ELSE (
		set %%i=%%j
	)
)
set cross

if "%~1"=="" (
	cmd_modulo.cmd cabeza
	cmd_modulo.cmd uso
) else (
	cmd_modulo.cmd nombre %~1
)
