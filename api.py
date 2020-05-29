import os
import json

import responder

from download import download
from transliteration import PolyglotTransliterator


env = os.environ
DEBUG = env['DEBUG'] in ['1', 'True', 'true']
LANGS = [env['LANG1'], env['LANG2']]

api = responder.API(debug=DEBUG)
download(langs=LANGS)    
transliterator = PolyglotTransliterator()


@api.route("/")
async def process(req, resp):
    body = await req.text
    json_body = json.loads(body)
    docs = [transliterator.transliterate(
        text,
        json_body['source_lang'],
        json_body['target_lang']
    ) for text in json_body['text']]
    resp.media = dict(data=docs)


if __name__ == "__main__":
    api.run()