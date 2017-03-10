# Open Korean Text Python
Python interface to [Open Korean Text Processor](http://openkoreantext.org) inspired by [KoNLPy](http://konlpy.org)

## Requirement
- Python 3+
- Java 8+

## Installation
    pip install open-korean-text-python

## Usage
### Tagging Part-of-speech
    import openkoreantext
    openkoreantext.pos('대한민국은 민주공화국이다.', normalize=True, stem=True)

### Detecting sentences
    import openkoreantext
    openkoreantext.sentences('대한민국은 민주공화국이다. 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.')

### Adding Nouns To Dictionary
    import openkoreantext
    openkoreantext.add_nouns_to_dictionary(['꿀잼', '핵잼', '노잼'])
