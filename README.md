# Google Custom Search Tool
## Basic files
* app.py: main program
* list.csv: city list
* support_organizations.csv: support organization list
* google_search_results.csv: url of support organization list by google search

## Search Standard
* First one in google search result with query(city name + support organization name)

## Description
* This tool can get website url from Google Custom Search API(from GCP)

## Getting Started
### Dependencies
* Windows/Linux OS, Python(version should be 3.8?+).

### Main Packages and APIs
1. requests
2. difflib
3. google custom search api

### 0. Pre-work
1. Get a account of Google Cloud Platform
2. Activate Custom Search API and setup api key
3. Setup Custom Search Engine（CSE）: get cx id
4. Download this project and go to the folder with CMD

- refer https://qiita.com/zak_y/items/42ca0f1ea14f7046108c

### 1. Install Packages
```
pip install -r requirements.txt
```

or you can just pickup packages you need


### 2. Set parameters
api_key = "YOUR_API_KEY"
cx = "YOUR_SEARCH_ENGINE_ID"

### 3. python script.py
```
python app.py
```

## Other
### Update requirements.txt
```
pip freeze > requirements.txt
```