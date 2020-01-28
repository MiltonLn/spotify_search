# Spotify Search

A Toy Project to show how powerfull is `ipdb` as a debugger.

This was used as a Live Demo for my talk [Debugging: A Senior's Skill](https://2020.pycon.co/en/talks/22/) given at
PyCon Colombia 2020


## Installation

* Clone the repository
* Create a virtualenv
* Run `pip install -r requirements.txt` to install the dependencies
* Create a file `.env` in the project's root duplicating `.env.example` and set your `SPOTIFY_AUTH_TOKEN`
* You can get your auth token from [this url](https://developer.spotify.com/console/get-search-item/) by clicking *GET TOKEN* (No special scope needed)
* Run `flask run`