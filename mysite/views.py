from django.shortcuts import render
from .models import message
from .models import count
from django.contrib.auth.models import User


def index(request):
    return render(request, "mysite/index.html")


def register(request):
    return render(request, "mysite/register.html")


def login(request):
    return render(request, "registration/login.html")


def users(request):
    data = User.objects.all()

    return render(request, "mysite/users.html", {'users': data})


def mail(request):
    if request.method == 'POST':
        if ('user_id_to' in request.POST) and (int(request.POST['user_id_to']) > 0):
            req = message(sender=request.user.id, recipient=request.POST['user_id_to'], title=request.POST['title'],
                          full_text=request.POST['full_text'])
            req.save()
            if count.objects.filter(user_from = request.user.id).exists():
                new_count = count.objects.get(user_from = request.user.id)
                new_count.count += 1
                new_count.save()
            else:
                msg_count = count(count= 1, user_from = request.user.id, user_to = request.POST['user_id_to'])
                msg_count.save()

    data = message.objects.filter(recipient = request.user.id)

    return render(request, "mysite/mail.html", {'data':data})


def send_msg(request):
    if request.method == 'POST':

        data = {
            'user_id_to': request.POST['user_id_to'],
            'error': ''
        }
    else:
        data = {
            'error': 'Ви не обрали користувача якому необхідно відправити лист'
        }
    return render(request, "mysite/send_msg.html", data)
