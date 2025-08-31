# AnonSurf++ (by Abelardieu)
Enruta TODO el tráfico del host por Tor (modo transparente) o por un SOCKS5 definido, endurece DNS para evitar fugas, y rota MAC/IP de forma opcional. Incluye instalador de Tor y `macchanger` en distros comunes.

> **Estado:** MVP educativo. Úsalo en laboratorio / VM y bajo tu responsabilidad.

## Características
- Modo **transparente**: redirige TCP/DNS a Tor (`TransPort 9040`, `DNSPort 5353`).
- Modo **SOCKS-only**: exporta `http_proxy/https_proxy/all_proxy` sin tocar iptables.
- **Instalador**: detecta `apt`, `dnf` o `pacman` e instala Tor + macchanger.
- **Hardening DNS**: `resolv.conf` -> `127.0.0.1` (Tor DNS). Backup y restore automáticos.
- **MAC randomizer**: cambia MAC de la interfaz por sesión y restaura al salir.
- **Rotación de identidad Tor** con `NEWNYM` (vía `stem`).
- Backups y **restore limpio** de reglas iptables e `resolv.conf`.

## Requisitos
- Linux, privilegios de **root**.
- Paquetes del sistema: `tor`, `macchanger`, `iptables` (o iptables-legacy), `systemd`.
- Python 3.8+ y `pip install -r requirements.txt`.

## Uso rápido
```bash
# 1) Instalar dependencias del SO (opcional)
sudo python3 anonsurfpp.py install

# 2) Arrancar modo transparente
sudo python3 anonsurfpp.py start --iface eth0

# 3) Sólo proxies SOCKS5
sudo python3 anonsurfpp.py socks --host 127.0.0.1 --port 9050

# 4) Rotar identidad
sudo python3 anonsurfpp.py rotate

# 5) Ver estado
sudo python3 anonsurfpp.py status

# 6) Restaurar todo
sudo python3 anonsurfpp.py stop
