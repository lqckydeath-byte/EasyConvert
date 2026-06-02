from django.shortcuts import render


def calculator(request):

    result = None

    if request.method == 'POST':

        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']

        if operation == '+':
            result = num1 + num2

        elif operation == '-':
            result = num1 - num2

        elif operation == '*':
            result = num1 * num2

        elif operation == '/':
                result = num1 / num2
    return render(request, 'calculator.html', {'result': result})