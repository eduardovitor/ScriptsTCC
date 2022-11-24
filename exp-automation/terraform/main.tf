terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

data "aws_ami" "ubuntu-linux-2204" {
  most_recent = true
  owners      = ["099720109477"]
  
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
  
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "wapiti" {
  count         = var.instance_count
  ami           = data.aws_ami.ubuntu-linux-2204.id
  instance_type = var.instance_type
  key_name      = "exp-wapiti"
  vpc_security_group_ids = ["sg-01e4a2e2d9dd844da"]

  tags = {
    Name  = "wapiti_${count.index+1}"
    Owner = "eduvitor"
  }
}