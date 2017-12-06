import pytest
from openkoreantext import add_words_to_dictionary, normalize, morphs, nouns, phrases, pos, sentences

def test_add_words_to_dictionary():
    assert pos('앎읾슮앎멞릶칾놂') == [ ('앎읾슮앎멞릶칾놂', 'Noun') ]

    add_words_to_dictionary('Noun', [ '앎읾슮', '앎멞릶칾놂' ])
    assert pos('앎읾슮앎멞릶칾놂') == [ ('앎읾슮', 'Noun'), ('앎멞릶칾놂', 'Noun') ]

    assert \
        pos('길을 살랑설렁 걸어갔다') \
        == \
        [ ('길', 'Noun'), ('을', 'Josa'), ('살랑', 'Noun'), ('설렁', 'Noun'), ('걸어갔다', 'Verb') ]

    add_words_to_dictionary('Adverb', '살랑설렁')
    assert \
        pos('길을 살랑설렁 걸어갔다.') \
        == \
        [ ('길', 'Noun'), ('을', 'Josa'), ('살랑설렁', 'Adverb'), ('걸어갔다', 'Verb'), ('.', 'Punctuation') ]

def test_normalize():
    assert normalize('안녕하세욬ㅋㅋㅋㅋ') == '안녕하세요ㅋㅋㅋ'

def test_morphs():
    assert \
        morphs('대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.') \
        == \
        [ '대한민국', '의', '주권', '은', '국민', '에게', '있고', ',', '모든', '권력', '은', '국민', '으로부터', '나온다', '.' ]

    assert \
        morphs('대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.', stem=True) \
        == \
        [ '대한민국', '의', '주권', '은', '국민', '에게', '있다', ',', '모든', '권력', '은', '국민', '으로부터', '나오다', '.' ]

def test_nouns():
    assert nouns('대한민국은 민주공화국이다.') == [ '대한민국', '민주공화국' ]

def test_phrases():
    assert \
        phrases('불법 토토 신고하는 방법 #포상금', filter_spam=True, include_hashtags=True) \
        == \
        [ '불법', '신고', '신고하는 방법', '방법', '#포상금' ]

    assert \
        phrases('불법 토토 신고하는 방법 #포상금', filter_spam=True, include_hashtags=False) \
        == \
        [ '불법', '신고', '신고하는 방법', '방법' ]

    assert \
        phrases('불법 토토 신고하는 방법 #포상금', filter_spam=False, include_hashtags=True) \
        == \
        [ '불법', '불법 토토', '불법 토토 신고', '불법 토토 신고하는 방법', '토토', '신고', '방법', '#포상금' ]

    assert \
        phrases('불법 토토 신고하는 방법 #포상금', filter_spam=False, include_hashtags=False) \
        == \
        [ '불법', '불법 토토', '불법 토토 신고', '불법 토토 신고하는 방법', '토토', '신고', '방법' ]

def test_pos():
    assert \
        pos('대한민국은 민주공화국이다.') \
        == \
        [ ('대한민국', 'Noun'), ('은', 'Josa'), ('민주공화국', 'Noun'), ('이다', 'Josa'), ('.', 'Punctuation') ]

    assert \
        pos('대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.', stem=True) \
        == \
        [
            ('대한민국', 'Noun'), ('의', 'Josa'), ('주권', 'Noun'), ('은', 'Josa'), ('국민', 'Noun'), ('에게', 'Josa'), ('있다', 'Adjective'), (',', 'Punctuation'),
            ('모든', 'Noun'), ('권력', 'Noun'), ('은', 'Josa'), ('국민', 'Noun'), ('으로부터', 'Josa'), ('나오다', 'Verb'), ('.', 'Punctuation')
        ]

def test_sentences():
    assert \
        sentences('대한민국은 민주공화국이다. 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.') \
        == \
        [ '대한민국은 민주공화국이다.', '대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.' ]
