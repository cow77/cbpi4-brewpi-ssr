from setuptools import setup

setup(name='cbpi4-brewpi-ssr',
      version='0.0.1',
      description='CraftBeerPi4 Brewpi SSR Interface',
      author='Jacobus de Waal',
      author_email='codewaal@micromaat.nl',
      url='https://github.com/cow77/cbpi4-brewpi-ssr',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-brewpi-ssr': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-brewpi-ssr'],
     )
