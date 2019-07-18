import json
import os
import base64
import tarfile
from zipfile import ZipFile

from xml_nusl.collecting import extracting_data


def parsing_id(id: str):
    if "::" in id:
        id = id.replace("::", ":")
    id_array = id.split(":")
    dir = id_array[-2]
    file_name = id_array[-1]
    return dir, file_name


def save_file(text, id: str, dir_path: str, file_type: str):
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    child_dir = parsing_id(id)[0]
    file_name = f"{parsing_id(id)[1]}.{file_type}"
    path = os.path.join(dir_path, child_dir, file_name)
    if not os.path.isdir(os.path.join(dir_path, child_dir)):
        os.mkdir(os.path.join(dir_path, child_dir))
    if not os.path.exists(path):
        if file_type == "json":
            with open(path, "w") as write_file:
                json.dump(text, write_file)
        if file_type == "zip":
            with open(path, "wb") as write_file:
                write_file.write(text)
    return path


def extract_binary(dictionary: dict):
    bin = dictionary["body"]["$binary"]
    return bin


def extract_tar(path: str):
    tar = tarfile.open(path)
    tar.extractall()
    tar.close()


def extract_zip(path: str, target_dir: str):
    with ZipFile(path, 'r') as zipObj:
        # Extract all the contents of zip file in current directory
        zipObj.extractall(target_dir)
        return target_dir


def save_xml(id, path, zip_file_path):
    parent_dir = parsing_id(id)[0]
    childir = parsing_id(id)[1]
    root_dir = os.path.dirname(path)
    target_dir = os.path.join(root_dir, 'xml', parent_dir, childir)
    if not os.path.isdir(os.path.join(root_dir, "xml")):
        os.mkdir(os.path.join(root_dir, "xml"))
    if not os.path.isdir(os.path.join(root_dir, 'xml', parent_dir)):
        os.mkdir(os.path.join(root_dir, 'xml', parent_dir))
    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)
        extract_zip(zip_file_path, target_dir)
        old_name = f"{target_dir}/body"
        new_name = f"{target_dir}/{parsing_id(id)[1]}.xml"
        os.rename(old_name, new_name)
    return f"{target_dir}/{parsing_id(id)[1]}.xml"


def run(path: str):
    with open(path) as f:
        counter = 0
        line = f.readline()
        while line:
            counter += 1
            line = f.readline()
            try:
                dictionary = json.loads(line)
                id = dictionary["objIdentifier"]
                file_path = save_file(dictionary, id, f"{os.path.join(os.path.dirname(path), 'jsons')}", "json")
                print(f"{counter}. json was saved: {file_path}")
                bin = (extract_binary(dictionary))
                decoded = base64.b64decode(bin)
                zip_file_path = save_file(decoded, id, f"{os.path.join(os.path.dirname(path), 'zip')}", "zip")
                xml_path = save_xml(id, path, zip_file_path)
                #####################################################
                #                    Parsing XML                    #
                #####################################################
                extracting_data(xml_path)

            except:
                continue


if __name__ == "__main__":
    run("/home/semtex/Projekty/TEST_PROJECTS/xml_nusl/xml_nusl/testovaci_openaire/sample.json")
    # extract_tar('/home/semtex/Projekty/TEST_PROJECTS/xml_nusl/xml_nusl/testovaci_openaire/tars/ec_fp7_ict__/1bfb37763b93858c625dab85ab1d888d.tar.gz')
    # extract_zip('/home/semtex/Projekty/TEST_PROJECTS/xml_nusl/xml_nusl/testovaci_openaire/tars/ec_fp7_ict__/1bfb37763b93858c625dab85ab1d888d.zip')
