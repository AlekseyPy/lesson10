hardware = ("Power","Off","Restart")
software = ["Power","Off","Restart"]
del software[1]
software.insert(1, "On")
print(software)
print("Кортеж нельзя изменять.А списки можно.")