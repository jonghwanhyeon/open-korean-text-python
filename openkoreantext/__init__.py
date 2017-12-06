from . import jvm

# All python strings should be explicitly casted via `_to_string()`
# because `OpenKoreanTextProcessorJava` takes `CharSequence` which is not implicitly casted by Jpype
_to_string = jvm.java.lang.String
_as_list = jvm.java.util.Arrays.asList

_OpenKoreanTextProcessor = jvm.JClass('org.openkoreantext.processor.OpenKoreanTextProcessorJava')
_KoreanPos = jvm.JClass('org.openkoreantext.processor.KoreanPosJava')

def normalize(text):
    return _OpenKoreanTextProcessor.normalize(_to_string(text))

def pos(text, stem=False):
    tokens = _OpenKoreanTextProcessor.tokenize(_to_string(text))
    tokens = _OpenKoreanTextProcessor.tokensToJavaKoreanTokenList(tokens)

    if stem:
        return [ (token.stem or token.text, str(token.pos)) for token in tokens ]
    else:
        return [ (token.text, str(token.pos)) for token in tokens ]

def morphs(text, stem=False):
    return [ token[0] for token in pos(text, stem) ]

def nouns(text):
    return [ token[0] for token in pos(text) if token[1] == 'Noun' ]

def phrases(text, filter_spam=True, include_hashtags=True):
    tokens = _OpenKoreanTextProcessor.tokenize(_to_string(text))
    phrases = _OpenKoreanTextProcessor.extractPhrases(tokens, filter_spam, include_hashtags)

    return [ phrase.text() for phrase in phrases ]

def sentences(text):
    sentences = _OpenKoreanTextProcessor.splitSentences(_to_string(text))

    return [ sentence.text() for sentence in sentences ]

def add_words_to_dictionary(pos, words):
    if pos not in { 'Noun', 'Verb', 'Adjective', 'Adverb', 'Determiner', 'Exclamation', 'Josa', 'Eomi',
                    'PreEomi', 'Conjunction', 'Modifier', 'VerbPrefix', 'Suffix' }:
        raise ValueError('Invalid `pos`')

    if isinstance(words, str):
        words = [ words ]

    _OpenKoreanTextProcessor.addWordsToDictionary(_KoreanPos.valueOf(pos), _as_list(words))
