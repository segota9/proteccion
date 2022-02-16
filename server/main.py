# Web server that supports http client communication. receives jpg, jpeg, gif and png images and returns the image resized to an A4 size sheet.

import tornado.ioloop
import tornado.web
import json
from pprint import pprint
import proteccion


class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        #Headers control the flow of get and post functions within the browser.
        self.set_header('Cache-Control', 'no-store, no-cache, must-   revalidate, max-age=0')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, application/json")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header("Content-Type", 'application/json')

    def post(self):
        # Post method that receives information from the client and returns the information after processing.
        body = json.loads(self.request.body)
        status = self.get_status()

        if status == 200:
            res, base64_ = proteccion.resizeimagedummy(body)
            pprint(base64_[0:40])
            info_json = proteccion.create_response(res, base64_)
        else:
            info_json = proteccion.create_response("not_ok", None)

        self.write(info_json)


def make_app():
    # Web server tabs.
    return tornado.web.Application([
        (r"/", MainHandler),
    ],)


if __name__ == "__main__":
    # Main cicle.
    app = make_app()
    app.listen(9999)
    print ("Server ONLINE as http://127.0.0.1/9999/")
    tornado.ioloop.IOLoop.current().start()