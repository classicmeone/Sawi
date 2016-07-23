from django.shortcuts import render
from django.http import HttpResponse
from .models import * #Event, Gallery, Management, Institution, News, Course
from django.contrib.auth import authenticate, login
from Sawi.forms import * #SearchForm, ContactForm,FormsetTest, NewsForm;
from django.forms import formset_factory, modelformset_factory
from django.views.decorators.http import require_http_methods
# Create your views here.


def news():
    news = News.objects.order_by("_datePosted")[:6];
    return news;
def index(request):
    try:
        latest_event = Event.objects.order_by("-date")[:5]
    except:
        raise("EVent Date not found");
    
    search = search_box(request)
    gallery = Gallery.objects.order_by('-date')[:5]
    latest_news = news()#News.objects.order_by('-datePosted')[:5]
    searchForm = SearchForm();
    #principal = Management.objects.filter(position="Principal")
    
    context = {'page_title':'Welcome To Sofwat', latest_news:latest_news, 'searchForm':searchForm, "shows":search[0], "bookmark":search[1]};
    return render(request, "Sawi/home.html", context)


@require_http_methods(["POST","GET"])
def registration(request):
    pass
def search_box(request):
    form = SearchForm({'name':"Man"});
    shows = False
    bookmark = {}
    
    if 'query' in request.GET:
        shows = True
        query = request.GET['query'];
        if query:
            form = SearchForm({"query":query})
            bookmark = {"name":"Sola", "Sex":"Shemale","Age":30}
    return shows, bookmark
def loadNews(request, title):
    
    news = News.objects.get(tit=title);
    context = {"news":news, 'page_title':'Sofwat News Page'}
    return render(request, "Sawi/news.html", context)

def about(request):
    
    institute = Institution.objects.get(pk = 1);
    news = news()
    #institute = "Softwat Al-islam"
    context= {"institute":institute, 'page_title':'About Sofwat Al-Islam', "latest_news":news}
    return render(request, "Sawi/about.html", context);
    
def contactus(request):
    
   news = news()
   if(request.method == 'POST'):
      # pass
      conform  = ContactForm(request.POST);
      if(conform.is_valid()):
          
          name = conform.cleaned_data['name'];
          
          return HttpResponse("Thank you " + name+ " WE SHALl get back to you ASAP")
          
       
   else:
       context = {'page_title':'SOfwat Contact Details',"latest_news":news}
       return render(request, "Sawi/contact-us.html", context)
   
   
def courses(request):
    pageTitle = "Courses Available"
    news = news()
    courses = Course.objects.all()
    context = {"courses":courses, "page_title":pageTitle, "latest_news":news}
    return render(request, "Sawi/course.html", context);
    #return HttpResponse("Thank you")
def admission(request):
    page_title = "Admission Requirement"
    news = news()
    AdmFrm = AdmissionForm()
    context = {"page_title":page_title, "form":AdmFrm, "latest_news":news}
    
    return render(request, "Sawi/admission.html", context)
def gallery(request):
    news = news()
    page_title = "Sofwat Events and Activities Images"
    
    gallery = Gallery.objects.order_by('-date');
    context = {"page_title":page_title, 'gallery':gallery, "latest_news":news}    
    
    return render(request,'Sawi/gallery.html',context)

def editCourse(request, courseID):
    course = Course.objects.get(pk=courseID)
    courseForm = CourseForm(course)
    news = news()
    if(request.method == "POST"):
        courseForm = CourseForm(request.POST)
        if courseForm.is_valid():
            coourseForm.save()
    else:
        context = {"form":courseForm, "page_title":"Course Edit Form", "latest_news":news}
        
    return HttpResponse("THank you for coming")

def formsetView(request):
    formset = formset_factory(FormsetTest, extra=2)
    if(request.method == "POST"):
        
        if(formset.is_valid()):
            alerts = "Thank you for your loyalty"
            
            return render(request, "Sawi/formsettest.html", {'alerts':alerts})
            
            
    return render(request, "Sawi/formsettest.html", {'formset':formset})

def newSet(request):
    Newset = modelformset_factory(News, form=NewsForm)
    form = Newset(queryset=News.objects.order_by("-datePosted")[:2],)# initial ={"title":"Title of news"})
    context = {"form":form, "page_title":"Test Page For Some Functionality", "length":len(form)}
    return render(request, "Sawi/test.html", context)

def uploadImages(request):
    if(request.method =="POST"):
        form = FileUpload(request.POST, request.FILES)
        
        if form.is_valid():
            title = request.POST['title']
            file = request.FILES['image']
            name = file.name
            if handleFile(file, name):
                return HttpResponse("Image Loaded")
                
    else:
        #f
            
        form = FileUpload()
    context = {"fileForm":form, "page_title":"Image Upload Page"}
    return render(request, "Sawi/test.html", context);

def handleFile(file, title):
    if(file):#.endswith(('png', 'jpg', 'jpeg', 'gif'))):
        #print("File processing")
        #with open("C:/Users/Michaelsegun/Documents/Images/".title, 'wb+') as destination:
        destination = open("C:/Users/Michaelsegun/Documents/Images/"+title, 'wb+')
            #f
        for chunk in file.chunks():
                #c
            destination.write(chunk)
        return True
        
        #return "Thank you"
    else:
        raise ValueError("Please select an image file");
def loginView(request):
    if request.method == "POST":
        username= request.POST['uname']
        password = request.POST['pass']
        users = authenticate(username=username, password=password);
        if(users is not None):
            login(request, users)
            return HttpResponse("Login successful")
        else:
            return HttpResponse("Backoff haters")
        
    context = {"page_title":"Login Page"};
    return render(request, "Sawi/login.html", context)
    return HttpResponse("Welcome to django login page")