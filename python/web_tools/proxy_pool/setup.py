from setuptools import setup

setup(
    name='python3',
    version='0.1',
    packages=['first_scrapy', 'first_scrapy.spiders', 'spiders', 'scrapy_selenium_demo', 'scrapy_selenium_demo.spiders',
              'way_fair', 'way_fair.spiders'],
    package_dir={'': 'python/web_tools/proxy_pool'},
    url='http://example.com',
    license='',
    author='Administrator',
    author_email='Administrator@qq.com',
    description='Administrator reports'
)
