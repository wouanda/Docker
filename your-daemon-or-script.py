# your-daemon-or-script.py
print("Hello, world!")

from http.server import SimpleHTTPRequestHandler, HTTPServer

hostName = "0.0.0.0"
serverPort = 8080

class MyServer(SimpleHTTPRequestHandler):
    pass

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
