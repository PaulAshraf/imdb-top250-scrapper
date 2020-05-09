# imdb-top250-scrapper

Python &amp; Selenium scrapper that produces a json with the full data about the IMDb's top 250 movies. Additional data is collected from TMDB free API.

## installation

### Selenium:

Download the chromedriver from [here](https://chromedriver.chromium.org/downloads). Download the version that matches your chrome version.

Extract the zip file and make sure that `chromedriver.exe` is in the root directory.

### TMDB API:

You need to get an API key in order to make the requests to the TMDB API. Don't worry it's free!

1. Create an account from [here](https://www.themoviedb.org/account/signup?language=en-US)

2. Get an API key [here](https://www.themoviedb.org/settings/api)

3. Add the new API key to your enviroment variables.

```cmd
set TMDB_API_KEY= <your-new-api-key>
```

Use an echo command to make sure it is set up.

```cmd
echo %TMDB_API_KEY%
```

## Running 

Only thing left is to run the script.

```cmd
python top250.py
```

You should see `list.json` created in the root directory.
