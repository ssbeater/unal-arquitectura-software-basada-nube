variable "region" {
    type = string
    default = "region"
}

variable "user_database_name"{
    type = string
    description = "nombre de la base de datos"
}

variable "google_project_id" {
    type = string
}

variable "registry_repo_id" {
    type = string
    default = "isbn_registry"
}

variable "registry_address" {
    type = string
}

variable "users_db_host" {
    type = string
}
