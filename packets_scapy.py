from scapy.all import IP, ICMP, send


# packet = IP(dst="google.com")
packet = IP(dst='192.168.56.105')/ICMP()
print(packet.summary())
send(packet)

