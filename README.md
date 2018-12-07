My Personal Blog

My blog is built heavily on the [Pelican Flex](https://github.com/alexandrevicenzi/Flex) theme.
If you're not familiar with Pelican, you should read their documentation [here].
I also use several Pelican plugins:

* [`pelican-cite`](https://github.com/cmacmackin/pelican-cite) for citing academic papers
* [`ipynb.markup`](https://github.com/danielfrg/pelican-ipynb) for rendering jupyter notebooks natively
* [`pelican_youtube`](https://github.com/kura/pelican_youtube) for rendering Youtube videos natively (definitely worth it since I have all of two on here...)
* [`render_math`](https://github.com/getpelican/pelican-plugins/tree/master/render_math) for rendering math notation

At the moment all development happens locally.
It is **VERY IMPORTANT** to work from the `source` branch, because GitHub Pages can only deploy the `master` branch -- which doesn't have the source codes.
To publish, run something like `bash push_from_local.sh`.

Note that you need to have `python` and `pelican` installed to do this.
I have these packages installed through the `environment.yml`, as well as some extra packages that I use for the analysis that I may blog about.
You don't need all of these packages, and you may prefer to use pip.
There are other ways for synchronizing with github pages, such as `doctr`, but for my current purposes this works well.