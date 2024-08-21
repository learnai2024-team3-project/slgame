import os
import yaml


def find_dataset_directory(base_dir, target_subdir):
    for root, dirs, files in os.walk(base_dir):
        if target_subdir in dirs:
            return os.path.join(root, target_subdir)
    return None


def update_data_yaml(yaml_path):
    # 獲取當前工作目錄
    current_dir = os.getcwd()

    # 動態查找第一層目錄，假設你要查找的目錄下包含 'train/images' 和 'valid/images'
    dataset_dir = find_dataset_directory(current_dir, 'train')
    if dataset_dir is None:
        raise FileNotFoundError("揣無 'train/images' 的目錄")

    # 查找到第一層目錄的名稱
    first_level_dir = os.path.basename(os.path.dirname(dataset_dir))

    # 更新 YAML 文件中的路徑
    train_path = os.path.join(current_dir, first_level_dir, 'train', 'images')
    val_path = os.path.join(current_dir, first_level_dir, 'valid', 'images')

    # 讀取 YAML 文件
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)

    # 更新路徑
    data['train'] = train_path.replace("\\", "/")  # 使用正斜杠
    data['val'] = val_path.replace("\\", "/")      # 使用正斜杠

    # 寫回 YAML 文件
    with open(yaml_path, 'w') as file:
        yaml.safe_dump(data, file)

    print(f"Updated train path to: {data['train']}")
    print(f"Updated val path to: {data['val']}")


def add_path_equal_dot(yaml_path):
    with open(yaml_path, 'r') as file:
        lines = file.readlines()
    if not lines or lines[-1].strip() != "path: .":
        with open(yaml_path, 'a') as file:
            if lines and not lines[-1].endswith('\n'):
                file.write('\n')  # if no EOL at EOF, add EOL
            file.write('path: .\n')
            print(f'"path: ." added to {yaml_path}')


if __name__ == '__main__':
    # 使用範例
    yaml_path = 'data.yaml'  # 替換為你實際的 yaml 文件路徑
    update_data_yaml(yaml_path)
