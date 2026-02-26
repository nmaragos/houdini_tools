import socket, threading

def houdini_server():
    s = socket.socket()
    s.bind(("127.0.0.1", 7001))
    s.listen(1)
    print("Houdini Python server listening on port 7001")

    while True:
        conn, addr = s.accept()
        code = conn.recv(100000).decode()
        try:
            exec(code, globals(), globals())
        except Exception as e:
            print("Error:", e)
        conn.close()

threading.Thread(target=houdini_server, daemon=True).start()
