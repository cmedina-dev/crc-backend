# Cloud Resume Challenge - Backend
* To visit the full website, [click here](https://cjmedina.dev/).
* For the frontend portion of the challenge, [click here](https://github.com/cjmedina95/crc-frontend).

## Table of contents
1. [Overview](#Overview)
2. [CosmosDB](#CosmosDB)
3. [Python API](#PythonAPI)
4. [Cypress](#Cypress)
5. [Terraform](#Terraform)
6. [CI/CD](#CI/CD)

## Overview

The Cloud Resume Challenge is composed of 16 total steps. 
The backend portion of the challenge requires development of an API, which can be used to retrieve and increment the number of visitors to the site.

The challenge was completed using Azure infrastructure. Visitor counts were stored in a CosmosDB table entity.
An API calls an HTTP-triggered Azure function which both retrieves and increases the visitor count.

Cypress tests were used to verify end-to-end connection to the API. 
Terraform was used to both configure and deploy the required infrastructure for the challenge.

Finally, code changes to the API are entirely handled by CI/CD, which is managed by GitHub Actions.
