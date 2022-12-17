import logging
import json
import azure.functions as func
import os

def main(req: func.HttpRequest, doc:func.DocumentList) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    #logging.info(doc[0].to_json())
    
    try:
        count = doc[0]["count"]        
    except IndexError as e:
        count = 0
    
    countJSON = {
        "count": count
    }
    
    countJSON = json.dumps(countJSON)
    
    return func.HttpResponse(
        countJSON.json(),
        status_code=200
    )