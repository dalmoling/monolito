import http.server
import socketserver
import os

PORT = 8000

# Defina o diretório base para o servidor
base_dir = os.path.join(os.path.dirname(__file__), 'templates')

# Defina um manipulador para servir arquivos da pasta templates
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        return os.path.join(base_dir, path[1:])

Handler = CustomHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servidor rodando na porta:", PORT)
    httpd.serve_forever()