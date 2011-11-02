from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.data.models import Entry
from apps.homepage.forms import ContactForm

def index(request):
    entries = Entry.objects.published_entries()
    return render_to_response('homepage/index.html', {
        'entries': entries,
        }, context_instance=RequestContext(request)
    )

def about(request):
    return render_to_response('homepage/about.html', {
        }, context_instance=RequestContext(request)
    )

def archive(request):
    return render_to_response('homepage/archive.html', {
        }, context_instance=RequestContext(request)
    )

def contact(request):

    success = False
    email = ""
    title = ""
    text = ""

    
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            success = True
            email = contact_form.cleaned_data['email']
            title = contact_form.cleaned_data['title']
            text = contact_form.cleaned_data['text']

    else:
        contact_form = ContactForm()

    return render_to_response('homepage/contact.html', {
            'contact_form': contact_form,
            'success': success,
            'email': email,
            'title': title,
            'text': text,
        }, context_instance=RequestContext(request)
    )

