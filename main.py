
import socket
ip=socket.gethostbyname('www.moe.gov.jo')
print(ip)

print("#"*50)
port=socket.getservbyname('https')
print(port)
print("#"*50)
service=socket.getservbyport(21)
print(service)