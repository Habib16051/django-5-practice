from django.shortcuts import render
from datetime import datetime
# Create your views here.

def introduction(request):
    """
    Render the introduction page.
    """
    return render(request, 'intro/introduction.html')

#  Dynamically generated view for the home page
def home_view(request):
    d = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    students_list = [
        {'name': 'Alice', 'age': 20},
        {'name': 'Bob', 'age': 22},
        {'name': 'Charlie', 'age': 21},
    ]
    context = {
        'title': 'Home Page',
        'message': 'Welcome to the Home Page!',
        'current_time': d,
        'students': students_list,
    }
    """
    Render the home page.
    """
    return render(request, 'intro/home.html', context=context)