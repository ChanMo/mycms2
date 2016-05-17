基本的cms系统
=============

一个简单的cms系统

快速开始：
----------

使用virtualenv:

.. code-block::

    git clone https://github.com/ChanMo/mycms2 project_com 
    mkdir project_com
    cd project_com
    virtualenv env
    source env/bin/activate
    pip install -r requirement.txt

更新数据库:

.. code-block::

    cd mycms2
    python manage.py migrate

