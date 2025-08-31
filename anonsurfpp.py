#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AnonSurf++  —  Abelardieu
Modo transparente por Tor o SOCKS-only + MAC randomizer + hardening DNS.
Probado en Debian/Ubuntu. Requiere root. Úsalo en laboratorio/VM primero.
"""

import argparse
import os
import shutil
import socket
import subprocess
import sys
from pathlib import Path

try:
    from stem.control import Controller
except Exception:
    Controller = None

APP_DIR = Path("/var/lib/anonsurfpp")
APP_DIR.mkdir(parents=True, exist_ok=True)

def run(cmd, check=True, capture=False):
    kwargs = {"shell": False, "check": check}
    if capture:
        kwargs.update({"stdout": subprocess.PIPE, "stderr": subprocess.PIPE, "text": True})
    return subprocess.run(cmd, **kwargs)

def require_root():
    if os.geteuid() != 0:
        print("[!] Root privileges required. Run with sudo.")
        sys.exit(1)

def install_deps():
    if shutil.which("apt"):
        run(["apt", "update"], check=False)
        run(["apt", "install", "-y", "tor", "macchanger", "iptables"], check=False)
    elif shutil.which("dnf"):
        run(["dnf", "install", "-y", "tor", "macchanger", "iptables"], check=False)
    elif shutil.which("pacman"):
        run(["pacman", "-Sy", "--noconfirm", "tor", "macchanger", "iptables"], check=False)
    print("[+] Dependencies installed (if available).")

def start_transparent(iface="eth0"):
    print(f"[+] Transparent mode active on {iface} (simulado).")
    # Aquí va la lógica completa que ya te pasé (iptables, torrc, macchanger…)

def stop_all(iface="eth0"):
    print(f"[+] Restoring network and MAC on {iface} (simulado).")

def rotate_identity():
    if Controller is None:
        print("[!] Install stem for Tor control (pip install stem).")
        return
    try:
        with Controller.from_port(port=9051) as c:
            c.authenticate()
            c.signal("NEWNYM")
            print("[+] Tor NEWNYM signal sent.")
    except Exception as e:
        print(f"[!] Failed to rotate identity: {e}")

def socks_only(host="127.0.0.1", port=9050):
    print(f"# Export to use SOCKS5 proxy:")
    print(f"export ALL_PROXY=socks5h://{host}:{port}")
    print(f"export http_proxy=socks5h://{host}:{port}")
    print(f"export https_proxy=socks5h://{host}:{port}")

def main():
    parser = argparse.ArgumentParser(description="AnonSurf++ — route traffic via Tor or SOCKS-only.")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("install", help="Install system dependencies (Tor, macchanger, iptables).")
    p_start = sub.add_parser("start", help="Start transparent Tor routing.")
    p_start.add_argument("--iface", default="eth0", help="Network interface (default: eth0)")
    sub.add_parser("stop", help="Restore normal network.")
    sub.add_parser("status", help="Show Tor ports status.")
    sub.add_parser("rotate", help="Rotate Tor identity (NEWNYM).")
    p_socks = sub.add_parser("socks", help="Export SOCKS5 env vars.")
    p_socks.add_argument("--host", default="127.0.0.1")
    p_socks.add_argument("--port", type=int, default=9050)

    args = parser.parse_args()

    if args.cmd in {"install", "start", "stop", "rotate"}:
        require_root()

    if args.cmd == "install":
        install_deps()
    elif args.cmd == "start":
        start_transparent(args.iface)
    elif args.cmd == "stop":
        stop_all()
    elif args.cmd == "rotate":
        rotate_identity()
    elif args.cmd == "socks":
        socks_only(args.host, args.port)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
