---
layout: single
title: 
description: A complete React-GraphQL-AppSync example, automatically provisioned with a single Terraform call
tags: front tech devops
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## 
This post is about a few new technologies that are gaining traction in the web sphere.  All the code here, both application source and infrastructure-as-code, is available [open-source in the reactappsyncterra repo](https://github.com/lightenna/react-appsync-terraform-example).

## March of the titan
AWS continues its march across the Infrastructure-as-a-Service (Iaas) world with new services coming out each month.  When evaluating these services, Engineers and Architects are called to make difficult decisions that balance vendor lock-in, standards, likely future adoption, maintainability and cost.

## Function over form
Crucially the need to deliver a product, quickly, reliably and scalably trumps the academic pursuit of the perfect tech or new-phoric love of the latest trend.  If there's an AWS service - read global, pay-as-you-go, massively scalable, low barrier to entry  -  that helps you to do what you're trying to do online, then surely it's worth evaluating.

## Embrace the new
AppSync promises to do exactly that.  Coupled with some good infrastructure-as-code, it reduces the complexity associated with setting up a GraphQL API and backing datastore to a few well ordered lines of Terraform code.

## AppSync
### GraphQL API
Let's start with a basic type in GraphQL
```
# Docs
type Doc {
    created: Int!
    creatorAccountId: String!
    id: ID!
    body: String!
}
```
then a connection to read streams of them and some CRUD param lists
```
type DocConnection {
    items: [Doc]
    nextToken: String
}

input CreateDocInput {
    creatorAccountId: String!
    body: String!
}

input UpdateDocInput {
    id: ID!
    body: String
}

input DeleteDocInput {
    id: ID!
}
```

We need a query to read the latest docs, mutations to update them and subscriptions to listen for changes:
```
type Query {
    getLatestDocs(
        creatorAccountId: String,
        limit: Int,
        nextToken: String
    ): DocConnection
}

type Mutation {
    createDoc(input: CreateDocInput!): Doc
    updateDoc(input: UpdateDocInput!): Doc
    deleteDoc(input: DeleteDocInput!): Doc
}

type Subscription {
    onCreateDoc(creatorAccountId: String!): Doc
    @aws_subscribe(mutations: ["createDoc"])
    onUpdateDoc(id: ID, body: String): Doc
    @aws_subscribe(mutations: ["updateDoc"])
    onDeleteDoc(id: ID, body: String): Doc
    @aws_subscribe(mutations: ["deleteDoc"])
}
```

Finally we want a top-level schema to tell GraphQL about all these bits
```
schema {
    query: Query
    mutation: Mutation
    subscription: Subscription
}
```