Visualize the Universe - CS 594 Final Project Website
=====================================================

This folder contains the web application detailing
the experiment and results for this project. It's a
node.js application that uses the Express framework,
so you'll need node.js and npm installed to run it.
Assuming you have those, running ```npm install```
in this directory should grab all the dependencies.

Then to run it:

```sh
$ PORT=8080 npm start
```

You can omit the port, and by default it will run on 3000.
If you want it on port 80, you'll probably need to run it
as root:

```sh
$ sudo PORT=80 npm start
```