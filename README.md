# MDMPy (Modular Download Manager)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/123ce4b041564c699671955db87819af)](https://www.codacy.com/app/mihaiblaga89/MDMPy?utm_source=github.com&utm_medium=referral&utm_content=mihaiblaga89/MDMPy&utm_campaign=badger)
[![Build Status](https://travis-ci.org/mihaiblaga89/MDMPy.svg?branch=master)](https://travis-ci.org/mihaiblaga89/MDMPy)
[![codecov](https://codecov.io/gh/mihaiblaga89/MDMPy/branch/master/graph/badge.svg)](https://codecov.io/gh/mihaiblaga89/MDMPy)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

![alt text](https://www.legocloud.org/wp-content/uploads/2017/03/MDMPy_logo.png "Logo")

# ---Work in progress---

### About
 I've been using SickRage and Radarr for movies and TV series automated downloader for some time now but there are no reliable download managers for books, games and music. (LazyLibrarian is buggy, Headphones does not allow track download and XDM is unmaintained and buggy)
 
 After the above mentioned issues, I've decided to write my own download manager. 
 
 **Python code ninjas beware, I'm using Python casually so most likely my code will drive you nuts in some cases**
 
 ### Tech
  - Python 2.7 
  - Cherrypy
  - Jinja2 template engine
  - peewee ORM
  - unittest
  - IGDB API
  - Spotify API
  - YouTube API
  - jQuery
  - Materializecss
  - FontAwesome
  - Modernizr
  - notificationFx
  - **CI with Travis-CI**
  - **Testing coverage with Codecov**

### Planned features
- [x] Music Search
- [x] Games Search
- [ ] Books Search
- [x] Torznab API Indexers support
- [ ] Torrent clients integration (Transmission, deluge, etc)
- [ ] Custom Indexer support
- [ ] Compatibility with Windows, UNIX, OSX
- [ ] Music Management
- [ ] Games Management
- [ ] Books Management
- [ ] Notifications (Slack, email, chrome, etc)

And many others...


### Installation

MDMPy requires Python 2.7 to run.

After you install Python:

```sh
$ git clone https://github.com/mihaiblaga89/MDMPy.git
$ cd MDMPy
$ python run.py
```

After it starts open your browser and point it to
```sh
http://127.0.0.1:3005/
```
I haven't done any testing regarding this on other machines than my laptop, so beware.

### Development

Want to contribute? Great, make a pull request!

License
----

![alt text](https://m7i.org/include/images/gpl-v3-logo.png "License")

Links
----

[LegoCloud](https://www.legocloud.org)

