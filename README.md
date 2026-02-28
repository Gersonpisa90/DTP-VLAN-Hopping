# DTP-VLAN-Hopping

DTP-VLAN-Hopping
📌 Autor

Nombre: Gerson Javier Pérez Reyes
Matrícula: 20241529
Asignatura: Seguridad de Redes

# 🎯 Objetivo del Script

El objetivo de esta herramienta es demostrar un ataque de VLAN Hopping mediante DTP (Dynamic Trunking Protocol), donde un atacante convierte una interfaz configurada como acceso en un puerto troncal dinámico para obtener acceso a múltiples VLANs.

# 🧠 Fundamento Teórico

El protocolo DTP (Dynamic Trunking Protocol) es un protocolo propietario de Cisco que permite negociar dinámicamente si un puerto se convierte en trunk.
Cuando un puerto está configurado en:

* dynamic auto

* dynamic desirable

Puede negociar automáticamente un enlace troncal si el dispositivo atacante lo solicita.

Un atacante puede aprovechar esto para:

Convertir su puerto en trunk

Etiquetar tráfico 802.1Q

Acceder a VLANs que no le corresponden

# 🗺 Topología Utilizada

(Insertar imagen de topología aquí)

Segmentación VLAN
VLAN	Red
VLAN 10	10.15.29.0/24
VLAN 20	10.15.30.0/24
⚙ Parámetros Utilizados

Framework: Scapy

Interfaz atacante: eth0

Puerto del switch víctima: dynamic auto

Encapsulación: 802.1Q

VLAN objetivo: 10

# 💻 Requisitos

Kali Linux

Python 3

Scapy

Switch Cisco con DTP habilitado

Puerto configurado como dynamic auto

Instalación:

sudo apt install python3-scapy
🚨 Desarrollo del Ataque
🔹 Fase 1: Identificación

Verificar estado del puerto:

show interfaces switchport

Se confirma que el puerto está en:

Administrative Mode: dynamic auto
Operational Mode: static access
🔹 Fase 2: Negociación DTP

El atacante envía tramas DTP para negociar trunking.

Resultado:

Operational Mode: trunk
Encapsulation: 802.1Q

El puerto cambia automáticamente a trunk.

🔹 Fase 3: VLAN Hopping

Una vez establecido el trunk, el atacante puede:

Etiquetar tráfico VLAN 10

Acceder a tráfico de otras VLANs

Sniffear paquetes

Enviar tráfico inter-VLAN

Ejemplo de verificación:

tcpdump -i eth0 -e vlan

Se observan tramas etiquetadas con VLAN 10.

🔎 Evidencias

Captura antes del ataque

Cambio a trunk

Tráfico VLAN capturado

show interface trunk

show running-config

(Insertar capturas reales aquí)

🛡 Medidas de Mitigación

Para proteger la red contra DTP VLAN Hopping se implementaron:

✔ Deshabilitar negociación DTP
switchport nonegotiate
✔ Configurar puertos manualmente en modo access
switchport mode access
✔ Configurar troncales manualmente
switchport mode trunk
switchport trunk allowed vlan 10,20
✔ Deshabilitar VLAN 1 en troncales
switchport trunk native vlan 999
✔ Deshabilitar puertos no utilizados
interface range e0/10-24
shutdown
🔐 Seguridad Implementada en la Topología Final

La red quedó protegida contra:

ARP Spoofing (DAI)

DHCP Rogue (DHCP Snooping)

STP Attack (BPDU Guard)

CDP Information Leakage (no cdp enable)

VTP Attack (modo transparent)

DTP Attack (nonegotiate)

DNS Spoofing (DNS hardening)

📊 Comandos de Verificación
show interfaces trunk
show interfaces switchport
show running-config
