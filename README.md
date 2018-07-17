# OnionSpider
by Michael Assyag

Asynchronous deep web crawler built in Python.

## Getting Started

The crawler runs only on console at the moment.

Important: I haven't had the time to make the requirements.txt to install properly. I looked it up and found that many people had the strugle for installing internal dependencies via 'pip3 install -r requirements.txt'

### Prerequisites

You need to have [Tor Project](https://www.torproject.org/index.html.en) installed and running

```
apt install tor
```

### Installing

First of all we start by installing the requirements.txt

```
pip3 install -r requirements.txt
```

And now because of the requirements.txt internal dependency issue, we reinstall requests and Pysocks

```
pip3 install requests==2.11.1
pip3 install pysocks
```

## Deployment

After finished installing we can run the program

```
    python3 main.py
```

## Docker

The repo has also a Dockerfile for creating Docker image but the docker can't run because of the dependencies issues

Nevertheless, we can build the docker image by executing the following command
```
     docker build --rm=true -t spider-docker .
```

And running our docker using this:
```
    run -it -p 9050:9050 -d onion-docker:latest
```

### Built with

* [requests](http://docs.python-requests.org/en/master/) - The HTTP package
* [tinyDB](http://tinydb.readthedocs.io/en/latest/) - Used for creating fast DB for storing the pastes

