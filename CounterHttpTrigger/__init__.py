import logging
import json
import azure.functions as func
import os

def main(req: func.HttpRequest, doc:func.DocumentList) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    #logging.info(doc[0].to_json())
    
    if doc[0]["count"]:
        count = doc[0]["count"]
    else:
        count = 0
    
    return func.HttpResponse(
        str(count),
        status_code=200
    )