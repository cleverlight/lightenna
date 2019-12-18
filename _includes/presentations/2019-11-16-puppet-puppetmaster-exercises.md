
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

## Exercise: puppet a machine from a shared master
+ Connect to puppetmaster machine
`puppetmaster.training.azure-dns.lightenna.com`
+ Spin up azure_pmd (bastion) using Terraform
    + `cd ~/devops-workstream/terraform/azure_pmd`
    + `terraform init`
    + `sudo ls`
        + You must `sudo` before attempting to spin up the machine to allow your SSH session to escalate
        + This is required for Terraform to run `puppetserver ca sign --certname=<your_new_hostname>`
+ Connect to your new machine
    + Check the puppet run using `sudo cat /root/puppet_agent.out`
+ Look for your machine on the puppetmaster
    + Tunnel a connection to port 18443
    + Check the puppet run using Puppetboard

{% if include.pres %}Note: {% endif %}
Compared to the previous exercise, you'll notice that provisioning puppet-mastered machines is much faster than manually creating these things yourself.

---

## Exercise: distribute secrets from a shared master
+ Using the previous exercise, puppet a puppet-mastered machine 
    + Connect to your bastion machine
    + Source your FQDN using `hostname -f` on your bastion machine
+ Update puppet manifests
    + create a feature branch from master
    + create a module with a single class
    + complete your changes
    + commit to feature branch
    + merge back into master
    + manually deploy master to control repo `/srv/git/github.com/devops-workstream`
    + run puppet agent 
+ Create a node definition for your node
    + For now, match the node name precisely in `site.pp`
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

## Exercise: repeat in Vagrant
+ Walk-through directory structure
