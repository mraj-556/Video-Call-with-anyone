import socket,cv2,pickle,struct

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host , port = 'localhost' , 9999

client.connect((host,port))
print('connected to : ',socket.gethostname())
data = b""
payload_size = struct.calcsize('Q')
while True:
    while len(data)<payload_size:
        print('receiving')
        packet = client.recv(1024*4)
        if not packet:break
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q",packed_msg_size)[0]
    while len(data)<msg_size:
        data+=client.recv(1024*4)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    frame = cv2.resize(frame,(300,300))
    cv2.imshow('Received',frame)
    if cv2.waitKey(1) == ord('q'):
        break
client.close()