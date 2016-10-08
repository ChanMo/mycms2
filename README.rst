MyCMS2
========

一个基于django的简单的cms系统

介绍:
--------

基于django，拥有页面和主题模板两项功能。可以自由切换网站主题模板，也可在后台实事修改模板代码。

基于:
--------

* django
* django-flat-theme
* django-ckeditor
* django-mptt
* beautifulsoup4
* breach


快速开始：
----------

下载代码:

.. code-block::

    git clone https://github.com/ChanMo/mycms2 project 


创建代码环境:

.. code-block::

    cd project
    virtualenv env
    source env/bin/activate
    pip install -r requirement.txt


操作数据库:

.. code-block::

    cd mycms2
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py makemigrations page
    python manage.py migrate

测试:

.. code-block::

    python manage.py runserver
