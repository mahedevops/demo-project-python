# demo-project-python
#Give the sample project in python 

To build docker build DockerImage: docker build -t python-app demo-application-python To run: docker run -dit -p 5000:5000 python-app:latest To check endpoint response: curl http://127.0.0.1:5000/health
