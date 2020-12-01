# enclosure_book
The Enclosure Project 

This is the repository for content to create the [Enclosure Book](https://jhconning.github.io/enclosure_book/).

- It uses the [jupyter book](https://jupyterbook.org/intro.html) framework to transform content from jupyter notebooks and markdown files into static HTML on github pages.
   - The left contnet navigation bar is created by the [_toc.yml](https://github.com/jhconning/enclosure_book/blob/main/_toc.yml) file
   - Most other info about the site is in [_config.yml](https://github.com/jhconning/enclosure_book/blob/main/_config.yml) 
   - Any new push to the site triggers a [github action](https://jupyterbook.org/publish/gh-pages.html?highlight=github%20action) that launches a virtual machine in the cloud that rebuilds the jupyterbook site (relevant script [here](https://github.com/jhconning/enclosure_book/blob/main/.github/workflows/book.yml))
