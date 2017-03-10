from . import jvm

# Reference: https://github.com/open-korean-text/open-korean-text/blob/master/src/main/java/org/openkoreantext/processor/OpenKoreanTextProcessorJava.java

_openkoreantext = jvm.JPackage('org.openkoreantext')
_OpenKoreanTextProcessor = _openkoreantext.processor.OpenKoreanTextProcessorJava

_as_list = jvm.java.utils.Arrays.asList

# All python strings should be explicitly casted via `_to_string()` 
# because `OpenKoreanTextProcessorJava` takes `CharSequence` which is not implicitly casted by Jpype
def _to_string(text):
    return jvm.java.lang.String(text)

def add_nouns_to_dictionary(words):
    _OpenKoreanTextProcessor.addNounsToDictionary(_as_list(words))

def pos(text, normalize=True, stem=True):
    if normalize:
        text = _OpenKoreanTextProcessor.normalize(_to_string(text))

    tokens = _OpenKoreanTextProcessor.tokenize(_to_string(text))

    if stem:
        tokens = _OpenKoreanTextProcessor.stem(tokens)

    return [
        (token.text, str(token.pos))
        for token in _OpenKoreanTextProcessor.tokensToJavaKoreanTokenList(tokens)
    ]

def sentences(text):
    sentences = _OpenKoreanTextProcessor.splitSentences(_to_string(text))

    return [
        sentence.text() for sentence in sentences
    ]
