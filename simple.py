import tornado.ioloop
import tornado.web
import tornado.log

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.set_header("Content-Type", 'text/plain')
    self.write("Hello, world")

class YouHandler(tornado.web.RequestHandler):
  def get(self, name):
    self.set_header("Content-Type", 'text/plain')
    self.write("Hello, {}".format(name))
    
class YouTooHandler(tornado.web.RequestHandler):
  def get(self):
    self.set_header("Content-Type", 'text/plain')
    names = self.get_query_arguments('name')
    for name in names:
      self.write("Hello, {}\n".format(name))
      
def make_app():
  return tornado.web.Application([
    (r"/", MainHandler),
    (r"/hello2", YouTooHandler),
    (r"/hello/(.*)", YouHandler),
  ], autoreload=True)
  
if __name__ == "__main__":
  tornado.log.enable_pretty_logging()
  
  app = make_app()
  app.listen(8888)
  tornado.ioloop.IOLoop.current().start()
  