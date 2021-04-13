# enclosure_book
The Enclosure Project 

This is the repository for content to create the [Enclosure Book](https://jhconning.github.io/enclosure_book/).

- It uses the [jupyter book](https://jupyterbook.org/intro.html) framework to transform content from jupyter notebooks and markdown files into static HTML on github pages.
   - The left navigation bar on the site is created by the [_toc.yml](https://github.com/jhconning/enclosure_book/blob/main/_toc.yml) file
   - Most other info for the site is set in [_config.yml](https://github.com/jhconning/enclosure_book/blob/main/_config.yml) 
   - Any new push to this repo triggers a [github action](https://jupyterbook.org/publish/gh-pages.html?highlight=github%20action) that launches a virtual machine in the cloud that rebuilds the jupyterbook site with the new content (relevant script [here](https://github.com/jhconning/enclosure_book/blob/main/.github/workflows/book.yml))
   - Typical workflow:  use jupyter book to build a local copy of the site on your machine.  Then just push the relevant changed markdown/notebooks.
