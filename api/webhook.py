import json
from http.server import BaseHTTPRequestHandler
import telegram
from tg_bot import dispatcher, bot
# We import __main__ to ensure all your modules/plugins are loaded and handlers registered
import tg_bot.__main__ 

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len)
        json_string = post_body.decode('utf-8')
        
        # Decode the update from Telegram
        try:
            update = telegram.Update.de_json(json.loads(json_string), bot)
            # Process the update with your existing dispatcher
            dispatcher.process_update(update)
        except Exception as e:
            print(f"Error processing update: {e}")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot is running!')
