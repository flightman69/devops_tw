# 1. AWS Provider Configuraton (Region)
provider "aws" {
  region = "us-east-1" 
}


# 2. Security Groups (Firewall Rules)
resource "aws_security_group" "api_sg" {
  name        = "api-sg"
  description = "Allow HTTPS and SSH traffic"

  # Allow SSH (Port 22) 
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  
  }

  # Allow HTTPS (Port 443) 
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Port 80 for Caddy certification
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  # outbound traffic (Docker)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 3. Static Ip (Elastic IP) 
resource "aws_eip" "api_ip" {
  instance = aws_instance.api_server.id
}

# 4. Creatign EC2 Instance
resource "aws_instance" "api_server" {
  ami           = "ami-0c7217cdde317cfec"  # Ubuntu 22.04 LTS
  instance_type = "t2.micro"
  key_name      = "speakx-aws-key"    
  vpc_security_group_ids = [aws_security_group.api_sg.id]
  tags = {
    Name = "speakx-aws-instance"
  }
}

# 5. AWS Ecr Repo for Dockerimage
resource "aws_ecr_repository" "flask_app" {
  name = "speakx-ecr"
}

# 6. Ouput Ip addr (Elastic Ip)
output "public_ip" {
  value = aws_eip.api_ip.public_ip
}

