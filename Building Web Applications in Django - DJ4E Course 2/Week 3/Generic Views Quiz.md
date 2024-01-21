# Generic Views Quiz

### 1. In the class django.generic.list.ListView, which of the following methods is called earliest in the process?
- [x] get_template_names()
- [ ] get_queryset()
- [ ] get_context_data()
- [ ] render_to_response()

### 2. In the class django.generic.detail.DetailView, which of the following methods is called latest in the process? 
- [ ] get_template_names()
- [ ] get_queryset()
- [ ] get_context_data()
- [x] render_to_response()

### 3. In the class django.generic.detail.DetailView, which of the following methods is called earliest in the process? 
- [ ] dispatch()
- [ ] get_queryset()
- [ ] get_object()
- [x] render_to_response()

### 4. In the class django.views.list.DetailView, which of the following methods is called latest in the process?    
- [ ] dispatch()
- [ ] get_queryset()
- [ ] get_object()
- [x] render_to_response() 

### 5. By convention when using an app_name of "abc" and a model of "Dog", if you use a View that extends django.viwes.generic.detail.DetailView, what is the file name that will be used for the template?
- [x] templates/abc/dog_detail.html
- [ ] templates/abc/dog_detail.djtl
- [ ] templates/dog_detail.djtl
- [ ] templates/doc/abc_detail.djtl

### 6. If you want to override the template name chosen by convention in a View that extends django.views.generic.detail.DetailView, what is the name of the class attribute variable that you use?
- [x] template_name
- [ ] template
- [ ] template_override
- [ ] template_extend

### 7. By convention when using an app_name of "abc" and a model of "Dog", if you use a View that extends django.views.generic.list.ListView, what is the name of the context variable that will include all of the Dog objects in the template when it is being redirected?
- [x] dog_list
- [ ] dogs
- [ ] dogs_select
- [ ] dog.values()

### 8. For the following line in a views.py file
```
class ArticleListView(ListView):

```
what is the best description of "ListView"?
- [x] The class that is being extended
- [ ] The class that is being created 
- [ ] The name of a view function
- [ ] The first parameter to the rendor() method

### 9. For the following line in a views.py file
```
class ArticleListView(ListView):

```
what is the best description of "ListView"?
- [ ] The class that is being extended
- [x] The class that is being created 
- [ ] The name of a view function
- [ ] The first parameter to the rendor() method

### 10. For the following line in a urls.py file
```
urlpatterns = [
    path('', TemplateView.as_view(template_name='gview/main.html'))
]
```  
where would you find the actual code for TemplateView?
- [ ] In views.py 
- [ ] In settings.py
- [ ] In urls.py
- [ ] In the Django source
