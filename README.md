# testDocker1

This is a simple Flask web application that displays the count of the number of times the webpage has been loaded ever.

To build the container image locally:
```
(.venv) ec2-user:~/path/to/file (main)$ docker build -t flask-container .
(.venv) ec2-user:~/path/to/file (main)$ docker run -p 8080:8080 flask-container
```


