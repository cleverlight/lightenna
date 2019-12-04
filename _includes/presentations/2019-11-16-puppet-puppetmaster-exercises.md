
## Exercise: puppet new machine
+ Connect to puppetmaster machine
`puppetmaster.training.azure-dns.lightenna.com`
+ Spin up azure_basic (bastion) using Terraform
`~/devops-workstream/terraform/azure_basic`
+ Connect to your new machine
+ Ping puppetmaster machine to check connectivity
+ Create /etc/puppetlabs/puppet/puppet.conf
    + Point `server` at puppetmaster
    + Set `environment = workstream`
+ Run agent to create cert request
+ Sign cert request on puppetmaster
    + Requires escalation using sudo
+ Run agent once manually
+ Review run output locally
+ Review run output using puppetboard on puppetmaster (port 18443)
    + Port is hidden behind firewall
    + Set up an SSH tunnel to bring remote port to localhost

{% if include.pres %}Note: {% endif %}

---

