1.安装poetry 命令：`pip install poetry poetry-plugin-shell`</br>
2.下载authentik文件`git clone XXXX`（项目包含sys link`website/static/blueprints`）</br>
3.换源`poetry source add --priority=primary mirrors https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/`</br>
4.创建Python虚拟环境,并进入poetry的shell`poetry shell`</br>
5.安装npm</br>
6.配置npm镜像源`npm config set registry https://mirrors.cloud.tencent.com/npm/`
7.确保电脑上有rust环境</br>
8.将pyproject.toml中的`psycopg = { extras = ["c"], version = "*" }`替换为`psycopg = { extras = ["binary"], version = "*" }`</br>
9.下载`https://github.com/mozilla/sccache`放到path环境变量指定的目录中</br>
10.配置环境(根据2025/3/11的MakeFile)(按顺序运行)</br>
```cmd
poetry lock
poetry install
cd web
npm ci
cd ../website
npm ci
```
11.配置本地配置文件`python -m scripts.generate_config`（`local.env.yml`）</br>
未完成
