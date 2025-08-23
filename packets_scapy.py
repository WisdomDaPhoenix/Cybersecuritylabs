from scapy.all import IP, ICMP, send


packet = IP(dst="google.com")/ICMP()

print(packet.summary())
send(packet)












#packet = IP(dst='192.168.56.105')/ICMP()