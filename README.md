# python-webserver
A simple, containerized Python web server.

# How to deploy
1. Clone the repo
2. After having docker installed, run the `docker build` and `docker run` commands in the `Dockerfile`
3. Use tool of choice (web browser, curl, carrier pigeon etc) to see the content served on port 8000

# How to test
If you're making changes to the http server (or the content it serves) and want to test outside of docker, do this:
1. Run the server: `python3 ./main.py`
2. With server running, use tool of choice to see the content served on port 8000. Example: Run `curl -i localhost:8000` from another terminal session.

# Credit:
The webserver code was initially taken from:
* https://github.com/aklatzke/python-webserver
* https://medium.com/@andrewklatzke/creating-a-python3-webserver-from-the-ground-up-4ff8933ecb96
