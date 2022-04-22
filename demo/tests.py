import re

from django.test import TestCase

# Create your tests here.
uPattern = re.compile('(http|https):\/\/([\w.]+\/?)\S*')
print(uPattern.search( 'www.baoiud.com'))
print(uPattern.search( 'https://item.jd.com/10046068989045.html'))
