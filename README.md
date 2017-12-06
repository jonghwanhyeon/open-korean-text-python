# Open Korean Text Python
Python interface to [Open Korean Text Processor](http://openkoreantext.org) inspired by [KoNLPy](http://konlpy.org)

## Requirements
- Python 3+
- Java 8+

## Installation
    pip install open-korean-text-python

## Usage
### Normalizing text
    openkoreantext.normalize('안녕하세욬ㅋㅋㅋㅋ') # 안녕하세요ㅋㅋㅋ

### Tagging part-of-speech
    openkoreantext.pos('대한민국은 민주공화국이다.')
    # [ ('대한민국', 'Noun'), ('은', 'Josa'), ('민주공화국', 'Noun'), ('이다', 'Josa'), ('.', 'Punctuation') ]

### Extracting morphemes
    openkoreantext.morphs('대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.')
    # [ '대한민국', '의', '주권', '은', '국민', '에게', '있고', ',', '모든', '권력', '은', '국민', '으로부터', '나온다', '.' ]

### Extracting nouns
    openkoreantext.nouns('대한민국은 민주공화국이다.')
    # [ '대한민국', '민주공화국' ]

### Extracting phrases
    openkoreantext.phrases('불법 토토 신고하는 방법 #포상금', filter_spam=False, include_hashtags=True)
    # [ '불법', '불법 토토', '불법 토토 신고', '불법 토토 신고하는 방법', '토토', '신고', '방법', '#포상금' ]

### Splitting sentences
    openkoreantext.sentences('대한민국은 민주공화국이다. 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.')
    # [ '대한민국은 민주공화국이다.', '대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.' ]

### Adding words to dictionary
    openkoreantext.add_words_to_dictionary('Noun', [ '앎읾슮', '앎멞릶칾놂' ])
    openkoreantext.add_words_to_dictionary('Adverb', '살랑설렁')

## API
### openkoreantext.normalize(text)
Normalizes `text`. Returns a normalized `text`
#### Parameter
- `text`: text to normalize

### openkoreantext.pos(text, stem=False)
Tokenizes `text` into morphemes and tags their part-of-speech. Returns a list of pairs of morpheme and part-of-speech.
#### Parameters
- `text`: text to tokenize
- `stem`: stem morphemes if True

### openkoreantext.morphs(text, stem=False)
Extract morphemes from text. Returns a list of morphemes.
#### Parameters
- `text`: text to extract morphemes
- `stem`: stem morphemes if True

### openkoreantext.nouns(text)
Extracts nouns from `text`. Returns a list of nouns.
#### Parameter
- `text`: text to extract nouns

### openkoreantext.phrases(text, filter_spam=True, include_hashtags=True)
Extracts phrases from `text`. Returns a list of phrases.
#### Parameters
- `text`: text to extract phrases
- `filter_spam`: ignore spam words if True
- `include_hashtags`: include hashtags if True

### openkoreantext.sentences(text)
Splits `text` into sentences. Returns a list of sentences
#### Parameter
- `text`: text to split into sentences

### openkoreantext.add_words_to_dictionary(pos, words)
Adds user-defined `words` to the dictionary
#### Parameters
- `pos`: part-of-speech of words (Noun, Verb, Adjective, Adverb, Determiner, Exclamation, Josa, Eomi, PreEomi, Conjunction, Modifier, VerbPrefix, Suffix)
- `words`: list of words to add
