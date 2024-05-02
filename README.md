# BCRM ETL service SSOT
![Powered by](https://img.shields.io/badge/Powered%20by-Mulesoft-535597.svg)
  ![Unit test](https://raw.githubusercontent.com/btfacrm/badges/main/bcrm-etl-service/bcrm-etl-service-ut.svg)
  ![Code coverage](https://raw.githubusercontent.com/btfacrm/badges/main/bcrm-etl-service/bcrm-etl-service-cc.svg)
  ![Build](https://github.com/btfacrm/bcrm-etl-service/actions/workflows/build.yml/badge.svg)
  ![Build job](https://raw.githubusercontent.com/btfacrm/badges/main/bcrm-etl-service/bcrm-etl-service-wf.svg)
  ![Release](https://raw.githubusercontent.com/btfacrm/badges/main/bcrm-etl-service/bcrm-etl-service-re.svg)
  ![dev version](https://raw.githubusercontent.com/btfacrm/badges/main/bcrm-etl-service/bcrm-etl-service-dev.svg)
  ![prd version](https://raw.githubusercontent.com/btfacrm/badges/main/bcrm-etl-service/bcrm-etl-service-prd.svg)
<br>

SSOT ETL service for Salesforce Integration

## Table of contents
1. [Description](#description) 
1. [Configuration](#configuration)

## Description  
SSOT ETL service for Salesforce Integration. The next diagram shows the high level architecture of the process:

<br>

![architecture](https://raw.githubusercontent.com/btfacrm/bcrm-salesforce-sapi/main/docs/architecture.png)
 
## Configuration

The next properties must be provided to run the service:

| Property                     | Description               |
| ---------------------------- | ------------------------- |
| mssql.host                   | Microsoft Sql Server Host |
| mssql.port                   | Microsoft Sql Server Port |
| mssql.user                   | Microsoft Sql Server User |
| mssql.password               | Microsoft Sql Server Password |
| mssql.database               | Microsoft Sql Server Database Name |
| api.id                       | API Manager instance id |
| jks.path                     | Path to the keystore for https |
| jks.keypassword              | Password to open the keystore for https |
| jks.alias                    | Name of the certificate in the keystore for https |
| service.host                 | BCRM Salesforce System API host |
| service.clientid             | BCRM Salesforce System API client-id |
| service.clientsecret         | BCRM Salesforce System API client-secret |
| logapplication               | Logging level for application messages |
| logconnectors                | Logging level for connectors |
| logroot                      | Logging level for root |
| env                          | Name of the environment where the application is running |

<br>

---

- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Mulesoft Documentation](https://docs.mulesoft.com/general/)