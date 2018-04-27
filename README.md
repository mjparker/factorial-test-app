## Overview
This is a single webpage application which accepts a single input and calculates the [factorial](https://en.wikipedia.org/wiki/Factorial) of that input. The app is seeded with various bugs and was designed for use in interviewing QA and software test candidates. 

There are various bugs throughout the app, of all shapes and sizes. 'Bug' is defined rather loosely here. It could be as small as a typo to as big as an actual functional issue. 

A version of this app is available for demo at https://qa-interview-app.herokuapp.com/

### Bugs include but are not limited to:
* Created a /secret page. You can find it only by finding the secret link. The easiest way to find it is by looking in the page source code. The secret page takes you to the source code.
* Copyright is 2018-2018
* Page title has a typo "Factoriall"
* The Enter button doesn't run the app correctly and refreshses the page
* The URLs for T&C and Privacy are wrong
* Rick Roll in the copyright
* Factorial has a limit
* The console log is worded all dumb "Hello! I am in the done part the ajax call"
* A bad link that leads to a 404
* Infinite loop when submiting a negative number

## Setup

### Preconditions:
* Python3
* Pip3

### To run this file locally:
1. Edit `factorial.py`. Change the `app.run` line to: 
`app.run(host='0.0.0.0', port=6464, debug= True)`

2. `pip install requirements.txt`

3. Run `python factorial.py`, then point your browser to `localhost:6464`.

---

### Secret Code

If you made it to this page from the secret link, pat yourself on the back and email me the passcode:
`CellarDoor`

---

### Credit 
This is a fork off the [qa-interview-web-application repo](https://github.com/qxf2/qa-interview-web-application) by the fine folks at [Qxf2 Sevices](https://www.qxf2.com/?utm_source=qa-interview&utm_medium=click&utm_campaign=From%20QA%20Interview). I've tweaked the source to update to Bootstrap4, add a few more bugs, and remove references that might lead the QA candidate to the solutions.