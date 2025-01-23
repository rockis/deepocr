# 使用嵌入模型OCR的 Demo



## 需求

python >= 3.10

通过pip安装依赖

```
pip install -r requirements.txt
```

CPU版本

```
pip install -r requirements_cpu.txt
```



## 运行

```bash
python t_ocr.ppy /path-to-image/img.png
```



注意，首次运行会从hugging-face下载模型，大约300-400MB。 若无法访问hugging-face,可设置环境变量
```
export HF_ENDPOINT=https://hf-mirror.com
```

