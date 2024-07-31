This is a [FastHTML](https://fastht.ml) project using [Tailwind CSS](https://taiwindcss.com) for styling

## Getting Started

The only node package needed is Tailwind CSS. I chose to leave it as a node package instead of an executable so the project is not OS dependent.

All commands are executed at the root of the folder.

First, you have to install node packages.

```bash
npm install
```

Then, you need to install the python packages, using pip for example, with an activated virtual environment, or in your base python install if you do not care about your computer anymore.

```bash
pip install -r requirements.txt
```

Finally, to execute (dev mode with Tailwind CLI build on save):

```bash
python --tailwind True main.py
```

Open [http://localhost:5001](http://localhost:5001) with your browser to see the result.

You can start editing the page by modifying `main.py`. For now, you will need to refresh the page to see the results after saving.

## Note
`main.py` contains a subprocess call that calls the Tailwinc CLI build process after each file modification. 
This is a hacky method to make Tailwind CSS work with FastHTML without using the CDN.
Feel free to suggest a better solution for this, or any improvement, via a PR.
I also used fast_app instead of FastHTML to make it work, inspired by the [code](https://github.com/tinloof/fasthtml) for the [FastHTML landing page](https://fastht.ml) by [Tinloof](https://tinloof.com/)
