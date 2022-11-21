resource "local_file" "ansible-inventory" {
  content = templatefile("templates/inventory.tmpl", {
    wapiti_instances : [for index, wapiti in aws_instance.wapiti.* : {
      name : wapiti.tags.Name,
      ip : wapiti.private_ip,
      id : wapiti.id,
    }]
  })
  filename = "../ansible/inventory"
  file_permission = "644"
}

output "instances" {
  value = {
    wapiti_instances : [for index, wapiti in aws_instance.wapiti.* : {
      name : wapiti.tags.Name,
      ip : wapiti.private_ip,
      id : wapiti.id,
    }]
  }
}