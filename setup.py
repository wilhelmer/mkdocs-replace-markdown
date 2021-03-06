from setuptools import setup, find_packages

setup(
    name='mkdocs-replace-markdown',
    version='0.1.0',
    description='An MkDocs plugin to replace text in Markdown on build.',
    long_description='',
    keywords='mkdocs replace',
    author='Lars Wilhelmer',
    author_email='lars.wilhelmer@baslerweb.com',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.1'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'replace_markdown = mkdocs_replace_markdown.plugin:ReplaceMarkdownPlugin'
        ]
    }
)
