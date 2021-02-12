from django.shortcuts import redirect, render
from .forms import ContactForm
import telebot
bot = telebot.TeleBot('1451470227:AAEMgbtTkbbDvskwBEtYaEFuFJ0h5yS0KUI')


def index(request):
    return render(request, 'index.html', {})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            msg = f"Имя: {name} \n" \
                  f"Почта: {mail} \n" \
                  f"Тема: {subject} \n" \
                  f"Текст: {message} "
            bot.send_message(565812696, msg)

    return redirect('home')

