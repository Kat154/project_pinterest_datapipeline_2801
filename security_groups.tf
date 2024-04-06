resource "aws_security_group" "sg_for_rds_postgresql_database"{
  name_prefix = "Pinterest-"
  ingress{
    from_port = 5432
    to_port = 5432
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
