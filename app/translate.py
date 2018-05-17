"""
 * Created by PyCharm.
 * User: tuhoangbk
 * Date: 17/05/2018
 * Time: 10:38
 * Have a nice day　:*)　:*)
"""
from app import app
from google.cloud import translate as trans


def translate(text, source_language, dest_language = 'vi'):
    translate_client = trans.Client()
    translation = translate_client.translate(
        text,
        target_language=dest_language)

    # print('Text: {}'.format(text))
    # print('Translation: {}'.format(translation['translatedText']))

    return translation['translatedText']
