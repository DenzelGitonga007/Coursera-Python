# Checking for my PC's health
# Import shell utilies
import shutil
# Get the storage
my_disk_usage = shutil.disk_usage("/")
print(my_disk_usage)
print((my_disk_usage.free / my_disk_usage.total) * 100)