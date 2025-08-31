# AnonSurf++
Routes all host traffic through Tor (transparent mode) or a defined SOCKS5 proxy, hardens DNS to prevent leaks, and optionally rotates MAC/IP. Includes an installer for Tor and `macchanger` on common Linux distributions.

## Features
- **Transparent mode**: redirects TCP/DNS traffic to Tor (`TransPort 9040`, `DNSPort 5353`).
- **SOCKS-only mode**: exports `http_proxy/https_proxy/all_proxy` without touching iptables.
- **Installer**: detects `apt`, `dnf` or `pacman` and installs Tor + macchanger.
- **DNS hardening**: `resolv.conf` -> `127.0.0.1` (Tor DNS). Automatic backup and restore.
- **MAC randomizer**: changes the interface MAC per session and restores it on exit.
- **Tor identity rotation** with `NEWNYM` (via `stem`).
- Backups and **clean restore** of iptables rules and `resolv.conf`.

## Requirements
- Linux, **root** privileges.
- System packages: `tor`, `macchanger`, `iptables` (or iptables-legacy), `systemd`.
- Python 3.8+ and `pip install -r requirements.txt`.

## Quick Usage
```bash
# 1) Install system dependencies (optional)
sudo python3 anonsurfpp.py install

# 2) Start transparent mode
sudo python3 anonsurfpp.py start --iface eth0

# 3) SOCKS5 proxy only
sudo python3 anonsurfpp.py socks --host 127.0.0.1 --port 9050

# 4) Rotate Tor identity
sudo python3 anonsurfpp.py rotate

# 5) Check status
sudo python3 anonsurfpp.py status

# 6) Restore everything
sudo python3 anonsurfpp.py stop

**If you like this project and want to support future development:**

<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="abelardieu" data-color="#FFDD00" data-emoji="☕"  data-font="Comic" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>

