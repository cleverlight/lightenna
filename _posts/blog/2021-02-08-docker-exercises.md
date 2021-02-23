---
layout: single
title: Docker exercises
description: Containers allow us to run isolated processes in a controlled security context.  Try out these exercises to hone your skills!
tags: tech devops docker
toc: true
header:
    overlay_image: /assets/images/techupdate_25318_1920x.jpg
    small_image: /assets/images/techupdate_25318_640x.jpg
---

## Exercise: containerising a Node.js webserver
* Create a simple Node.js web server
    * Create `index.js` to expose a web server on port 3030
    ```
    // content of index.js
    const http = require('http');
    const port = 3030;
    const requestHandler = (request, response) => {
        console.log(request.url);
        response.end('Hello Node.js Server!');
    };
    const server = http.createServer(requestHandler);
    server.listen(port, (err) => {
        if (err) { return console.log('something bad happened', err); }
        console.log(`server is listening on ${port}`);
    });
    ```      
    * Test locally
        * Install `package.json` using `npm install`
        * Start using `npm start`
        * `curl localhost:3030` or open in local browser
        * Terminate local service after testing
* Write a `Dockerfile` to:
    * Use a Node.js base image
    * Copy package.json over to image and `npm install` at build time
    * Run `npm start` at container start time
    * `EXPOSE` port 3030 from the container
* Instantiate this image and connect to your container
    * Verify that you can connect to the web service from within the container
    * Use `docker container ls` to show exposed ports for running containers
    * Verify that you can connect to the web service from outside the container
        * e.g. on host machine
    * Capture all your commands in scripts (good IAC practice)
* Run your container as a non-root user, e.g. user `1000`
    * Modify your container to run all processes as user `1000`
    * Set appropriate file permissions to enable access to your non-root user

{% if include.pres %}Note: {% endif %}
The [solution to the 'containerising' exercise](https://github.com/lightenna/devops-workstream/tree/master/docker/tutorial/01-dockerfile-build) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

## Exercise: augment existing Dockerfile
* Create a `Dockerfile` that augments the existing NGINX Dockerfile
    * Use the `FROM` keyword to reference the [latest nginx](https://hub.docker.com/_/nginx)
* Install an additional package such as procps (for `ps` commands)
    * using the package manager built into your chosen distribution
* Copy a local nginx.conf file into your container
    * You might base your configuration on a simplified version of this [Nginx Example Configuration](https://www.nginx.com/resources/wiki/start/topics/examples/full/)
        * Alternatively see solution for sample config
* Copy a local website into your container
    * A single `index.html` file will suffice, but you can enrich it if you'd like
* Run NGINX as a non-root user, e.g. user `1000`
    * Hint: you'll need to direct NGINX to use /tmp subfolder for all writable outputs

{% if include.pres %}Note: {% endif %}
The [solution to the 'augment' exercise](https://github.com/lightenna/devops-workstream/tree/master/docker/tutorial/02-dockerfile-augment) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

## Exercise: environment variables
* Build on the ['containerising' exercise](https://github.com/lightenna/devops-workstream/tree/master/docker/tutorial/01-dockerfile-build) to pass in a `PORT` environment variable
    * Extend the Node.js code to look for the `PORT` environment variable
        * Add to package.json
    ```
    ...
        "main": "src/index.js",
        "dependencies": {
        "dotenv": "^8.2.0",
        "nodemon": "^2.0.1"
        },
    ...
    ```
    * Modify the `index.js` to accept an environment variable, but fall back to a default if absent
    ```
    ...
        const http = require('http');
        const env = require('process').env;
        require('dotenv').config();
        const port = env.PORT || 8080;
    ...
    ```
* Initially don't set a environment value for port
    * Test to see if it's exposed on 8080, both in the container and to the host
* Set a value for the environment variable in `Dockerfile`
    * Connect into the machine and `echo $PORT` to see environment value
    * Retest access on 8080 and your new value, both in the container and to the host
        * Hint: use `docker container ls` to see what your container exposes by default
* Set a value for `PORT` in the `docker run` command that you use to instantiate your container
    * Retest access again

{% if include.pres %}Note: {% endif %}
The [solution to the 'environment variables' exercise](https://github.com/lightenna/devops-workstream/tree/master/docker/tutorial/03-dockerfile-environment-variables) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

## Exercise: volumes
* Build on the ['augment' exercise](https://github.com/lightenna/devops-workstream/tree/master/docker/tutorial/02-dockerfile-augment) to share volumes into your container
    * Instead of using `COPY` to make a duplicate of your `nginx.conf`
        * mount the file as a volume
* Try modifying your config then restarting your container
    * Hint: you can use `docker logs <container_name>` to see start-up logs from NGINX
* Repeat this process for the local website you made previously
    * Instead of using `COPY` to make a duplicate of your local website
        * mount the directory as a volume
* Modify your local website and restart your container

{% if include.pres %}Note: {% endif %}
The [solution to the 'volumes' exercise](https://github.com/lightenna/devops-workstream/tree/master/docker/tutorial/04-dockerfile-volumes) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

## Exercise: docker-compose
* Write a `docker-compose.yml` file to bring up an ELK stack, using container images:
    * Elasticsearch `docker.elastic.co/elasticsearch/elasticsearch:7.10.0`
    * Logstash `docker.elastic.co/logstash/logstash:7.10.0`
    * Kibana `docker.elastic.co/kibana/kibana:7.10.0`
* Bring your stack up using `docker-compose up`
    * You might choose to run that in a separate process (using `&`) to avoid blocking your command prompt
* Pass an environment variable to Elasticsearch:
    * `discovery.type=single-node`
* Expose port `9200` for Elasticsearch and `5601` for Kibana
    * Test internal (in-container) and external (on-guest) access to both services
* Ensure that Elasticsearch spins-up before Logstash and Kibana using the `depends_on` relationship

{% if include.pres %}Note: {% endif %}
The [solution to the 'docker-compose' exercise](https://github.com/lightenna/devops-workstream/tree/master/docker/tutorial/05-dockerfile-environment-variables) is available as part of our open-source [Devops-Workstream](https://github.com/lightenna/devops-workstream/).

---
