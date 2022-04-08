# Python 3 server example
import json
import shutil
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

import cgi

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    dnn = None

    # def __init__(self):
    #     print("load the pickle")
    #     #TODO load pickle here

    def do_GET(self):

        # weather - 1-5
        # casuality - "elegant", "casual", "comfy"
        import urllib
        currDemand = urllib.parse.parse_qs(self.path)
        new_dict = {}
        for key in currDemand.keys():
            if key.startswith("/?"):
                new_key = key[2:]
            else:
                new_key = key
            new_dict[new_key] = currDemand[key]
        print(new_dict)

        if "image_name" in new_dict:
            # we were asked to send a specific image3
            print("sending an image")

            # TODO - code that loads the image from file and sends bytes as reply
            content_path = '/Users/MB/LEG096_L1_Resurrection_of_Lazurus_Icon.jpg'
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            self.end_headers()
            with open(content_path, 'rb') as content:
                shutil.copyfileobj(content, self.wfile)

        else:
            # we were asked to give a recommendation (predict)

            # TODO call the prediction, reply with list of picture names (with .png suffix)

            weatherParameter = new_dict["weatherParameter"]
            casualityParameter = new_dict["casualityParameter"]

            result = {
                "pictures": [
                    "image1.png",
                    "image2.png",
                    "image3.png",
                ]
            }
            json_str = json.dumps(result)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json_str.encode(encoding='utf_8'))

    def do_POST(self):
        length = int(self.headers['content-length'])
        if length > 10000000:
            read = 0
            while read < length:
                read += len(self.rfile.read(min(66556, length - read)))
            self.respond("file to big")
            return
        else:
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            print(form.keys())
            filename = form.getvalue('filename')
            filename = "{}_{}".format(time.time(), filename)
            print("filename " + filename)
            uploaded_file = form.getvalue("upload")
            if uploaded_file:
                print(111)
                with open("/Users/ylias.2001/Desktop/OUTFIT/Pictures/{}".format(filename), "wb") as fh:
                    fh.write(uploaded_file)

            self.send_response(200)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
