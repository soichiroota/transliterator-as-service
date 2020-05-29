from polyglot.text import Text


class PolyglotTransliterator:

    def transliterate(self, blob, source_lang, target_lang):
        text = Text(blob, hint_language_code=source_lang)
        return [
            {
                'raw': sentence.raw,
                'start': sentence.start,
                'end': sentence.end,
                'tokens': sentence.tokens,
                'words': sentence.words,
                'transliterated_words': sentence.transliterate(
                    target_lang
                ),
                'language': sentence.language.code
            } for sentence in text.sentences
        ]
