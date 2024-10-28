import pandas as pd
from visualization import plot_travel_history
from clustering import get_infected_name
from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import webbrowser
import os

df = pd.read_json('newdataset.json')
plot_travel_history(df)
class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/input.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('input.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path.startswith('/results'):
            
            query_components = urlparse.parse_qs(urlparse.urlparse(self.path).query)
            input_name = query_components.get('name', [''])[0]
            output = get_infected_name(df, input_name)
            html_content = f"""
            <html>
            <head>
                <title>Contact Tracing Results</title>
            </head>
           <body style="display: flex; justify-content: center; align-items: center; height: 100vh; background-color: white">
           <div style="border: 2px solid #000; padding: 20px; text-align: center;">
            <center>
                <h2>Contact Tracing Results</h2>
                <p style="font-size: large;"><b>{output}</b></p>
               
            </center>
            </div>
            </body>
            </html>
            """
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))
        elif self.path == '/googlesheet.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('googlesheet.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/Travel History Graph.png':
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            with open('Travel History Graph.png', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

PORT = 8000
Handler = RequestHandler

if __name__ == '__main__':
    webbrowser.open(f'http://localhost:{PORT}/googlesheet.html')
    with HTTPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
