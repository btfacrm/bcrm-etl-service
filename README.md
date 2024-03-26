# BCRM ETL service SSOT
![Powered by](https://img.shields.io/badge/Powered%20by-Mulesoft-535597.svg)
  ![Unit test](https://gist.githubusercontent.com/jpontdia/2f22ca2ddf1ba473d6e2cff61cc2fba9/raw/bcrm-salesforce-sapi-fips-ut.svg)
  ![Code coverage](https://gist.githubusercontent.com/jpontdia/2f22ca2ddf1ba473d6e2cff61cc2fba9/raw/bcrm-etl-service-cc.svg)
  ![Build](https://github.com/btfacrm/bcrm-etl-service/actions/workflows/build.yml/badge.svg)
  ![Build job](https://gist.githubusercontent.com/jpontdia/2f22ca2ddf1ba473d6e2cff61cc2fba9/raw/bcrm-etl-service-wf.svg)
  ![Release](https://gist.githubusercontent.com/jpontdia/2f22ca2ddf1ba473d6e2cff61cc2fba9/raw/bcrm-etl-service-re.svg)
  ![dev version](https://gist.githubusercontent.com/jpontdia/2f22ca2ddf1ba473d6e2cff61cc2fba9/raw/bcrm-etl-service-dev.svg)
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
| sqlserver.host               | Keystore with the cetificate to connect with Salesforce. |
| api.id                       | API Manager instance id |
| logapplication               | Logging level for application messages |
| logconnectors                | Logging level for connectors |
| logroot                      | Logging level for root |
| env                          | Name of the environment where the application is running |

<br>

---

- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Mulesoft Documentation](https://docs.mulesoft.com/general/)