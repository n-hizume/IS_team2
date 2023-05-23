# Create your views here.
from django.http import HttpResponse


from .mail import get_mails
from .mail import send_mail

'''def initialfunc(request):
    #return HttpResponse("Initial")
    if request.method == 'POST':
        token = request.POST['token']
        refresh_token = request.POST['refresh_token']
        expiry = request.POST['expiry']


        response = JsonResponse({"": ""})
        response.content
        """try:
            user = User.objects.
        except IntegrityError:
            return render(request, '.html', {'error':''})"""
    else:


    return render(request, '.html' )'''




def getmailfunc(request):
    if request.method == 'POST':
        
        json_str = request.body
        response = get_mails(json_str)
        return HttpResponse(response)
        """try:
            user = User.objects.
        except IntegrityError:
            return render(request, '.html', {'error':''})"""
    else: 
        return HttpResponse('POST ONLY')
    
def sendmailfunc(request):
    if request.method == 'POST':
        
        json_str = request.body
        response = send_mail(json_str)
        return HttpResponse(response) 
        """try:
            user = User.objects.
        except IntegrityError:
            return render(request, '.html', {'error':''})"""
    else: 
        return HttpResponse('POST ONLY')






'''

def compose(request):

    # Composing a new email must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Check recipient emails
    data = json.loads(request.body)
    emails = [email.strip() for email in data.get("recipients").split(",")]
    if emails == [""]:
        return JsonResponse({
            "error": "At least one recipient required."
        }, status=400)

    # Convert email addresses to users
    recipients = []
    for email in emails:
        try:
            user = User.objects.get(email=email)
            recipients.append(user)
        except User.DoesNotExist:
            return JsonResponse({
                "error": f"User with email {email} does not exist."
            }, status=400)

    # Get contents of email
    subject = data.get("subject", "")
    body = data.get("body", "")

    # Create one email for each recipient, plus sender
    users = set()
    users.add(request.user)
    users.update(recipients)
    for user in users:
        email = Email(
            user=user,
            sender=request.user,
            subject=subject,
            body=body,
            read=user == request.user
        )
        email.save()
        for recipient in recipients:
            email.recipients.add(recipient)
        email.save()

    return JsonResponse({"message": "Email sent successfully."}, status=201)

def mailbox(request, mailbox):

    # Filter emails returned based on mailbox
    if mailbox == "inbox":
        emails = Email.objects.filter(
            user=request.user, recipients=request.user, archived=False
        )
    elif mailbox == "sent":
        emails = Email.objects.filter(
            user=request.user, sender=request.user
        )
    elif mailbox == "archive":
        emails = Email.objects.filter(
            user=request.user, recipients=request.user, archived=True
        )
    else:
        return JsonResponse({"error": "Invalid mailbox."}, status=400)

    # Return emails in reverse chronologial order
    emails = emails.order_by("-timestamp").all()
    return JsonResponse([email.serialize() for email in emails], safe=False)


def email(request, email_id):

    # Query for requested email
    try:
        email = Email.objects.get(user=request.user, pk=email_id)
    except Email.DoesNotExist:
        return JsonResponse({"error": "Email not found."}, status=404)

    # Return email contents
    if request.method == "GET":
        return JsonResponse(email.serialize())

    # Update whether email is read or should be archived
    elif request.method == "PUT":
        data = json.loads(request.body)
        if data.get("read") is not None:
            email.read = data["read"]
        if data.get("archived") is not None:
            email.archived = data["archived"]
        email.save()
        return HttpResponse(status=204)

    # Email must be via GET or PUT
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)'''