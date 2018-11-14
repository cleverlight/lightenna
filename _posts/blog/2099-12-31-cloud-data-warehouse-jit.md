---
layout: single
title: Cloud data warehouse, just-in-time
description: Gone are the days when you needed a massive online database 24/7 for analytics 
tags: front tech consulting
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## Getting data out
+ Export
    + CSV export
    + JDBC (Tableau integration)
    + AWS Athena ODBC driver (PowerBI integration)


## Lock-in
+ Lock-in
    + Athena is Presto (open-source), so we could stand-up our own cluster in the medium-term.
+ Lift-and-shift

There's no need to migrate servers in the future, only send the data somewhere else.
If you move in the future, only your investment in setting up the infrastructure and writing custom queries is lost.


## Data warehouse products
There are a variety of cloud-based data warehouse tools.  Each has compute and storage costs associated.  The ones listed below are managed-infrastructure (SaaS) products, meaning that you don't have to invest time in specifically creating, say, a RedShift cluster.


## Sending data to the warehouse
The data is stored in a collection of independent databases.  It needs to be extracted and sent to the data warehouse.  Depending on the type of product selected, it may also need transforming and loading into the warehouse.


### AWS Athena
+ Compute
    + $5 for a 1TB-data-parsed query
+ Storage
    + 1TB storage $24/month
    + Data into S3, $0
+ Authentication
    + AWS Cognito
    + AWS IAM 


### Snowflake
+ Compute
     + $3.7 per hour per unit
+ Storage costs
    + 1TB storage $40/month on-demand, $23/month if up-front
+ Authentication
    + Easy AzureAD integration, Snowflake listed as 'gallery' application


## Returning query results
+ Several ways to get query results out
+ CSV download
+ JDBC/ODBC connection from a client


### Future thinking
+ Is it worth wrapping the query interface?
    + Abstract the underlying data warehouse technology
        + Look at Athena/Snowflake interface.  How rich is the UI?
        + Look at the API.  How much can we do with it.
    + Implement logging independently
    + Implement SSO

