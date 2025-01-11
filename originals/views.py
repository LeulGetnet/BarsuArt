from django.shortcuts import render, redirect
from django.http import HttpResponse
from aboutme.models import AboutMe
from .models import Artwork
from backgroundvid.models import Video
from django.shortcuts import render, get_object_or_404
from contactme.forms import ContactForm
# views.py or any other module

from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages


def send_confirmation_email(subject, message, userEmail):
    try:
        EmailMessage(
            subject,                # Subject of the email
            message,                # Body of the email
            settings.EMAIL_HOST_USER,  # Sender's email address
            [settings.DEFAULT_TO_EMAIL],           # Recipient's email address
            reply_to=[userEmail]
        ).send(fail_silently=False)
        return True
    except Exception as e:
        print(f"error to send email to ueser {settings.DEFAULT_TO_EMAIL} : {e}")
        return False

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            form.save()
            sent_email = send_confirmation_email("new contact me notification from barsuArt", f"user name: {user_name} email: {email} message: {message}", email)
            if sent_email:
                messages.success(request, "Your message was sent successfully!")
                return redirect('index')
            else:
                print("testing if it ever gets here")
                messages.info(request, "your record has been saved but the owner didnt recive a notification email")
                return redirect('index')#in the future if we want to raise an error or different handling method if email sent faild.
        messages.error(request, "invalid input please check you data and try again.")
        return redirect('index')
    else: 
        aboutme = AboutMe.objects.order_by('-created_at').first()
        if aboutme:
            back_vid = Video.objects.first()
        else:
            back_vid = None
        form = ContactForm()
        context = {
            'aboutme': aboutme,
            'back_vid' : back_vid,
            'form': form
        }
        return render(request, 'index.html', context)
def original_view(request):
        latest_work = Artwork.objects.order_by('-created_at').filter(catagory="original")
        originals = []
        for original in latest_work:
            latest_image = original.images.order_by('-created_at').first()  # Get the latest image based on created_at
            originals.append({
                'original': original,
                'latest_image': latest_image
            })
        context = {
             'originals': originals,
             'title' : 'My original art works'
        }
        return render(request, 'orders_list.html', context)
def detail(request, id):
    Artworks = get_object_or_404(Artwork, id=id)
    list_image = Artworks.images.order_by('created_at')  # Get the latest image based on created_at
    context = {
        'Artwork': Artworks,
        'list_image': list_image
    }
    return render(request, 'detail.html', context)
