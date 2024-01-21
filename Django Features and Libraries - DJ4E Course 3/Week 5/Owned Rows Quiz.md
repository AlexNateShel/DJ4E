# Owned Rows Quiz

### 1. Why do we insist on producing a delete confirmation screen?
- [x] Because a GET request should never modify data
- [ ] Because a POST request cannot modify data
- [ ] Because Django would not be able to delete the data
- [ ] To make sure that there are not JavaScript errors

### 2. Which of the following methods is called first in the Django generic list view?
- [ ] get_queryset()
- [ ] render_to_response
- [x] setup()
- [ ] get()
- [ ] startup

### 3. Which method do we override in the Django generic list view to keep users from making changes to the rows they don't own?
- [x] get_queryset()
- [ ] render_to_response
- [ ] setup()
- [ ] get()
- [ ] startup

### 4. What doed OwnerUpdateView do if a user tries to delete a record that does not belong to them?
- [ ] It stops and fails with an error log message
- [ ] It redirects the user to www.djangoproject.org
- [ ] It puts out an error message in the JavaScript console
- [x] It returns a 404 (not found error) 

### 5. What template variable indicates the current logged-in user?
- [ ] request.user
- [x] user
- [ ] article.owner
- [ ] tsugi.user
- [ ] myarts.owner

### 6. What is the name of the model that Django uses to store User objects?
- [x] settings.AUTH_USER_MODEL
- [ ] DjangoUsers
- [ ] settings.USERS
- [ ] Users
- [ ] django.users

### 7. What is the database relationship between the Article model and the User model?  
- [ ] Many-to-Many
- [ ] One-to-One
- [x] One-to-Many
- [ ] Zero-to-Zero

### 8. In views.py in the myarts cample code, what is the purpose of the "fields" class-wide value? 
- [ ] To double-check that model fields are not missing
- [x] To limit the model fields displayed in the form
- [ ] To list the fields that will be autosaved 
- [ ] To make the listed fields un-editable

### 9. For a data model named Frog, what is the generic Edit View convention for the template used when editing a Frog object?
- [x] frog_form.html
- [ ] frog_update.html 
- [ ] frog_modify.html
- [ ] frog_edit.html

### 10. In the OwnerCreateView, what method is overriden to set the "owner" field to the current logged-in user?
- [ ] add_owner()
- [x] form_valid() 
- [ ] LoginRequiredMixin
- [ ] save(commit=False)

### 11. In the OwnerUpdateView, how do we make sure that the current logged-in user cannot retrieve any rows that don't belong to them?  
- [ ] We call the method of the same name in the super class
- [x] We add a model filter
- [ ] We retrieve all the objects and throw away the non-owned objects 
- [ ] We intercept the SQL and add a WHERE clause

### 12. In OwnerUpdateView, which is the "super" or "parent" class?
- [x] UpdateView
- [ ] OwnerUpdateView 
- [ ] UpdateView::Super
- [ ] SuperUpdateView
- [ ] get_queryset()

### 13. When a generic edit view is receiving POST data, which of the following steps is done first?
- [ ] first_post()
- [x] clean()
- [ ] form_valid()
- [ ] pre_post()
- [ ] get_query_set()