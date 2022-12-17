import logging
import azure.functions as func
import json
import uuid
from urllib.request import urlopen
from urllib.error import HTTPError

def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    URL = "https://crc-counterapp.azurewebsites.net/api/counter/get"

    try:
        res = urlopen(URL)
    except HTTPError as e:
        return func.HttpResponse(f"An unexpected error accessing the API occurred. Error: {e}")

    #logging.info('Requested URL opened.')

    #data = json.loads(res.read())
    #logging.info(data)

    #new_doc = func.DocumentList()

    #if not data['count']:
    #    data['count'] = 0

    #new_data = {
    #    "id": "VisitCount",
    #    "count": data['count'] + 1
    #}
    
    #logging.info('Appending data...')
    
    #new_doc.append(func.Document.from_dict(new_data))
    #doc.set(new_doc)

    return func.HttpResponse("HTTP triggered function executed successfully.", status_code=200)
