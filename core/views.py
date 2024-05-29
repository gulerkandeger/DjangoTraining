from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia, Document
# Create your views here.

def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''

    return obj

def get_image_setting(parameter):
    try:
        obj = ImageSetting.objects.get(name=parameter).file
    except:
        obj = ''

    return obj


def layout(request):  #tüm sayfalarda kullanılanlar

    # Document
    documents = Document.objects.all()
    #Home
    site_title = get_general_setting('set_title')
    site_keywords = get_general_setting('site_keywords')
    site_description = get_general_setting('site_description')
    home_banner_name = get_general_setting('home_banner_name')
    home_banner_title = get_general_setting('home_banner_title')
    home_banner_description = get_general_setting('home_banner_description')
    about_myself_welcome = get_general_setting('about_myself_welcome')
    about_myself_footer = get_general_setting('about_myself_footer')
    # Images
    header_logo = get_image_setting('header_logo')
    home_banner_image = get_image_setting('home_banner_image')
    site_favicon = get_image_setting('site_favicon')
    # Social Media
    socialmedias = SocialMedia.objects.all()

    context = {
        #Document
        'documents': documents,
        #Home
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
        # Images
        'header_logo': header_logo,
        'home_banner_image': home_banner_image,
        'site_favicon': site_favicon,
        # SocialMedia
        'socialmedias': socialmedias,
    }

    return context


def index(request):

    #Skills
    skills = Skill.objects.all().order_by('order')
    #Experiences
    experiences = Experience.objects.all()
    #Educations
    educations = Education.objects.all().order_by('-start_date')

    context = {

        #Skills
        'skills': skills,
        #Experince
        'experiences': experiences,
        #Educations
        'educations': educations,

    }

    return render(request, "index.html", context=context)

def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)

