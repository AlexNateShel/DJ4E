# Tutorial 3 

### These Questions come from the Django project tutoril materials.

### 1. When you see a path with the following pattern in urls.py, path('<int:question_id>/', views.detail, name='detail'), where in the code does the question_id value parsed from the URL end up?
- [x] As an additional parameter to the detail() view
- [ ] As a global variable in views.py
- [ ] In the context thtat is passed to the render engine
- [ ] As part of the database connection used by the model
- [ ] In the cookies structure

### 2. What kind of data is passed into a view in the 'request' object?
- [x] Information about the incoming HTTP request from the browser
- [ ] A list of all the models available to the application
- [ ] All the possible combinations of context variables
- [ ] All of the global Python variables

### 3. Which of the following SQL commands will be run by the Question.objects.values() statement in a view function?
- [x] SELECT
- [ ] INSERT
- [ ] UPDATE
- [ ] DELETE

### 4. How do you indicate that a particular question cannot be found in a detail view?
- [x] Raise an Http404 exception
- [ ] Send back an HttpResponse with the text 'not found'
- [ ] Send back a blank page
- [ ] Raise an Http500 exception

### 5. How do you retrueve only the first five objects in a table using a Django model query?
- [x] Add [:5] to the end of the model query
- [ ] Add a LIMIT clause to the retrieved SQL
- [ ] Retrieve all the records and then write a loop to discard all but the first 5
- [ ] Use an SQL DELETE to remove all the records beyond the first 5

### 6. In Django, why do we add an extra folder (i.e., namespace) to our templates?
- [ ] To make it harder to find and edit template files
- [x] To make sure there is not a conflict with a template of the same name in a different application
- [ ] To make sure that no other application can use a template file
- [ ] To make it impossible to extend a template from one application in another application

### 7. What is the difference between a list view and a detail view?
- [x] A list view shows multiple items and a detail view shows only one item
- [ ] A list view lists all the fields in a model item and the detail view focuses on one field
- [ ] A list view throws a 404 error but a detail view never throws a 404 error

### 8. What is a "404" error?
- [x] It tells a browser that it did not get the page it was looking for
- [ ] It tells the browser that it needs to redirect to another URL
- [ ] It tells the browser that it lacks the necessary authorization to view the requested page
- [ ] It tells the browser that something unexpected happened inside the server as it was fullfilling the request

### 9. In Django, what is the default language used in HTML template files?
- [ ] Handlebars
- [x] DTL - Django Template Language
- [ ] Moustache
- [ ] HAML
- [ ] VTL - Velocity Templating Language
- [ ] Java Server Pages

### 10. If the "get_object_or_404()" helper function finds the requested item, it returns the item. What happens if it cannot return the item?
- [ ] It returns -1
- [ ] It returns False
- [x] It raises an Http404 exception
- [ ] It returns an empty object

### 11. Why do we name space URL names using the "app_name" variable in the urls.py file?
- [ ] To make it harder to write the urls.py file
- [ ] To make sure that no other application can access our local paths
- [ ] To make it impossible reference a path from one application in another application
- [x] In case we have multiple applications with the same named path
