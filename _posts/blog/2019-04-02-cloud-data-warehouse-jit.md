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

I never imagined that I'd get so excited about the ability to turn something off.

Cloud is often sold on the basis of its flexibility and scalability, and there are some good savings.
Auto-scaling gives many smaller web services (like [some of mine](https://poc.cloudlog.live/)) a good opportunity to avoid paying for a lot of servers provisioned only to cope with intermittent (and all too rare) busy periods.

Perhaps more significantly, Cloud is making top-tier enterprise-grade services available to smaller organisations.


## On, but mainly off
Where before you'd have to set up a data warehouse to run 24/7 - or rather you'd at least have to license it to run 24/7 even if you only used it occasionally - you can now run one only when you need it.
By exporting your data to a (well-secured) AWS S3 bucket or Azure Blob Storage account, you can turn on your data warehouse capability for a few hours or even minutes, then turn it off.
Best of all, you only pay for it when you're using it.


## $10,000/year now $5/hour
If I want to dynamically sync my local online transactions processing (OLTP) DB system with my new Cloud data warehouse, which is an online analytical processing (OLAP) system, I can.  There are some great change-data capture (CDC) tools, but I've traditionally avoided them due to the high barriers to adoption.  Now with Amazon Marketplace, I could instantiate a CDC appliance (HVR) for a few hours and reduce the cost of my experimentation to a few dollars.

## Exchanging numbers
+ CSV export
+ JDBC connections (e.g. Tableau integration)
+ AWS Athena ODBC driver (e.g. PowerBI integration)

Dropping data in and querying data out of a Cloud Data Warehouse (CDW) are both very flexible operations.

Snowflake and AWS Athena both ingest structured or semi-structured data in columnar formats (such as Apache Parquet) or good old-fashioned CSVs.  Getting data out is just as easy, although you can hit some largely-surmountable performance issues if using more advanced query clients (like PowerBI, Looker or Tableau).

## Lock-in
+ Lock-in
+ Lift-and-shift

I'm often mindful of vendor lock-in, but the data can be readily re-ingest into another service and the queries are broadly standard SQL.  AWS Athena is based on Presto (open-source), so standing-up our own cluster is an option.

There's no real need to migrate servers in the future, only send the data somewhere else.
If you eventually decide to move, only your investment in setting up the infrastructure and writing custom queries is lost.


## Data warehouse products
There are a variety of cloud-based data warehouse tools.  Each has compute and storage costs associated.  The ones listed below are managed-infrastructure (SaaS) products, meaning that you don't have to invest time in specifically creating, say, an AWS RedShift cluster.  You just put your data somewhere, then query it (although Snowflake does have an additional ingest stage and Athena requires configuring AWS Glue).


## Sending data to the warehouse
OLTP data is stored in a collection of independent databases (Finance, HR, ERP, Web app DBs, legacy system, phone and server logs etc.).  It needs to be extracted and sent to the data warehouse.  Depending on the type of product selected, it may also need transforming and loading into the warehouse.

The advantage with a Data Lake approach is that this data can typically be ingested untransformed, then later processed when a use case (and associated business case/value propositon) has been discovered. 
Given that the thrust of this project is minimising upfront investment and reacting to future need with agility, building out a Cloud Data Lake is a good first step for many organisations.


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
+ Plain CSV download
+ JDBC/ODBC connection from a client

Rich clients (like PowerBI) can, behind the scenes, construct complex and verbose queries.  Getting those resolved in a useful timeframe requires being pragmatic about the volume of data to be processed or scaling the cloud data warehouse.

Scalability is key.  If you've got a complex PowerBI report that requires serious processing, you can now throw a 100+ core machine at it for a few minutes, then just shut it down when you're done.

