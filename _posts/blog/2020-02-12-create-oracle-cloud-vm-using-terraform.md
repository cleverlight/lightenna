---
layout: single
title: Create an Oracle Cloud VM (always free) instance using Terraform
description: Oracle Cloud is still something of the new kid on the block, but their always-free tier offers a great starting place for some automated cloud resources provisioned with Terraform
tags: tech devops remprov
toc: true
header:
    overlay_image: /assets/images/techupdate_25318_1920x.jpg
    small_image: /assets/images/techupdate_25318_640x.jpg
---

## Getting started
This is a short primer on using Terraform to provision and puppet resources in Oracle Cloud.

## Cloud credentials for Terraform
We need to give Terraform some credentials in order to provision resources in our Oracle Cloud:
```
provider "oci" {
  tenancy_ocid = var.tenancy_ocid
  user_ocid = var.user_ocid
  fingerprint = var.fingerprint
  private_key_path = var.private_key_path
  region = var.region
}
```

## Getting the basics up
Let's start with a VCN to contain it all:
```
resource "oci_core_vcn" "vcn" {
  cidr_block = "10.1.0.0/16"
  compartment_id = var.compartment_ocid
  display_name = "vcn-${var.hostname}"
  dns_label = "vcn${var.hostname}"
}
```

## Outbound access
Next we'll need an Internet gateway and routing table for external access:
```
resource "oci_core_internet_gateway" "internet_gateway" {
  compartment_id = var.compartment_ocid
  display_name = "ig-${var.hostname}"
  vcn_id = oci_core_vcn.vcn.id
}
```
```
resource "oci_core_default_route_table" "default_route_table" {
  manage_default_resource_id = oci_core_vcn.vcn.default_route_table_id
  display_name = "rt-${var.hostname}"

  route_rules {
    destination = "0.0.0.0/0"
    destination_type = "CIDR_BLOCK"
    network_entity_id = oci_core_internet_gateway.internet_gateway.id
  }
}
```
We'll also need to allow access out of our Network Security Group (see later):
```
resource "oci_core_network_security_group_security_rule" "nsg_outbound" {
  network_security_group_id = "${oci_core_network_security_group.nsg.id}"
  direction = "EGRESS"
  protocol = "all"
  description = "nsg-${var.hostname}-outbound"
  destination = "0.0.0.0/0"
  destination_type = "CIDR_BLOCK"
}
```

## Network
Create a subnet, but create an empty (secure) Default Security List so as not to accidentally expose any unmanaged ports:
```
resource "oci_core_subnet" "subnet" {
  availability_domain = data.oci_identity_availability_domain.ad.name
  cidr_block = "10.1.0.0/24"
  display_name = "subnet-${var.hostname}"
  dns_label = "subnet${var.hostname}"
  security_list_ids = [
    oci_core_security_list.empty_security_list.id]
  compartment_id = var.compartment_ocid
  vcn_id = oci_core_vcn.vcn.id
  route_table_id = oci_core_vcn.vcn.default_route_table_id
  dhcp_options_id = oci_core_vcn.vcn.default_dhcp_options_id
}
```
```
# create empty security list to avoid using 'default' with open 22
resource "oci_core_security_list" "empty_security_list" {
  compartment_id = var.compartment_ocid
  vcn_id = oci_core_vcn.vcn.id
  display_name = "seclist-${var.hostname}"
}
```

## Inbound access
Next we create a Network Security Group that explicit allows only SSH in:
```
resource "oci_core_network_security_group" "nsg" {
  compartment_id = var.compartment_ocid
  vcn_id = oci_core_vcn.vcn.id
  display_name = "nsg-${var.hostname}"
}
```
```
resource "oci_core_network_security_group_security_rule" "nsg_inbound_ssh" {
  network_security_group_id = "${oci_core_network_security_group.nsg.id}"
  direction = "INGRESS"
  protocol = "6" # TCP
  description = "nsg-${var.hostname}-inbound-ssh"
  source = "${data.dns_a_record_set.bastion-host.addrs[0]}/32"
  source_type = "CIDR_BLOCK"
  destination = "${module.vminst.public_ip}/32"
  destination_type = "CIDR_BLOCK"
  tcp_options {
    destination_port_range {
      min = 22
      max = 22
    }
  }
}
```

## VM instance
Finally we're in a position to create our VM instance.  As with all the Clouds (Azure, AWS, DigitalOcean) supported by `devops-workstream`, we can use the familiar format plus a view dedicated Oracle parameters:
```
module "vminst" {
  source = "../../shared/create-oraclecloud-vm-puppetmless"
  region = var.region
  region_ad = var.region_ad
  compartment_ocid = var.compartment_ocid
  project = var.project
  account = var.account
  hostname = var.hostname
  host_domain = var.host_domain
  # install Oracle Linux 7, using image in uk-london-1
  host_os_image = "ocid1.image.oc1.uk-london-1.aaaaaaaagwdcgcw4squjusjy4yoyzxlewn6omj75f2xur2qpo7dgwexnzyhq"
  public_key_path = var.public_key_path
  subnet_id = oci_core_subnet.subnet.id
  nsg_id = oci_core_network_security_group.nsg.id
  create_dns_entry = "yes"
}
```

## Open-source
All the code for these tutorials is available as part of [DevOps-Workstream](https://github.com/lightenna/devops-workstream). 
If you'd like to see all the [previous and future installments of this tutorial](/tech/remprov), they're available under the `remprov` tag.

{% include call_to_action-opsteam_iac.html %}
