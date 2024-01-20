# Django Forms Quiz

### 1. Which of the following is NOT a benefit of using the Django forms capability?
- [x] Database portability
- [ ] You reduce the amount of HTML you need to generate 
- [ ] You can easily create attractively styled forms
- [ ] You can have a mapping layer between your models and templates
- [ ] You can add complex form validation rules to your applicaiton

### 2. What happens when a Create form is submitted and Django forms detect a validation error?
- [ ] The form is re-displated with the error message
- [ ] The record is deleted from the database
- [ ] A 403 (Not authorized) is set back to the browser
- [x] The form is re-displayed with the incorrect data and error messages
- [ ] The form is re-displayed with the incorrect data

### 3. You cannot use a Django form unless it is connected to a Django model.
- [ ] True
- [x] False

### 4. How do you indicate that you want to display a form using the Crispy library in a template?  
- [ ] csrf_token
- [ ] form.as_crispy
- [x] form|crispy
- [ ] form.as_table

### 5. What does the fields="__all__" statement do in the Meta section of a Django form class?  
- [ ] Indicates that none of the model fields are to be saved
- [ ] Indicates that the owner field is not supported to be shown to the user when the form is displayed 
- [x] Indicates that all of the underlying model fields should be in the form

### 6. In what method in a view would you expect to see "form.save()" to save data from an incoming form?  
- [x] post()
- [ ] dispatch()
- [ ] get_queryset()
- [ ] get()

### 7.  What utlity method simplifies the code needed to load the old model data when processing an update request?
- [ ] load_try_except()
- [ ] render_to_template_with_check()
- [ ] conditional_render_404()
- [x] get_object_or_404()

