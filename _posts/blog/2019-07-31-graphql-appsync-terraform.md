---
layout: single
title: GraphQL using AWS AppSync
description: An AppSync GraphQL example, automatically provisioned with Terraform
tags: front tobecontinued tech devops
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

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

Finally we want a top-level schema to tell GraphQL about all these bits:
```
schema {
    query: Query
    mutation: Mutation
    subscription: Subscription
}
```

## Terraform
Next we're going to need some Terraform code to provision it.  First we create an AppSync API:
```
provider "aws" {
  region = "eu-west-1"
  alias = "ireland"
}
resource "aws_appsync_graphql_api" "grapple" {
  name = "grapple-${terraform.workspace}-${var.project_name}"
  authentication_type = "API_KEY"
  provider = "aws.ireland"
}
```
At the time of writing AppSync wasn't available in eu-west-2 (London) so we're using eu-west-1 (Ireland).  Now we need an API key to access it:
```
resource "aws_appsync_api_key" "api_key" {
  api_id = "${aws_appsync_graphql_api.grapple.id}"
  # API keys have a maximum validity period of 365 days
  expires = "2020-01-04T13:00:00Z"
  provider = "aws.ireland"
}
```

Once we've got an API, we can upload our new schema to it:
```
# upload schema from template file
data "template_file" "grapple_schema" {
  template = "${file("${path.root}/../../appsync/grapple/schema.graphql")}"
}
resource "null_resource" "grapple_upload_schema" {
  provisioner "local-exec" {
    command = "aws appsync start-schema-creation --region ${var.aws_region_appsync} --api-id ${aws_appsync_graphql_api.grapple.id} --definition '${data.template_file.grapple_schema.rendered}'"
  }
  # trigger based on changes to the schema
  triggers = {
    file_changes = "${md5(data.template_file.grapple_schema.rendered )}"
  }
  depends_on = ["aws_appsync_graphql_api.grapple"]
}
```
The use of a trigger here means that whenever our API file changes locally, it will be re-uploaded to AWS in the next `terraform apply`.

## To be continued
If you want to see more of this kind of material, just [drop me an email](/contact) and I'd be happy to expand it here.

<!---
## Open source
All the code here, both application source and infrastructure-as-code, is available [open-source in the repo](https://github.com/lightenna/react-appsync-terraform-example).
-->
