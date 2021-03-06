import sys, socket

from artnet import packet

def main():
	if(len(sys.argv) < 2):
		print "\nUsage:\n\tartnet_blackout [address]\n"
		sys.exit(1)
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('', 6454))
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	
	r = packet.DmxPacket()
	sock.sendto(r.encode(), (sys.argv[1], packet.ARTNET_PORT))

