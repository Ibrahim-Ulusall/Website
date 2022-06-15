from django.shortcuts import render

# Create your views here.
data = {
    'lessons': [
        {
            'id' : 1,
            'title' : 'Sıfırdan Html 5 Dersleri',
            'image' : 'html.png',
            'description' : 'Sıfırdan ileri düzey web tasarımı için Html dersleri'
        },
        {
            'id' : 2,
            'title' : 'Sıfırdan CSS 3 Dersleri',
            'image' : 'css.png',
            'description' : 'Sıfırdan ileri düzey web tasarımı için Html dersleri'
        },
        {
            'id' : 3,
            'title' : 'Sıfırdan Bootstrap Dersleri',
            'image' : 'bootstrap_logo.png',
            'description' : 'Sıfırdan ileri düzey web tasarımı için Html dersleri'
        },
        {
            'id' : 1,
            'title' : 'Sıfırdan C# Dersleri',
            'image' : 'csharp.png',
            'description' : 'Sıfırdan ileri düzey web tasarımı için Html dersleri'
        },
        {
            'id' : 1,
            'title' : 'Sıfırdan Php Dersleri',
            'image' : 'php.png',
            'description' : 'Sıfırdan ileri düzey web tasarımı için Html dersleri'
        },
        {
            'id' : 1,
            'title' : 'Sıfırdan Python Dersleri',
            'image' : 'python_logo.png',
            'description' : 'Sıfırdan ileri düzey web tasarımı için Html dersleri'
        },
    ]
}
class Domains:
    
    def __init__(self) -> None:
        pass
    
    # www.deltasoftware.com
    # www.deltasoftware.com/index
    def index(self,request):
        return render(request,'blog/index.html',{
            'lessons': data['lessons']
        })
    
    # www.deltasoftware.com/blogs
    def blogs(self,request):
        return render(request,'blog/blogs.html')    
    
    # www.deltasoftware.com/blogs/5
    def blog_details(self,request,id):
        return render(request,'blog/blog-details.html',{
            'id': id
        })
        
    # www.deltasoftware.com/login
    def login(self,request):
        return render(request,'blog/login.html')
    
    # www.deltasofware.com/register
    
    def register(self,request):
        pass