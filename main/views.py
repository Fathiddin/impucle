from django.shortcuts import render, redirect
from .forms import AddPostForm
from django.contrib import messages
# Create your views here.


def home(request):
    form = AddPostForm() 
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            message = "Malumotlaringiz muvafaqiyatli yuborildi!"
            messages.add_message(request, messages.SUCCESS, message)
            return render(request, 'index.html', {"message":message, "form":form})
        else:
            form = AddPostForm()
            message = "Uzr malumotlaringiz yuborilmadi"
            messages.add_message(request, messages.ERROR, message)
            return render(request, 'index.html', {"message":message, "form":form})

    context = {
        'form':form
    }
    return render(request, 'index.html', context)