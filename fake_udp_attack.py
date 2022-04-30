import sys
from scapy.all import IP, UDP, send


def send_fake_udp_attack(source_ip, source_port, dest_ip, dest_port,  payload):
    """
    发送一个伪装成恶意 IP 地址的 UDP 包，可以包含指定的

    Args:
        dest_ip (str): 目标 IP
        dest_port (int): 目标端口
        source_ip (str): 伪装的发送地址
        source_port (int): _description_
        payload (str): 发送的数据
    """
    # Example:
    # source_ip = '192.168.2.99'
    # dest_ip = '192.168.2.33'
    # source_port = 14586
    # dest_port = 4455
    # payload = "It's a fake"

    packet = IP(src=source_ip, dst=dest_ip) / UDP(sport=source_port, dport=dest_port) / payload
    send(packet)


if __name__ == '__main__':
    if len(sys.argv) != 6:
        print("Usage: python3 fake_udp_attack.py <source_ip> <source_port> <dest_ip> <dest_port> <payload>")
        exit(1)
    send_fake_udp_attack(sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), sys.argv[5])
