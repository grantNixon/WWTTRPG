from django.shortcuts import render

# Create your views here.
def test_view(request):
    # python manage.py migrate
    # check apps.py file inside my_app
    # confirm Config class is there
    # add Config to INSTALLED_APPS ('my_app.apps.MyAppConfig')
    # python manage.py makemigrations my_app (result is No changes detected in app 'my_app')
    # python manage.py migrate (no migrations to apply)
    # create my_app/templates/my_app/home.html
    return render(request,'home_page/homepage.html')

def getting_started(request):
    return render(request, 'home_page/Getting_Started.html')

