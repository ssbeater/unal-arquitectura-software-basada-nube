resource "null_resource" "docker_commands" {
  provisioner "local-exec" {
    command = "docker tag isbn-users-ms ${var.registry_address}/isbn-users-ms"
  }

  provisioner "local-exec" {
    command = "docker push ${var.registry_address}/isbn-users-ms"
  }

  provisioner "local-exec" {
    command = "docker tag isbn-ag ${var.registry_address}/isbn-ag"
  }

  provisioner "local-exec" {
    command = "docker push ${var.registry_address}/isbn-ag"
  }

  provisioner "local-exec" {
    command = "docker tag isbn-wa ${var.registry_address}/isbn-wa"
  }

  provisioner "local-exec" {
    command = "docker push ${var.registry_address}/isbn-wa"
  }
}
