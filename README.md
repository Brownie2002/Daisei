Enter the directory to scan: /workspaces/Daisei/examples/terraform
# Terraform AWS VPC Module

This Terraform module creates a Virtual Private Cloud (VPC) on AWS. The module is designed to be flexible and configurable, allowing you to create a VPC with various configurations, including IPv6, network ACLs, VPC flow logs, secondary CIDR blocks, and more.

## Features

- **Flexible VPC Configuration**: Supports IPv4, IPv6, dual-stack, and secondary CIDR blocks.
- **Network ACLs**: Configure network access control lists for fine-grained control.
- **VPC Flow Logs**: Enable VPC flow logs for monitoring and troubleshooting.
- **Manage Default VPC**: Option to manage the default VPC.
- **Outposts**: Supports AWS Outposts for on-premises AWS infrastructure.
- **Public Access Blocking**: Configure settings to block public access.
- **Separate Route Tables**: Create separate route tables for different subnets.
- **VPC Endpoints**: Create VPC endpoints for secure and private connections to AWS services.

## Prerequisites

- Terraform 1.0.0 or later
- AWS account and credentials

## Usage

```hcl
module "vpc" {
  source = "/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master"

  name = "example-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-west-2a", "us-west-2b", "us-west-2c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true
}
```

## Examples

This module includes several examples to illustrate different use cases:

- [IPv6 Dualstack VPC](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/examples/ipv6-dualstack)
- [Network ACLs](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/examples/network-acls)
- [IPAM](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/examples/ipam)
- [Issues](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/examples/issues)
- [Manage Default VPC](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/examples/manage-default-vpc)
- [Simple VPC](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/examples/simple)
- [VPC Flow Logs](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/examples/vpc-flow-logs)
- [Complete VPC](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/examples/complete)
- [Outpost VPC](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/examples/outpost)
- [Block Public Access](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/examples/block-public-access)
- [Separate Route Tables](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/examples/separate-route-tables)
- [IPv6 Only VPC](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/examples/ipv6-only)
- [Secondary CIDR Blocks](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/examples/secondary-cidr-blocks)

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|----------|
| name | Name to be used on all the resources as identifier | `string` | n/a | yes |
| cidr | The CIDR block for the VPC. | `string` | n/a | yes |
| azs | A list of availability zones in the region | `list(string)` | n/a | yes |
| private_subnets | A list of private subnets inside the VPC | `list(string)` | n/a | yes |
| public_subnets | A list of public subnets inside the VPC | `list(string)` | n/a | yes |
| enable_nat_gateway | Should be true to provision NAT Gateways for each of the private networks | `bool` | `false` | no |
| enable_vpn_gateway | Should be true to create a new VPN Gateway resource and attach it to the VPC | `bool` | `false` | no |

## Outputs

| Name | Description |
|------|-------------|
| vpc_id | The ID of the VPC |
| private_subnets | List of IDs of private subnets |
| public_subnets | List of IDs of public subnets |
| nat_gateway_ids | List of NAT Gateway IDs |
| vpn_gateway_id | The ID of the VPN Gateway |

## License

This module is licensed under the MIT License. See the [LICENSE](/workspaces/Daisei/examples/terraform/terraform-aws-vpc-master/LICENSE) file for more information.

## Contributing
