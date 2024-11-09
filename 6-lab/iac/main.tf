provider "google" {
  project =  var.google_project_id
  region  = "us-east4"
}

module "APIs" {
    source = "./modules/Apis"
    google_project_id = var.google_project_id
}

module "Registry" {
    source = "./modules/Registry"
    repository_id = var.registry_repo_id
    depends_on = [ module.APIs ]
}

module "Database" {
    source = "./modules/CloudSQL"
    user_database_name = var.user_database_name
    region = var.region
    depends_on = [ module.APIs ]
}

module "Firestore" {
  source = "./modules/Firestore"
  region = var.region
  depends_on = [ module.APIs ]
}

module "docker_commands" {
  source = "./modules/DockerCommands"
  registry_address = var.registry_address
  depends_on = [ module.Registry ]
}

module "CloudFunction" {
  source = "./modules/CloudFunction"
  region = var.region
  project_id = var.google_project_id
  depends_on = [ module.APIs ]
}

module "UserService" {
    source = "./modules/UserService"
    region = var.region
    registry_address = var.registry_address
    db_host = var.users_db_host
    depends_on = [ module.APIs, module.docker_commands ]
}
