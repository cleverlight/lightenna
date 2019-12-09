
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

## Exercise: distribute secrets from a shared master
+ Update puppet manifests
    + create a feature branch from master
    + make your changes
    + commit to feature branch
    + merge back into master
    + manually deploy master to control repo `/srv/git/github.com/devops-workstream`
    + run puppet agent 
+ Create a node definition for your node
+ Add a notify resource
+ Repuppet your node to verify the notify resource runs
+ Create a class in `/puppet/environments/workstream/modules`
+ Move your notify resource into the module
+ Specify a class-scope variable in the class definition and assign it a default value
+ Display that value using a variable reference in your "quoted" notify message attribute
+ Override that value using a hiera name:value pair in `/puppet/environments/workstream/hieradata/common.yaml`
+ Override that value using a secret in `/puppet/environments/workstream/hieradata/secrets.eyaml`
+ Create a template file and populate using data from hiera
    + You may wish to use the example resources in `/puppet/tutorial/07-templating`

{% if include.pres %}Note: {% endif %}

---
