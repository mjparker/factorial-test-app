## Overview
This is a single webpage application which accepts a single input and calculates the [factorial](https://en.wikipedia.org/wiki/Factorial) of that input. The app is seeded with various bugs and was designed for use in interviewing QA and software test candidates. 

There are various bugs throughout the app, of all shapes and sizes. 'Bug' is defined rather loosely here. It could be as small as a typo to as big as an actual functional issue. 

A version of this app is available for demo at https://qa-interview-app.herokuapp.com/

## Setup

### Preconditions:
* Python3
* Pip3

### To run this file locally:
1. Edit `factorial.py`. Change the `app.run` line to: 
`app.run(host='0.0.0.0', port=6464, debug= True)`

2. `pip install -r requirements.txt`

3. Run `python factorial.py`, then point your browser to `localhost:6464`.

---

### Credit 
This is a heavily modified fork of [qa-interview-web-application](https://github.com/qxf2/qa-interview-web-application). I wrote entirely new HTML/CSS, updated to Bootstrap4, added a few more bugs, and removed references to solutions.
