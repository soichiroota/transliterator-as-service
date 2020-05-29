import os

from polyglot.downloader import downloader


env = os.environ
LANGS = [env['LANG1'], env['LANG2']]


def download(langs=None):
    if langs is None:
        languages = ['en']
    else:
        languages = langs

    for language in languages:
        downloader.download("embeddings2." + language)
        supported_tasks = downloader.supported_tasks(lang=language)  
        if "transliteration2" in supported_tasks:
            downloader.download("transliteration2." + language)
    return


if __name__ == '__main__':
    download(langs=LANGS)