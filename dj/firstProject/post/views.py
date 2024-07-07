from django.shortcuts import render,HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
def home(request):
    return HttpResponse("This is first view....")

def contact(request):
    
    return render(request,"contact.html",{"name":"Nikita",
                                          "address":"Mumbai",
                                          "school":"Vikas school"})


def employee(request):
    employees={
        "101":{"name":"Manoj","age":25,"salary":50000},
        "102":{"name":"Nisha","age":29,"salary":35000},
        "103":{"name":"Manoj","age":25,"salary":50000},
        "104":{"name":"Nisha","age":29,"salary":35000}
    }
    return render(request,"employee.html",{"employees":employees})


def subjects(request):
    return render(request,"subject.html",{"subject":["Maths","English","History","Science"],"age":69})


def inputData(request):
    return render(request,"data.html")


def submit(request):
    if request.method=="GET":
        return HttpResponse("You are not allowed to be here Through GET")
    elif request.method=="POST":
        # username=request.GET.get("username")
        username=request.POST.get("username")
        phoneno=request.POST.get("phoneno")
        print(username)
        return render(request,"data.html",{"username":username,"phoneno": phoneno})
#=============================================================================================
#  TemplateView
    
class StudentView(TemplateView):
    template_name="studentview.html"
   
    def get_context_data(self):
        context=super().get_context_data()
        context["name"]="Janki"
        context["age"]=18
        return context
    

