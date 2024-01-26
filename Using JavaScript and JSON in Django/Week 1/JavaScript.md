# DJ4E JavaScript Quiz

### 1. Where does the following JavaScript code execute?
```
<p>One Paragraph</p>

<script type="text/javascript">
 document.write("<p>Hello World</p>")
</script>

<p>Second Paragraph</p>
```
- [x] In the browser
- [ ] In the web server
- [ ] In the database server
- [ ] On the network

### 2. What happens when JavaScript runs the alert() function?  
- [x] JavaScript execution is paused and a dialog box pops up
- [ ] JavaScript pops up a dialog box and execution continues until the </alert> tag is encountered
- [ ] JavaScript checks to see if there are any unprocessed events
- [ ] A message is sent back to the Django code to be logged on the server

### 3. Which of the following is NOT a way to include JavaScript in an HTML document?
- [ ] By including the code between <script> and </script> tags
- [x] By including the code the <?javascript and ?> tags
- [ ] On a tag using an attribute like onclick="" 
- [ ] By including a file containing JavaScript using a <script> tag
- [ ] 

### 4. In the following code, what does the "return false" accomplish?
```
<a href="js-01.htm" onclick="alert('Hi'); return false;">Click Me</a>
```
- [ ] It is necessary to insure that the onclick code is at least two lines of code
- [x] It keeps the browser from following the href attribute when "Click Me" is clicked
- [ ] It sets the default for the alert() dialog box
- [ ] It suppresses the pop-up dialog that asks "Are you sure you want to navigate away from this page?"

### 5. What happens in a normal end user's browser when there is a JavaScript error?  
- [ ] JavaScript prints a traceback indicating the line in error
- [ ] JavaScript logs the error to the Django error log
- [x] Nothing except perhaps a small red error icon that is barely noticeable
- [ ] JavaScript skips the line in error and continues executing after the next semicolon (;) 

### 6. Where can a developer find which line in a web page of JavaScript file is causing a syntax error? 
- [ ] By doing a "View Source" to see the HTML source code
- [ ] By looking at the file on the hard disk of the system where the browser is running
- [x] In developer console in the browser
- [ ] In the Django error log

### 7. What does the following JavaScript do?
```
console.log("This is a message");
```
- [ ] Puts the message in the Django console log
- [ ] Sends the message to console.log.com
- [ ] Puts the message in the browser console and pauses JavaScript execution
- [x] Puts the message in the browser developer console and continues JavaScript execution

### 8. Which of the following is not a valid comment in JavaScript?
- [ ] // This is a comment
- [ ] /* This is a comment
- [x] # This is a comment

### 9. Which of the following is not a valid JavaScript variable name?
- [ ] _data
- [ ] $_data
- [ ] $data
- [x] 3peat

### 10. What is the difference between strings with single quotes and double quotes in JavaScript?
- [ ] Double-quoted strings cannot be used in JavaScript
- [ ] Double-quoted strings do variable substitution for variables that start with dollar sign ($)
- [x] There is no difference
- [ ] Single-quoted strings do not treat \n as a newline

### 11. What does the following JavaScript print out?
```
toys = ['bat', 'ball', 'whistle', 'puzzle', 'doll']; console.log(toys[1]); 
```
- [ ] whistle
- [ ] doll
- [ ] bat
- [ ] puzzle
- [x] ball

### 12. What value ends up in the variable x when the JavaScript below is executed?
```
x = 27 % 2
```
- [ ] 0
- [ ] 54
- [ ] 2
- [ ] 27
- [x] 1
- [ ] 13.5

### 13. What is the meaning of the "triple equals" operator (===) in JavaScript?
- [x] The values being compared are the same without any type conversion
- [ ] Both sides of the triple equals operator are converted to strings before comparision
- [ ] Both sides of the triple ewuals operator are converted to boolean before comparision
- [ ] Both sides of the triple ewuals operator are converted to integers before comparision

### 14. How do you indicate that a variable reference within a JavaScript function is a global (i.e., not a local) variable?
- [ ] Use the keyword "global" to declare the variable in the function
- [ ] Use the keyword "var" to declare the variable in the function
- [ ] Use the keyword "global" when declaring the variable outside the function
- [x] Declare the variable globally before the function in the code
