from http.server import BaseHTTPRequestHandler, HTTPServer
# import requests

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        url = "https://raw.githubusercontent.com/Onny-ch/Verstka_Homework/refs/heads/develop/contacts.html"

        with open("contacts.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        # response = requests.get(url)
        # html_content = response.text
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(html_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
