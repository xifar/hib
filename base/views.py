from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import WorkImage, Client, ServiceImage, OtherImage
from . forms import EnquiryForm
from . viewsSupport import *

# Create your views here.

# This function renders the page when user successfully sends
# the enquiry form
def enquiry_sent(request):
    return render(request, 'base/success.html')

# This function renders the Home page
def home(request):
    sample_display_size = 6

    flex1_image = get_image_or_client(OtherImage, keyword='flex1')
    flex2_image = get_image_or_client(OtherImage, keyword='flex2')
    flex3_image = get_image_or_client(OtherImage, keyword='flex3')
    flex_images = [flex1_image, flex2_image, flex3_image]

    about_image = get_image_or_client(OtherImage, keyword='about')

    work_images_samples = get_image_or_client(WorkImage, sample_display_size)
    clients_samples = get_image_or_client(Client, sample_display_size)

    context = {
        'hibHome_active': 'colorlib-active',
        'about_image': about_image,
        'flex_images': flex_images,
        'work_images_samples': work_images_samples,
        'clients_samples': clients_samples
    }
    return render(request, 'base/index.html', context)

# This function renders the About page
def about(request):    
    about_image = get_image_or_client(OtherImage, keyword='about')
    status_bg = get_image_or_client(OtherImage, keyword='status_bg')

    context = {
        'hibAbout_active': 'colorlib-active',
        'about_image': about_image,
        'status_bg': status_bg,
    }

    return render(request, 'base/about.html', context)

# This function renders the What We Render page
def whatWeRender(request):
    whatWeRende_image = get_image_or_client(OtherImage, keyword='what we render')

    context = {
        'hibWhatWeRender_active': 'colorlib-active',
        'whatWeRende_image': whatWeRende_image,
    }

    return render(request, 'base/whatWeRender.html', context)

# This function renders the Services page
def services(request):    
    service_images  = get_image_or_client(ServiceImage)

    context = {
        'hibServices_active': 'colorlib-active',
        'service_images': service_images,
    }

    return render(request, 'base/services.html', context)

# This function renders the Turnkey Solutions page
def turnkey(request):
    
    context = {
        'hibTurnkey_active': 'colorlib-active',
    }

    return render(request, 'base/turnkey.html', context)

# This function renders the Projects page
def work(request):    
    work_images_perPage = get_work_images_perPage(request)
    pageNo_display_list = get_pageNo_display_list()

    context = {
        'hibWork_active': 'colorlib-active',
        'work_images_perPage': work_images_perPage,
        'pageNo_display_list': pageNo_display_list,
    }

    return render(request, 'base/work.html', context)

# This function renders the Work Image page which displays 
# individual image
def work_image(request, pk = None):
    work_image = get_work_image(pk)
    
    context = {
        'hibWork_active': 'colorlib-active',
        'work_image': work_image,
    }

    return render(request, 'base/workImage.html', context)

# This function renders the Clients page
def client(request):
    clients = get_image_or_client(Client)

    context = {
        'hibClient_active': 'colorlib-active',
        'clients': clients,
    }

    return render(request, 'base/client.html', context)

# This function renders the Contact page
def contact(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/message-sent/')
    else:
        form = EnquiryForm()

    context = {
        'hibContact_active': 'colorlib-active',
        'form': form,
    }

    return render(request, 'base/contact.html', context)