基本的cms系统
=============

一个简单的cms系统

快速开始：
----------

使用virtualenv:

.. code-block::

    mkdir project_com
    cd project_com
    virtualenv env
    source env/bin/activate
    pip install requirement.txt

使用mycms2:

.. code-block::

   git clone https://github.com/ChanMo/mycms2 

更新数据库:

.. code-block::

    cd mycms2
    python manage.py migrate

