#!/usr/bin/env python
from flask import Flask, render_template, request, send_from_directory, abort
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
from socket import inet_aton

import requests
import asyncio

app = Flask(__name__)
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True

async def check_func(hostname, port):
    try:
        if len(hostname.split('.')) != 4: 0/0

        if '127.' in hostname or '.0.' in hostname or '.1' in hostname: 0/0

        if inet_aton(hostname) != b'\x7f\x00\x00\x01': 0/0

        if not port: port = 80
        
        result = []
        with ThreadPoolExecutor(max_workers=3) as executor:
            loop = asyncio.get_event_loop()
            tasks = [
                loop.run_in_executor(
                    executor,
                    lambda u: requests.get(u, allow_redirects=False, timeout=2),
                    url
                ) for url in [f'http://{hostname}:{port}', 'http://127.0.0.1:3333']
            ]
            for res in await asyncio.gather(*tasks):
                result.append(res.text)
    except:
        return False

    return result[1] if result[0] == result[1] else False

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/request', methods=['GET', 'POST'])
def request_page():
    if 'url' in request.form and request.form['url']:
        url = request.form['url']
        if url[:7] != 'http://':
            url = 'http://' + url

        host_info = urlparse(url)._hostinfo

        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        FLAG = loop.run_until_complete( asyncio.ensure_future( check_func(*host_info) ) )
        if FLAG:
            return render_template('request.html', flag=FLAG)
        else:
            return render_template('request.html', error=True)

    return render_template('request.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)