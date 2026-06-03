import random
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def calculator(request):
    result = None

    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', ''))
            num2 = float(request.POST.get('num2', ''))
            operation = request.POST.get('operation')

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
        except (TypeError, ValueError):
            result = None

    return render(request, 'calculator.html', {'result': result})


def square(request):
    result = None

    if request.method == 'POST':
        try:
            value = float(request.POST.get('value', ''))
            result = value * value
        except (TypeError, ValueError):
            result = None

    return render(request, 'kvadrat.html', {'result': result})


def cube(request):
    result = None

    if request.method == 'POST':
        try:
            value = float(request.POST.get('value', ''))
            result = value ** 3
        except (TypeError, ValueError):
            result = None

    return render(request, 'cube.html', {'result': result})


def temperature(request):
    result = None

    if request.method == 'POST':
        try:
            value = float(request.POST.get('value', ''))
            result = (value * 9 / 5) + 35
        except (TypeError, ValueError):
            result = None

    return render(request, 'temperature.html', {'result': result})


def luck(request):
    result = None
    comment = None

    if request.method == 'POST':
        result = random.randint(0, 100)
        if result < 30:
            comment = 'не повезло'
        elif result < 80:
            comment = 'пойдет'
        else:
            comment = 'Быстрее беги в казино'

    return render(request, 'luck.html', {'result': result, 'comment': comment})


def weight(request):
    result = None

    if request.method == 'POST':
        try:
            value = float(request.POST.get('value', ''))
            from_unit = request.POST.get('from_unit')
            to_unit = request.POST.get('to_unit')
            kg = 0

            if from_unit == 'g':
                kg = value / 1000
            elif from_unit == 'kg':
                kg = value
            elif from_unit == 't':
                kg = value * 1000

            if to_unit == 'g':
                result = kg * 1000
            elif to_unit == 'kg':
                result = kg
            elif to_unit == 't':
                result = kg / 1000
        except (TypeError, ValueError):
            result = None

    return render(request, 'weight.html', {'result': result})


def memory(request):
    result = None

    if request.method == 'POST':
        try:
            value = float(request.POST.get('value', ''))
            from_unit = request.POST.get('from_unit')
            to_unit = request.POST.get('to_unit')
            mb = 0

            if from_unit == 'kb':
                mb = value / 1024
            elif from_unit == 'mb':
                mb = value
            elif from_unit == 'gb':
                mb = value * 1024

            if to_unit == 'kb':
                result = mb * 1024
            elif to_unit == 'mb':
                result = mb
            elif to_unit == 'gb':
                result = mb / 1024
        except (TypeError, ValueError):
            result = None

    return render(request, 'memory.html', {'result': result})


def vremya(request):
    result = None

    if request.method == 'POST':
        try:
            value = float(request.POST.get('value', ''))
            from_unit = request.POST.get('from_unit')
            to_unit = request.POST.get('to_unit')
            sec = 0

            if from_unit == 'sec':
                sec = value
            elif from_unit == 'min':
                sec = value * 60
            elif from_unit == 'hour':
                sec = value * 3600

            if to_unit == 'sec':
                result = sec
            elif to_unit == 'min':
                result = sec / 60
            elif to_unit == 'hour':
                result = sec / 3600
        except (TypeError, ValueError):
            result = None

    return render(request, 'vremya.html', {'result': result})