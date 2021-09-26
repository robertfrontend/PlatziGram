# PlatziGram Views

# Django
from django.http import HttpResponse

# Utils
from datetime import datetime
import json


def hello_word(request):
    now = datetime.now().strftime('%b %dth, %y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current server time is {now}'.format(
        now=str(now)
    ))


def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Intergers sorted successfully'
    }
    # import pdb
    # pdb.set_trace()

    return HttpResponse(
        json.dumps(data),
        content_type='application/json'
    )


def say_hi(request, name, age):
    if age < 12:
        message = f'Sorry {name}, you are not allowed here'.format(name)
    else:
        message = f'Hello, {name}! Welcome to Platzigram'.format(name)

    return HttpResponse(message)
