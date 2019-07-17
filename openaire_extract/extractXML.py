import json
import os
import base64


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
        if file_type == "tar":
            with open(path, "wb") as write_file:
                write_file.write(text)
    return file_name


def extract_binary(dictionary: dict):
    bin = dictionary["body"]["$binary"]
    return bin


def run():
    with open("/tmp/openaire/example.json") as f:
        counter = 0
        line = f.readline()
        while line:
            counter += 1
            line = f.readline()
            try:
                dictionary = json.loads(line)
                id = dictionary["objIdentifier"]
                file_name = save_file(dictionary, id, "/tmp/openaire/jsons", "json")
                print(f"{counter}. json was saved: {file_name}")
                bin = (extract_binary(dictionary))
                decoded = base64.b64decode(bin)
                tar_file = save_file(decoded, id, "/tmp/openaire/tars", "tar")

            except:
                continue


if __name__ == "__main__":
    run()
