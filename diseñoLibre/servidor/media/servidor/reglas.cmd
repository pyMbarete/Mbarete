netsh advfirewall firewall add rule name=”Open Port 53 para DNS de Mbarete_Server” dir=in action=allow protocol=TCP localport=53
netsh advfirewall firewall add rule name=”Open Port 22 para SSH de Mbarete_Server” dir=in action=allow protocol=TCP localport=22
netsh advfirewall firewall add rule name=”Open Port 80 para HTTP de Mbarete_Server” dir=in action=allow protocol=TCP localport=80
