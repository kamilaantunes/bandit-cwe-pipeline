import os

def connect_to_database():
    password = "hardcoded_password"  # Vulnerabilidade (CWE-259)
    print("Connecting to database with password:", password)

def execute_command(cmd):
    os.system(cmd)  # Vulnerabilidade (CWE-78)

# Uso
connect_to_database()
execute_command("ls -la")
