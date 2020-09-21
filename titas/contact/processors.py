from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')              
            
            
                     

            email = EmailMessage(
                "Titas: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@gmail.com",
                ["rodrigojrodriguezm@gmail.com","luiisana29@gmail.com","terramar.luisa@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                check = "Su mensaje se ha enviado correctamente, en breve nos pondremos en contacto con usted!!!!"
                return {'check': check,'form':contact_form }
            except:
                check = "Por favor intente de nuevo!!!!"
                return {'check': check,'form':contact_form }         

               

   
    return {'form':contact_form}
    

    

