# 克隆已有微服务仓库进行本地开发
* 按教程创建django工程（不会问梦里）
* 找到`views.py`所在的那个目录
* 把`urls.py`和`views.py`删除
* 克隆仓库到**该目录**（把路径看好了，克隆之后新的`views.py`应该就在这个目录内，不要克隆出子目录！！）

# 本地新建微服务
* 按教程创建django工程（不会问梦里）
* 找到`views.py`所在的那个目录
* 把我们的[.gitignore](.gitignore)和[cloudDeployment.py](cloudDeployment.py)复制到这个目录

## 创建git仓库
注意要在`views.py`所在的目录下创建，不要在外面创建

# 云端部署微服务
* cd到src目录（可以直接vscode右键目录点`在终端中打开`）
* `git clone 你的微服务仓库`
* cd到你刚克隆的仓库
* `python cloudDeployment.py`
* 由于我们是前后端分离的，未来会在接口内鉴权，所以不用django自带的CSRF检验。所以如果你的服务里有POST接口，在`setting.py`中删除`'django.middleware.csrf.CsrfViewMiddleware',`（否则POST请求会被直接拒绝）
* 点vscode框下面的部署按钮

## 拉取最新代码
* cd到之前克隆的仓库
* `git pull`
* `python cloudDeployment.py`
* 点vscode框下面的部署按钮

### Note
谁帮我优化一下`cloudDeployment.py`：复制的时候把`.git`里面的东西也复制到`djangodemo`，这样每次打开自动部署cd到`djangodemo`直接`git pull`就行了，省的每次拉取都执行`cloudDeployment.py`了
