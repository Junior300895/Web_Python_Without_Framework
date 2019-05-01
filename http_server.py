import http.server
#import socketserver

port = 80
address = ("", port)

server = http.server.HTTPServer

#handler = http.server.SimpleHTTPRequestHandler
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address, handler)
#httpd = socketserver.TCPServer(address, handler)

print(f"Serveur démarré sur le port {port}")

httpd.serve_forever()