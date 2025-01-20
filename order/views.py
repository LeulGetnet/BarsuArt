from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
# Create your views here.
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import OrderForm
from .models import Order, OrderFormDescription
from originals.models import Artwork
from django.conf import settings
from django.contrib import messages

def send_order_email(subject, message, uploaded_image):
    try:
        email = EmailMessage(
            subject,                # Subject of the email
            message,                # Body of the email
            settings.DEFAULT_FROM_EMAIL,  # Sender's email address
            [settings.DEFAULT_TO_EMAIL] # Reciver's email address
        )
        file_name = uploaded_image.name
        file_data = uploaded_image.read()
        content_type = uploaded_image.content_type
        print(file_data)
        print(content_type)
        email.attach(file_name, file_data, content_type)
        email.send(fail_silently=False)
        return True

    except Exception as e: 
        print(f"failed to send email to {settings.DEFAULT_TO_EMAIL}: {e}")
        return False

def orderView(request):
    latest_work = Artwork.objects.order_by('-created_at').filter(catagory="order")
    
    originals = []
    for original in latest_work:
        latest_image = original.images.order_by('created_at').first()  # Get the latest image based on created_at
        originals.append({
            'original': original,
            'latest_image': latest_image
        })
    context = {
             'originals': originals,
             'title' : "Art's made by order",
             'site_title' : 'orders'
        }
    return render(request, 'orders_list.html', context)

def order(request):
    
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)  # Redirect after successful form submission
        
        if form.is_valid():
            # Save the form data to the database
            name = form.cleaned_data.get("user_name")
            description = form.cleaned_data.get("description")
            sample_photo = form.cleaned_data.get("sample_photo")
            wanted_size = form.cleaned_data.get("wanted_size")
            style = form.cleaned_data.get("style")
            email_or_phone_number= form.cleaned_data.get("email_or_phone_number")
            form.save()

            text = f"""name: {name}, 
                    description: {description}, 
                    wanted size: {wanted_size} 
                    style {style} 
                    cotact type: {email_or_phone_number}"""
            email_sent = send_order_email("New order from barsuARt", text, sample_photo)
            if email_sent:
                messages.success(request, "information successfully submited thank you.")
            # Optionally add custom behavior (e.g., sending an email)
                return redirect('index')
            
            messages.info(request, "your record has been saved but the owner didnt recive a notification email")
            return redirect('index') # in the future if we want to raise an error or different handling method if email sent faild.
        messages.error(request, "invalid input please check your data and try again.")
        return redirect('index')
    else:
        description = OrderFormDescription.objects.order_by('-created_at').first()
        form = OrderForm()
        context = {
            "description": description,
            "form": form,
            'site_title' : 'order_form'
        }
        return render(request, 'order.html',  context)
    
def detail(request, id):
    Artworks = get_object_or_404(Artwork, id=id)
    list_image = Artworks.images.order_by('created_at')  # Get the latest image based on created_at
    context = {
        'Artwork': Artworks,
        'list_image': list_image,
        'site_title' : Artworks.title
    }
    return render(request, 'detail.html', context)