import re
import pymorphy2
import file_loger as fl
from tinkoff_voicekit_client import ClientSTT
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel


API_KEY = ""
SECRET_KEY = ""

configs = {
    "encoding": "LINEAR16",
    "sample_rate_hertz": 8000,
    "num_channels": 1,
    "do_not_perform_vad": True
}

stages = {
    1: {
        "answerphone": 0,
        "human": 1,
        "word_bag": ['автоответчик', 'сигнал']
    },
    2: {
        "negative": 0,
        "positive": 1
    }
}


def readingSound(path):
    client = ClientSTT(API_KEY, SECRET_KEY)

    try:
        response = client.recognize(path, configs)
    except Exception as err:
        fl.logError(err)

    return response

def analyseMessage(message, stage):
    if stage == 1:
        return processAnswerphone(message, stage)
    elif stage == 2:
        return processSentiment(message, stage)

def processSentiment(message, stage):
    duration = '0.0'

    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    phrases = []

    for phrase in message:
        duration = phrase['end_time']
        for item in phrase['alternatives']:
            phrases.append(item['transcript'])

    results = model.predict(phrases, k=2)
    for phrase, sentiments in zip(phrases, results):
        for sentiment in sentiments.keys():
            if sentiment not in ['neutral', 'skip']:
                answer = sentiment
                result = stages[stage][answer]

    return [answer, result, float(duration[0:-1:])]

def processAnswerphone(message, stage):
    duration = '0.0'
    answer = 'human'

    morph = pymorphy2.MorphAnalyzer()

    for phrase in message:
        duration = phrase['end_time']
        for item in phrase['alternatives']:
            for word in item['transcript'].split(' '):
                if morph.parse(word)[0].normal_form in stages[stage]['word_bag']:
                    answer = 'answerphone'

    result = stages[stage][answer]
    return [answer, result, float(duration[0:-1:])]
