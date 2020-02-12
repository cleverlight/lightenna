---
layout: single
title: Beware open ports in Oracle Cloud's Default Security Lists
description: Setting up a Network Security Group confers additional (OR) access, not restrictive access (AND)
tags: tech devops terraform oracle-cloud
toc: true
header:
    overlay_image: /assets/images/techupdate_00012_1920x.png
    small_image: /assets/images/techupdate_00012_640x.png
---

## Oracle Cloud
When you provision a machine in Oracle Cloud it's tempting to use the VCN's Default Security List:
```
resource "oci_core_subnet" "subnet" {
  availability_domain = data.oci_identity_availability_domain.ad.name
  cidr_block = "10.46.0.0/24"
  display_name = "subnet-${var.hostname}"
  dns_label = "subnet${var.hostname}"
  security_list_ids = [
    oci_core_vcn.vcn.default_security_list_id]
...
```

##
If you don't want SSH open to all and sundry, it's important to create your own empty security list thus:
```
resource "oci_core_subnet" "subnet" {
  availability_domain = data.oci_identity_availability_domain.ad.name
  cidr_block = "10.46.0.0/24"
  display_name = "subnet-${var.hostname}"
  dns_label = "subnet${var.hostname}"
  security_list_ids = [
    oci_core_security_list.empty_security_list.id]
  compartment_id = var.compartment_ocid
  vcn_id = oci_core_vcn.vcn.id
  route_table_id = oci_core_vcn.vcn.default_route_table_id
  dhcp_options_id = oci_core_vcn.vcn.default_dhcp_options_id
}

# create empty security list to avoid using 'default' with open 22
resource "oci_core_security_list" "empty_security_list" {
  compartment_id = var.compartment_ocid
  vcn_id = oci_core_vcn.vcn.id
  display_name = "seclist-${var.hostname}"
}
```

which means you can explicitly open the ports you want in the Network Security Group:
```
resource "oci_core_network_security_group_security_rule" "nsg_outbound" {
  network_security_group_id = "${oci_core_network_security_group.nsg.id}"
  direction = "EGRESS"
  protocol = "all"
  description = "nsg-${var.hostname}-outbound"
  destination = "0.0.0.0/0"
  destination_type = "CIDR_BLOCK"
}

resource "oci_core_network_security_group_security_rule" "nsg_inbound_ssh" {
  network_security_group_id = "${oci_core_network_security_group.nsg.id}"
  direction = "INGRESS"
  protocol = "6" # TCP
  description = "nsg-${var.hostname}-inbound-ssh"
  # allow SSH traffic only from the bastion
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

## Open-source
All the code for these tutorials is available as part of [DevOps-Workstream](https://github.com/lightenna/devops-workstream). 

## Get your team coding
If you'd like to help your Operations team move to infrastructure-as-code, please [get in touch](/contact) to find out how Lightenna consulting could accelerate your Cloud journey.
