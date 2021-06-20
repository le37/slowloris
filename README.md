# Slowloris

A simple pure Python3 [Slowloris](https://en.wikipedia.org/wiki/Slowloris_(computer_security)) implementation for educational purposes. Includes Docker files for building demonstration targets.

Related CVE: [CVE-2007-6750](https://www.cvedetails.com/cve/CVE-2007-6750/)

## Usage

    python3 slowloris.py {HOST} {PORT} {NUMBER_OF_CONNECTIONS}

e.g.

    python3 slowloris.py localhost 8080 1000

## Build Targets (Optional)

Two Docker files are included to build demonstration targets:
- Apache latest (quick to build but less vulnerable) 
- Apache 2.2.14 (slower to build but more vulnerable)

**Step 1**

Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop)

**Step 2**

To build latest:

    cd targets/latest

    docker build -t apache-latest .

    docker run -dit --name slowloris-target -p 8080:80 apache-latest

To build 2.2.14:

    cd targets/2.2.14

    docker build -t apache-2.2.14 .

    docker run -dit --name slowloris-target -p 8080:80 apache-2.2.14

**Step 3**

Test the target is up and running by visiting http://localhost:8080 in your browser

