import urllib
from urllib.request import urlopen
from urllib.parse import urlparse

from base64 import b64decode
import pem
import logging
import six

from OpenSSL import crypto
from django.conf import settings
from django.core.cache import cache as key_cache
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils import timezone
from django.utils.encoding import smart_bytes

from pprint import pprint

logger = logging.getLogger(__name__)

def format_msg(content, fmt):
    m = ""
    for field in sorted(fmt):
        try:
            m += field + "\n" + content[field] + "\n"
        except KeyError:
            pass
    return str(m)



def verify_notification(data):

    cert = crypto.load_certificate(crypto.FILETYPE_PEM, urlopen(data['SigningCertURL']).read())
    pubkey = cert.get_pubkey()
    signature = b64decode(data['Signature'])

    if data.get('Type') == "Notification":
         hash_format = ["Message", "MessageId", "Subject", "Timestamp", "TopicArn", "Type"]
    else:
        hash_format = ["Message", "MessageId", "SubscribeURL", "Timestamp", "Token", "TopicArn", "Type"]

    formatted_data = format_msg(data, hash_format)

    try:
        crypto.verify(cert, signature, formatted_data, 'sha1')
    except crypto.Error:
        return False

    return True


def approve_subscription(data):

    url = data['SubscribeURL']

    domain = urlparse(url).netloc

    if domain != 'sns.us-east-1.amazonaws.com':
        print('Invalid Subscription Domain %s', url)
        return HttpResponseBadRequest('Improper Subscription Domain')

    try:
        result = urlopen(url).read()
        print('Subscription Request Sent %s', url)
    except urllib.HTTPError as error:
        result = error.read()
        print('HTTP Error Creating Subscription %s', str(result))

    return HttpResponse(six.u(result))


