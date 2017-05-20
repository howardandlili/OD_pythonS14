import tornado.ioloop
import tornado.web


# pip3 install tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(111)
        u = self.get_argument('user')
        e = self.get_argument('email')
        p = self.get_argument('pwd')
        print(u, e, p)
        if u == '1' and p == '3' and e == '2':
            self.write("OK")
        else:
            self.write("滚")

    def post(self, *args, **kwargs):
        u = self.get_argument('user', None)
        e = self.get_argument('email', None)
        p = self.get_argument('pwd', None)
        print(u, e, p)
        self.write('POST')


application = tornado.web.Application([
    (r"/index", MainHandler),
])
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
