tasks = ["Research", "Analyze", "Code", "Test", "Deploy"]

tasks[1] = "Pin"
tasks.append("Construct")
tasks.remove("Deploy")
removed = tasks.pop(2)
tasks.sort()
print(tasks)