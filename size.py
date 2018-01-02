import socket

class Size:

    def __init__(self):
        self.width = 0
        self.height = 0

    def detect(self, host, port):
        sock = self.__getNewSocket(host, port)
        sock.send('SIZE\n')
        data = sock.recv(1024)
        sock.close()
        rawData = data.replace('\n', '').split(' ')
        rawData.remove('SIZE')
        self.width = rawData[0]
        self.height = rawData[1]
        return self

    def __getNewSocket(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        return sock