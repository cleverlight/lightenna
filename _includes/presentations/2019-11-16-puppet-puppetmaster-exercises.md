
## Exercise: puppet new machine
+ Connect to remprov machine
+ Spin up azure_basic (bastion) using Terraform
~/devops-workstream/terraform/azure_basic
+ Connect to your bastion machine
+ Ping remprov machine to check connectivity
+ Create /etc/puppetlabs/puppet/puppet.conf
    + Point at remprov puppetmaster
    + Set environment = teaching
+ Run agent to create cert request
+ Sign cert request on puppetmaster
+ Run agent once manually
+ Review run output locally
+ Review run output using puppetboard on remprov (port 18443)

{% if include.pres %}Note: {% endif %}

---

