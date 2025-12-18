from django.shortcuts import render
from .models import NewRequest
from .forms import NewRequestForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from chat.models import PrivateMessage
from agent.forms import PrivateMessageForm

from django.http import HttpResponseForbidden

# Create your views here.

def user(request):
    return render(request,"user.html")

@login_required
def newrequest(request):
    if request.method == 'POST':
        form = NewRequestForm(request.POST)
        if form.is_valid():
            new_request=form.save(commit=False)
            new_request.user=request.user
            new_request.save()
            success_message = "Your request has been successfully sent!"
            return render(request, 'newrequest.html', {'form': form, 'success_message': success_message})
    else:
        form = NewRequestForm()
    return render(request, 'newrequest.html', {'form': form})

def testmsg(request):
    return render(request,"testmsg.html")

@login_required
def myrequest(request):

    requests = NewRequest.objects.filter(user=request.user)
    return render(request, 'myrequest.html', {'requests': requests})

def private_messageu(request, request_id):
        # Get the corresponding request using request_id
    current_request = get_object_or_404(NewRequest, pk=request_id)

    # Fetch all private messages related to the current request
    messages_list = PrivateMessage.objects.filter(request=current_request).order_by('-timestamp')

    if request.method == 'POST':
        # Create a form instance with POST data
        form = PrivateMessageForm(request.POST)

        if form.is_valid():
            # Create a new PrivateMessage instance
            new_message = form.save(commit=False)
            new_message.request = current_request
            new_message.username = request.user.username  # Assuming a logged-in user

            # Save the new PrivateMessage instance
            new_message.save()

            # Add a success message
            messages.success(request, 'Message sent successfully.')

            # Redirect to the same page to prevent form resubmission and reload messages
            return redirect('private_messageu', request_id=request_id)
    else:
        # Create an empty form instance
        form = PrivateMessageForm()

    # Render the template with the form and messages list
    return render(request, 'privatemsgu.html', {
        'form': form,
        'current_request': current_request,
        'messages_list': messages_list,
    })