# ccccAI
## 使用说明
### 1. 

创建 `models` 文件夹将,利用 `PaddleDetection` 将权重导出并放入

```
models/
      model1/infer_cfg.yml
             model.pdiparams
             model.pdiparams.info
             model.pdmodel
```

### 2. 

创建 `Market-1501-v15.09.15` 文件夹，用来存放 `Re-ID` 的 `query` 和 `bounding_box_test`

### 3. 

运行 `main.py` 打开使用界面 

![image](https://user-images.githubusercontent.com/74087260/127842218-ad6b2869-8039-42a2-8b87-4ddc3882d933.png)

### 4. 

首先界面**右上角**选择你自己准备的模型，并选择**置信度**和 **GPU 或 CPU 加速**。

再添加你想要检测的视频（如果使用 CPU 多线程则**线程数量对应视频数量**），点击「开始检测」即可开始行人目标检测。

### 5.

检测完毕后，检测结果将会被存放在 `output/detect`。

点击「开始追踪」按钮后，会启动追踪操作，追踪完毕之后的追踪结果会被存放在 `output/track` 中。

### 6.

#### 多镜头使用说明：

添加两个及以上的视频（视频以**数字命名**且**不要有下划线**）且同个人在不同视频中都有出现。

通过点击选择需要寻找的目标，根据追踪的结果，会自动将每个视频中的每个 ID 的图片单独抠出，存放在 `Market-1501-v15.09.15/bounding_box_test`，每个视频中的每个 ID 的一张图片会被存放在 `query` 文件夹中。

如下图：![image](https://user-images.githubusercontent.com/74087260/127846011-8c29477d-6b53-484f-8ebf-8810b99b1f02.png)


### 7.
选择一个 ID 进行多镜头追踪，追踪完毕后会输出在输入的视频中目标的 ID、目标的图片和在视频中出现的当前帧。
如下图：

![image](https://user-images.githubusercontent.com/74087260/127847880-4d7426da-ba7d-4e1c-81c0-91100ebbc014.png)


### 8.
输出图会保存在 `show.png` 中。

如下图：

![image](https://user-images.githubusercontent.com/74087260/127848282-fb5ff95e-cb0d-4f0d-afec-ce52ce0f9faa.png)
