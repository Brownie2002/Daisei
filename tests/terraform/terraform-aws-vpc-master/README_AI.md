# Terraform AWS VPC Module

This Terraform module creates a Virtual Private Cloud (VPC) on AWS. It includes support for various advanced features such as VPC Flow Logs, Network ACLs, IPAM, and more.

## Prerequisites

- Terraform 1.0.0 or newer.
- Provider: AWS

## Usage

To use this module, include something like the following in your Terraform configuration:

```hcl
module "vpc" {
  source = "path/to/terraform-aws-vpc-master"

  # Required variables
  name        = "example-vpc"
  cidr_block  = "10.0.0.0/16"

  # Optional variables
  azs             = ["us-west-2a", "us-west-2b", "us-west-2c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway   = true
  enable_vpn_gateway   = true
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}
```

## Examples

This module includes several examples to demonstrate its usage:

- [ipv6-dualstack](examples/ipv6-dualstack/README.md)
- [network-acls](examples/network-acls/README.md)
- [ipam](examples/ipam/README.md)
- [issues](examples/issues/README.md)
- [manage-default-vpc](examples/manage-default-vpc/README.md)
- [simple](examples/simple/README.md)
- [vpc-flow-logs](examples/vpc-flow-logs/README.md)
- [complete](examples/complete/README.md)
- [outpost](examples/outpost/README.md)
- [block-public-access](examples/block-public-access/README.md)
- [separate-route-tables](examples/separate-route-tables/README.md)
- [ipv6-only](examples/ipv6-only/README.md)
- [secondary-cidr-blocks](examples/secondary-cidr-blocks/README.md)

## Inputs

| Name                     | Description                                                                 | Type          | Default       | Required |
|--------------------------|-----------------------------------------------------------------------------|---------------|---------------|----------|
| name                     | Name to be used on all the resources as identifier                         | `string`      | n/a           | yes      |
| cidr_block               | The CIDR block for the VPC                                                 | `string`      | n/a           | yes      |
| azs                      | A list of availability zones in the region                                  | `list(string)`| n/a           | yes      |
| private_subnets          | A list of private subnets inside the VPC                                    | `list(string)`| n/a           | yes      |
| public_subnets           | A list of public subnets inside the VPC                                     | `list(string)`| n/a           | yes      |
| enable_nat_gateway       | Should be true if you want to provision NAT Gateways for each of your private networks | `bool`        | `false`       | no       |
| enable_vpn_gateway       | Should be true if you want to create a new VPN Gateway resource and attach it to the VPC | `bool`        | `false`       | no       |
| enable_dns_hostnames     | Should be true to enable DNS hostnames in the VPC                          | `bool`        | `false`       | no       |
| enable_dns_support       | Should be true to enable DNS support in the VPC                             | `bool`        | `true`        | no       |
| tags                     | A mapping of tags to assign to all resources                                | `map(string)` | `{}`          | no       |

## Outputs

| Name                     | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| vpc_id                   | The ID of the VPC                                                           |
| private_subnets          | List of IDs of private subnets                                             |
| public_subnets           | List of IDs of public subnets                                               |
| nat_public_ips           | List of public Elastic IPs created for AWS NAT Gateway                     |
| azs                      | A list of availability zones specified as input                             |

## Authors

Module managed by [Your Organization].

## License

Apache 2 Licensed. See [LICENSE](LICENSE) for full details.

## Contributing

Contributions are welcome! See [Contributing Guidelines](.github/contributing.md) for more information.

## Changelog

Refer to the [Changelog](CHANGELOG.md) for a full history of the project.

## Upgrading

Follow the [Upgrade Guides](UPGRADE-3.0.md) and [UPGRADE-4.0.md](UPGRADE-4.0.md) for instructions on upgrading the module.
