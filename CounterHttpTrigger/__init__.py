import os
import copy
import logging 

import azure.functions as func 

def __init__(self):
    self.connection_string = os.getenv("AzureCosmosDBConnectionString")
    self.table_name = "crc-db"

def fetchEntityData(self):
    from azure.data.tables import TableClient
    from azure.data.tables import UpdateMode
    from azure.core.exceptions import ResourceExistsError
    
    with TableClient.from_connection_string(self.connection_string, self.table_name) as table_client:
        entity = {
            "PartitionKey": "visitorpart",
            "RowKey": "visitors",
            "count": 400,
        }
        
        try:
            table_client.create_entity(entity = entity)
            table_entity = table_client.get_entity(partition_key=entity["PartitionKey"], row_key=entity["RowKey"])
        except ResourceExistsError:
            table_entity = table_client.get_entity(partition_key=entity["PartitionKey"], row_key=entity["RowKey"])
            table_entity["count"] += 1
            
        return table_entity
        
def main(req: func.HttpRequest) -> func.HttpResponse:
    table_entity = fetchEntityData()
    return func.HttpResponse(f"{table_entity['count']}")
    
if __name__ == "__main__":
    main()