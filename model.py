import requests
def getImageUrlFrom(query):
    giphy_request_link = "https://api.giphy.com/v1/gifs/search?api_key=dIm2FEAJQKeOTxVk8bZSbQK2El4VZfUh&q=" + query + "&limit=25&offset=0&rating=g&lang=en"
    response = requests.get(giphy_request_link).json()
    return response["data"][0]["images"]["fixed_height"]["url"]