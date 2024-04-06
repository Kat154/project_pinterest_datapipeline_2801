resource "aws_db_instance" "pinterest-datapipeline-postgresql-database"{
  engine = "postgres"
  db_name = "pinterest_datapipelines_postgresql_db"
  identifier = "sonia-postgresql-database"
  instance_class = "db.t3.micro"
  allocated_storage = 20
  publicly_accessible = true
  username = var.db-username
  password = var.db-password
  vpc_security_group_ids = [aws_security_group.sg_for_rds_postgresql_database.id]
  skip_final_snapshot = true
  tags={
    Name = "sonia-ka-postgresql-database"
  }
}
