from django.shortcuts import render
from app.models import Contact,logs

# Create your views here.
def home(request):

        # return redirect("")
    return render(request,'home.html')

def login(request):
    # if request.method=="POST":
    #         name = request.POST.get('username')
    #         p = request.POST.get('password')
    #         print(name,' ',p)
    #         re=nlogs.objects.filter(uname=p,pas=p)
    #         print(re)
    #         if re:
    #             return redirect("home")
    #         else:
    #             return render(request,"log.html")
    # else:
        return render(request,"log.html")


def create(request):
    # if(request.method=='POST'):
    #     u = request.POST.get('username')
    #     p = request.POST.get('password')
    #     e = request.POST.get('email')
    #     print(u,e,p)
    #     # s=logs.objects.filter(uname=p,pas=p,email=e)
    #     s=nlogs.objects.filter(uname=u).first()
    #     print(s)
    #     if s:
    #         print('usernmae found')
    #         messages.warning(request,'user already exist!')
    #         return render(request,'create.html')
    #         # return redirect("")
    #     else:
    #         print('no user found')
    #         entry = nlogs(uname=u,pas=p,email = e)
    #         entry.save()
    #         messages.success(request,'user created')
    #         return redirect("/")
    #         # return render(request,'create.html')
    # else:
        return render(request,'create.html')


def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')
 

def contact(request):
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     desc = request.POST.get('desc')
    #     contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
    #     contact.save()
    #     messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 