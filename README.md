# Cloud Resume Challenge - Backend
* To visit the full website, [click here](https://cjmedina.dev/).
* For the frontend portion of the challenge, [click here](https://github.com/cjmedina95/crc-frontend).

## Table of contents
1. [Overview](#overview)
2. [CosmosDB](#cosmosdb)
3. [Python API](#python-api)
4. [Cypress](#cypress)
5. [Terraform](#terraform)
6. [GitHub Actions](#github-actions)
7. [Helpful links](#helpful-links)

## Overview

The Cloud Resume Challenge is composed of 16 total steps. 
The backend portion of the challenge requires development of an API, which can be used to retrieve and increment the number of visitors to the site.

The challenge was completed using Azure infrastructure. Visitor counts were stored in a CosmosDB table entity.
An API calls an HTTP-triggered Azure function which both retrieves and increases the visitor count.

Cypress tests were used to verify end-to-end connection to the API. 
Terraform was used to both configure and deploy the required infrastructure for the challenge.

Finally, code changes to the API are entirely handled by CI/CD, which is managed by GitHub Actions.

## CosmosDB

![CosmosDB Table Entity](https://i.imgur.com/HeOYcLe.png)

While a table entity was used for this project, a second approach could have involved using CosmosDB NoSQL. Both are completely viable methods.

The infrastructure, specifically the Terraform code, was created with [Hashicorp's reference documentation](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/cosmosdb_table). Some notable changes from the reference included enabling Serverless and enabling Table functionality, which aren't shown in the reference:

```
  capabilities {
	name = "EnableServerless"
  }
  
  capabilities {
	name = "EnableTable"
  }
```

## Python API

The API was deployed through an Azure Function App. The Function App requires several key configuration components. The two important ones are the connection strings, which connect AppInsights and CosmosDB to the Function App, allowing these resources to talk to each other.

![Function App Configuration](https://i.imgur.com/oVOgC0Y.png)

The Python function itself involves two files: the [\_\_init\_\_.py file](https://github.com/cjmedina95/crc-backend/blob/main/CounterHttpTrigger/__init__.py) and a [function.json file](https://github.com/cjmedina95/crc-backend/blob/main/CounterHttpTrigger/function.json) for configuration.

Importantly, the Python code retrieves the aforementioned connection string for use in the code with the following line: `self.connection_string = os.getenv("AzureCosmosDBConnectionString")`

After retrieving and storing the variables, if the table entity doesn't already exist, the code creates the entity with a default visitor count value. Otherwise the code increments it if the entity already exists. Once fetched, the function returns the value to be used on the front end.

## Cypress

The Cypress test is fairly simple since the API is also simplistic. The test verifies whether the API returns an HTTP response code of 200, indicating the API is responsive and available.

## Terraform

The Terraform code was created by hand, almost exclusively using Hashicorp's reference documentation. Notably, while tools such as Azure Terrafy exist to import existing Azure infrastructure into Terraform, it felt as though this would detract from the challenge's purpose and were left unused.

In order to tear down and redeploy the entire Azure infrastructure stack from scratch, some parts of the Terraform stack had to be loaded in a specific order. Notably, the Azure Key Vault certificate:
```
resource "azurerm_key_vault_certificate" "crc_cert" {
  name         = "crc-tf-cert2"
  key_vault_id = azurerm_key_vault.crc_keyvault.id

  certificate {
    contents = filebase64("crcresume-keyvault-cjmedina-dev-20221115.pfx")
  }

  depends_on = [azurerm_key_vault_access_policy.crc_keyvault_ap_cdn, azurerm_key_vault_access_policy.crc_keyvault_ap_user]
}
```

One of the benefits of deploying the infrastructure by hand was being able to reference the configurations needed while writing the code.

## GitHub Actions

Microsoft wrote an excellent guide on setting up GitHub Actions for Azure Function Apps. Deploying the API was almost exclusively done using their [reference documentation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions?tabs=python).

The Cypress test sets up the npm package, then installs the Cypress dependency to run correctly. This is done in the following code block:
```
      - name: setup NPM package
        run: npm init -y && npm install
        
      - name: Cypress run
        uses: cypress-io/github-action@v4
        with:
          build: npm i -D cypress  
```

Combining these two allowed for code changes to be pushed to the GitHub repository, enabling CI/CD.

## Helpful Links

* Azure CosmosDB Tables: https://learn.microsoft.com/en-us/python/api/overview/azure/data-tables-readme?view=azure-python
* Azure CosmosDB NoSQL: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-python?tabs=azure-portal%2Cwindows%2Csync#get-an-item
* Azure Functions Python: https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level&pivots=python-mode-configuration
* Deploying Python code to Azure: https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration
