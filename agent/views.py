from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from user.models import NewRequest
from .forms import CustomUserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from chat.models import PrivateMessage
from .forms import PrivateMessageForm

# Create your views here.

def agent(request):
    return render(request,"agent.html")

def unassigned_requests(request):
    success_message = None  # Initialize success_message
    
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        request_instance = NewRequest.objects.get(pk=request_id)
        request_instance.assign_to_agent(request.user)
        success_message = "The request has been added to your supports!"

    # Retrieve unassigned requests for both POST and GET requests
    unassigned_requests = NewRequest.objects.filter(status='waiting')
    
    return render(request, 'unassigned.html', {'unassigned_requests': unassigned_requests, 'success_message': success_message})

# View to display requests assigned to the logged-in agent
def my_supports(request):
    if request.method == 'POST':
        # Check if the request is marked as resolved
        request_id = request.POST.get('request_id')
        if request_id:
            # Get the request instance
            request_instance = NewRequest.objects.get(pk=request_id)
            # Mark the request as resolved
            request_instance.status = 'resolved'
            request_instance.save()

    assigned_requests = NewRequest.objects.filter(assigned_agent=request.user).exclude(status='resolved')
    return render(request, 'mysupports.html', {'assigned_requests': assigned_requests})

def assigned_requests(request):
    assigned_requests = NewRequest.objects.filter(status='assigned').exclude(assigned_agent=request.user)
    return render(request, 'assigned.html', {'assigned_requests': assigned_requests})


def resolved_requests(request):
    # Retrieve resolved requests
    resolved_requests = NewRequest.objects.filter(status='resolved')
    return render(request, 'resolved.html', {'resolved_requests': resolved_requests})

def testmsgage(request):
    return render(request,"testmsgage.html")

def register(request):
    success_message = None
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "user created successfully"
            return redirect('agent')

    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form, 'success_message': success_message})

def private_messagea(request, request_id):
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
            return redirect('private_messagea', request_id=request_id)
    else:
        # Create an empty form instance
        form = PrivateMessageForm()

    # Render the template with the form and messages list
    return render(request, 'privatemsga.html', {
        'form': form,
        'current_request': current_request,
        'messages_list': messages_list,
    })

def logout_agent(request):
    logout(request)
    # Redirect to the starting web page
    return redirect('')