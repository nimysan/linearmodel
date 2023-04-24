# 创建一个可以执行常见scikit-learn的conda环境

## 执行环境创建 - RpML

```bash

conda create -n RpML python=3.10
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.14.0
  latest version: 23.3.1

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: /Users/yexw/miniconda3/envs/RpML

  added / updated specs:
    - python=3.10


The following NEW packages will be INSTALLED:

  bzip2              pkgs/main/osx-arm64::bzip2-1.0.8-h620ffc9_4
  ca-certificates    pkgs/main/osx-arm64::ca-certificates-2023.01.10-hca03da5_0
  libffi             pkgs/main/osx-arm64::libffi-3.4.2-hca03da5_6
  ncurses            pkgs/main/osx-arm64::ncurses-6.4-h313beb8_0
  openssl            pkgs/main/osx-arm64::openssl-1.1.1t-h1a28f6b_0
  pip                pkgs/main/osx-arm64::pip-23.0.1-py310hca03da5_0
  python             pkgs/main/osx-arm64::python-3.10.11-hc0d8a6c_2
  readline           pkgs/main/osx-arm64::readline-8.2-h1a28f6b_0
  setuptools         pkgs/main/osx-arm64::setuptools-66.0.0-py310hca03da5_0
  sqlite             pkgs/main/osx-arm64::sqlite-3.41.2-h80987f9_0
  tk                 pkgs/main/osx-arm64::tk-8.6.12-hb8d0fd4_0
  tzdata             pkgs/main/noarch::tzdata-2023c-h04d1e81_0
  wheel              pkgs/main/osx-arm64::wheel-0.38.4-py310hca03da5_0
  xz                 pkgs/main/osx-arm64::xz-5.2.10-h80987f9_1
  zlib               pkgs/main/osx-arm64::zlib-1.2.13-h5a0b063_0


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate RpML
#
# To deactivate an active environment, use
#
#     $ conda deactivate

Retrieving notices: ...working... done

```

## install Jupyter notebook

```bash
conda install -n RpML jupyter
```

## 关闭或者激活环境

```bash
conda deactivate # 关闭虚拟环境
conda activate RpML #激活虚拟环境
```

## 设置镜像

```bash
conda config add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
```

## 安装matplotlib等数据分析包

```bash
python -m pip install \
  --upgrade \
  --pre \
  --index-url https://pypi.anaconda.org/scipy-wheels-nightly/simple \
  --extra-index-url https://pypi.org/simple \
  matplotlib

python -m pip install -U scikit-learn
```