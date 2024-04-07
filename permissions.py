import os

def change_permissions(file_path, mode):
    try:
        os.chmod(file_path, mode)
        print(f'Permissions changed for {file_path}')
    except Exception as e:
        print(f'Error changing permissions for {e}')

file_path = '/backup_files'
mode =  0o755
change_permissions(file_path, mode)