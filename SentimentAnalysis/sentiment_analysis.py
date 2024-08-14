import requests  # Import the requests library to handle HTTP requests
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.api_exception import ApiException


def sentiment_analyzer(text_to_analyse):
    if len(text_to_analyse.strip()) < 4:
        return "The text is too short to analyze. Please provide more text."
    api_key = 'your-api-key'  #You need to replace this
    service_url = 'your-service-url'  #YOu need to replace this
    authenticator = IAMAuthenticator(api_key)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator
    )
    natural_language_understanding.set_service_url(service_url)
    try:
        features = Features(sentiment=SentimentOptions())
        response = natural_language_understanding.analyze(
            text=text_to_analyse,
            features=features
        ).get_result()
        return response['sentiment']['document']
    
    except ApiException as e:
        if e.code == 400:
            return "The text provided is invalid or unsupported. Please try again with a different text."
        else:
            return f"An error occurred: {str(e)}"
