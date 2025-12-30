
import os
import shutil
import re

# source and destination paths
source = r"C:\xampp\htdocs\dcpi"
destination = r"C:\xampp\htdocs\dcpi_backup"
zip_path = r"D:\Download\dcpi"

def copy_dcpi(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)  # Remove existing backup if it exists

    # Walk through the source folder
    for root, dirs, files in os.walk(src):
        # Determine relative path to maintin folder structure
        rel_path = os.path.relpath(root, src)
        dest_path = os.path.join(dest, rel_path)

        # Skip gen_sql folder entirely
        if 'gen_sql' in dirs:
            dirs.remove('gen_sql') # Prevent walking into it

        # Create destination folder 
        os.makedirs(dest_path, exist_ok=True)

        # Copy files
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_path, file)

            # Skip gen_func_lib_data.js in lib folder
            if rel_path == "lib" and file == "gen_func_lib_data.js":
                continue

            shutil.copy2(src_file, dest_file)

    # Remove drugcheckphilippines.com folder if exists
    drugcheck_path = os.path.join(dest, "medical_app", "drugcheckphilippines.com")
    if os.path.exists(drugcheck_path):
        shutil.rmtree(drugcheck_path)


    # Modify header.js variable from 0 to 1 for live server deployment
    header_js = os.path.join(dest, "gen_page", "header.js")
    if os.path.exists(header_js):
        with open(header_js, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace first occurence of = 0; with = 1; (adjust pattern if variable name is known)
        content = re.sub(r"=(\s*)0;", "= 1;", content, count=1)

        with open(header_js, "w", encoding="utf-8") as f:
            f.write(content)


    # Modify medical_app.js variable from 0 to 1 for live server deployment 
    medical_app_js = os.path.join(dest, "medical_app", "medical_app.js")
    if os.path.exists(medical_app_js):
        with open(medical_app_js, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace first occurence of = 0; with = 1; (adjust pattern if variable name is known)
        content = re.sub(r"=(\s*)0;", "= 1;", content, count=1)

        with open(medical_app_js, "w", encoding="utf-8") as f:
            f.write(content)

    print("DCPI folder copied successfully with exclusions!")




def zip_dcpi_folder(folder_path, zip_name):
    # Remove old zip if exists
    if os.path.exists(zip_name + ".zip"):
        os.remove(zip_name + ".zip")

    shutil.make_archive(zip_name, 'zip', folder_path)
    print(f"Folder zipped successfully to {zip_name}.zip")






# Run the code
copy_dcpi(source, destination)
zip_dcpi_folder(destination, zip_path)