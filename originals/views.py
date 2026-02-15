from django.shortcuts import render, redirect
from django.http import HttpResponse
from aboutme.models import AboutMe
from .models import Artwork
from backgroundvid.models import Video
from django.shortcuts import render, get_object_or_404
from contactme.forms import ContactForm
# views.py or any other module

from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from datetime import datetime

def send_confirmation_email(subject, message, sender_name, userEmail):
    try:
        # Prepare context for the email template
        context = {
            "subject": subject,
            "message": message,
            "sender_name": sender_name,
            "sender_email": userEmail,
            "date": datetime.now().strftime("%B %d, %Y %I:%M %p"),
            "year": datetime.now().year
        }
        
        # Render HTML email template with context
        html_content = render_to_string("email_templates/contact.html", context)
        text_content = strip_tags(html_content)  # Convert HTML to plain text fallback

        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,  # Plain text version
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.DEFAULT_TO_EMAIL],
            reply_to=[userEmail],
        )
        email.attach_alternative(html_content, "text/html")  # Attach HTML version

        email.send(fail_silently=False)
        return True
    except Exception as e:
        print(f"Error sending email to {settings.DEFAULT_TO_EMAIL}: {e}")
        return False



def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            form.save()
            sent_email = send_confirmation_email(f"Barsenet art contact me from {user_name}", message, user_name, email)
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
        latest_work = Artwork.objects.order_by('-created_at').filter(category="original")
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
