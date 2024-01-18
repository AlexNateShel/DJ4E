# The Request / Response Cycle 

## Practice Quiz

1. When a browser connects to a web server to retrieve a document, what default TCP/IP port is used?
   - [] 142
   - [x] 80
   - [] 420
   - [] 119
   - [] 25

2. When a browser connects to a web server to retrieve a document, what command is sent to the server?
   - [] PUT
   - [] POST
   - [x] GET
   - [] DELE

3. What does the second "T" of HTTP stand for?
   - [x] Transfer
   - [] Transpose
   - [] Transport
   - [] movemenT

4. Which of the following is NOT a part of the Uniform Resource Locator:
   - [] Host
   - [x] Operating System
   - [] Document
   - [] Protocol

5. Which HTML tag typically generates a request to retrieve a document from the server when it is clicked?
   - [] b
   - [] h1
   - [x] a
   - [] div
   - [] p
   - [] img

6. What standards organization publishes many of the documents that describe the protocols we use on the internet?
   - [] 6-Sigma
   - [] RIA
   - [] Educause
   - [] IRR
   - [x] IETF

7. Which of the HTTP headers does the browser look at to decide how to display the retrieved document?
   - [] ETAG
   - [] Display-type
   - [] Location
   - [x] Content-Type
   - [] Format
   - [] Content-length

8. In Python, what is the difference between an open file and a socket?
   - [x] A socket can be simultaneously read and written
   - [] When you open a file, you get a read and write handle to allow simultaneous operations
   - [] A program can rewind a socket and start writing again at the beginning of the socket
   - [] A program writes to a socket, it can read its data back after closing the socket

9. What must happen before a client can open a socket?
   - [] The client must create a local file with the same name as the socket
   - [] The client must be in the same folder as the server
   - [x] A server must be running that is listening for socket connections
   - [] A client must be on the same system as the server
   - [] The server must allocate sufficient memory to handle any needed retransmissions

10. What port is used for the Simple Mail Transer Protocol (SMTP) ? 
   - [x] 25
   - [] 119
   - [] 142
   - [] 420
   - [] 80

11. What port is used by default for Secure HTTP (https) ?
   - [] 119
   - [] 142
   - [] 25
   - [] 80
   - [x] 443

12. What is the topic of the Internet Engineering Task Force document RFC2616?
   - [] SMTP - Simple Mail Transfer Protocol
   - [] FTP - File Transfer Protocol
   - [] POP - Post Office Protocol
   - [] Message Data Types
   - [x] HTTP - HyperText Transfer Protocol

13. What is the topic of the Internet Engineering Task Force document RFC42?
   - [] SMTP - Simple Mail Transfer Protocol
   - [] FTP - File Transfer Protocol
   - [] POP - Post Office Protocol
   - [x] Message Data Types
   - [] HTTP - HyperText Transfer Protocol

14. Wich of these Internet Engineering Task Force (IETF) documents described the "Internet Control Message Protocol"?
   - [] RFC5325
   - [] RFC1224
   - [x] RFC792
   - [] RFC815

15. What is the purpose of encode() in the socket1.py code:
   - [] To make sure that the web server properly recognizes the GET command
   - [] To break the data into packets for network transmission
   - [x] To convert the data to UTF-8 before sending
   - [] To check if there is any data ready to send

16. What can't you see in the Browser Developer Mode for most browsers?
   - [] The browser Document Object Model (DOM)
   - [x] The code that runs in the server
   - [] The HTTP response code (like 200 or 404) for each request
   - [] The request and response headers for retrieved documents

17. In the sample server.py code, which function call actually waits for incoming socket connections requests?
   - [x] listen()
   - [] socket()
   - [] recv()
   - [] bind()
   - [] decode()

18. In the same server.py code, which function call will fail if another application is already using a port?
   - [] listen()
   - [] socket()
   - [] recv()
   - [x] bind()
   - [] decode()

19. Which Python library makes it very easy to make HTTP requests from Python?
   - [] decode
   - [] re
   - [x] urllib
   - [] json