# molihedownload

模拟“魔力盒APP”随机下载视频。

# main.py

这是最终文件。实现的功能有：
- 包含GUI
- 模拟“魔力盒APP”随机下载视频
- 下载过程中会显示视频的相关信息
- 文件会单独保存到`video`文件夹下
- 如果网络出现异常会提示检查网络和错误信息。

# initial_version.py

这是下载器的最初文件，手动输入视频ID，下载对应视频到本地。

# random_download.py

该文件实现了视频的下载，其实只是用到了`random`库

# disable_button.py

这是一个禁用按钮的文件，因为普通按钮不能实现禁用，用这种方法可以实现按钮的禁用。保证在下载过程中不能再次点击下载。（如果不禁用可以下载，只是程序会略卡）

# 安装依赖

```
pip install -r requirements.txt
```
