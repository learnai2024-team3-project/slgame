# 使用說明文件
1. 安裝 Sphinx
    ```shell
    pip install -U sphinx
    ```

2. 建立說明文件（HTML）
    ```shell
    make html # MacOS, Linux
    make.bat html # Windows 
    ```

# 編輯說明文件

**ReStructuredText** (RST) 的基本語法

```rst
===========================
ReStructuredText 快速教學
===========================

簡介
====

ReStructuredText (RST) 是一種輕量級標記語言，廣泛應用於 Sphinx 文件生成器及其他工具。它的設計目的是讓純文字格式易於閱讀，並且可以轉換為 HTML、PDF 等多種輸出格式。

標題
====

你可以透過不同的符號來創建不同層級的標題，最常見的是 `=` 和 `-`：

主標題
======

副標題
------

另一個章節
~~~~~~~~~~~

列表
====

可以輕鬆創建項目符號列表和編號列表：

- 項目符號 1
- 項目符號 2
  - 子項目符號

1. 編號項目 1
2. 編號項目 2

Inline Markup
=============

使用 Inline Markup 來強調文字或建立超連結：

- *斜體* 或 _斜體_
- **粗體** 或 __粗體__
- ``等寬字體``（用於程式碼或檔名）
- `超連結 <https://example.com>`_

程式碼區塊
==========

使用雙冒號和縮排來包含程式碼區塊：

.. code-block:: python

    def hello_world():
        print("Hello, world!")

Literal Blocks
==============

Literal Block 的創建方法是段落結尾使用 "::" 並縮排區塊內容：

::

    這是一個 Literal Block。
    它保留了換行和縮排格式。

表格
====

簡單的表格可以使用 `=` 或 `-` 符號來創建：

+-------------+---------------+
| 標題 1      | 標題 2        |
+=============+===============+
| 列 1, 欄 1  | 列 1, 欄 2    |
+-------------+---------------+
| 列 2, 欄 1  | 列 2, 欄 2    |
+-------------+---------------+

連結
====

你可以使用 inline markup 來創建超連結：

`Sphinx 文件 <https://www.sphinx-doc.org/zh_TW/master/>`_

圖片
====

要插入圖片，使用 `.. image::` 指令：

.. image:: https://www.example.com/image.png
   :alt: 範例圖片
   :width: 200px

註腳
====

註腳在文字中標記為 `[#]_`，並在文件底部定義：

這是一個包含註腳的範例句子 [#]_。

.. [#] 這是註腳內容。

指令
====

指令提供了額外的功能。例如，你可以插入目錄 (Table of Contents, TOC) 或參考資料：

.. toctree::
   :maxdepth: 2
   :caption: 目錄:

   section1
   section2

結論
====

這是一個關於 ReStructuredText 的基本入門介紹。你可以參閱官方文件來探索更複雜的功能。

```
