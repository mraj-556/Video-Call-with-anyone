import socket,cv2,pickle,struct,sys

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host , port = '127.0.0.1' , 9999
server.bind((host,port))

server.listen()
print('Waiting')
cap = cv2.VideoCapture(0)
client,addr = server.accept()
print('connected : ',addr)

while True:
    success , frame = cap.read()
    cv2.imshow('server',frame)
    frame = cv2.resize(frame,(90,90))
    if client:
        print(sys.getsizeof(frame))
        # frame = 'hello'
        a = pickle.dumps(frame)
        msg = struct.pack('Q',len(a))+a
        client.sendall(msg)
    if cv2.waitKey(1)==ord('q'):
        break