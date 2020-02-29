# Jammer Backend (RESTful with [Eve][eve])

This is the seed and prototype of REST-ful backend for Jammer.

This is an [Eve][eve] app using a standard image for Mongo container and a morph of [Alex Pankov's Eve Dockerfile][alexdock] for its own box.

[eve]: http://docs.python-eve.org/en/latest/index.html
[alexdock]: https://github.com/alekspankov/docker-eve-python

### Prerequisites

- [Docker](https://docs.docker.com/) 
- [Docker Compose](https://docs.docker.com/compose/)

Both can be installed on Ubuntu by the included [startmeup script](./startmeup-ubuntu.bash).

## RUN

The repo includes **docker-compose.yml**. To use it run:

```bash
docker-compose up
```
