import argparse
import subprocess

from fasthtml.common import *

parser = argparse.ArgumentParser(
    prog="Fast HTML + Tailwind template",
    description="FastHTML template using Tailwind CSS for styling",
)
parser.add_argument(
    "--tailwind",
    type=bool,
    default=False,
    help="Run the Tailwind CLI build or not",
)
args = parser.parse_args()

hdrs = [
    Meta(charset="UTF-8"),
    Meta(
        name="viewport",
        content="width=device-width, initial-scale=1.0, maximum-scale=1.0",
    ),
    Meta(
        name="description", content="FastHTML template using Tailwind CSS for styling"
    ),
    Link(href="css/output.css", rel="stylesheet"),
]

# For now, fast_app and rt are necessary for Tailwind to work properly
app, rt = fast_app(hdrs=hdrs, default_hdrs=False, pico=False)


def home_hero_section():
    return Section(
        H1(
            "This is a ",
            A(
                Img(
                    src="images/fast_html_logo-cropped.svg",
                    alt="FastHTML logo",
                    width="200",
                    height="200",
                    cls="inline",
                ),
                href="https://fastht.ml",
            ),
            "demo using",
            A(
                Img(
                    src="images/tailwindcss-logotype.svg",
                    alt="Tailwind CSS logo",
                    width="300",
                    height="300",
                    cls="inline",
                ),
                href="https://tailwindcss.com/",
            ),
            "for styling",
            cls="font-bold text-5xl",
        ),
        P(
            "No .js file except tailwind.config. Tailwind CSS is the only package needed. Node is used only to have a universal install.",
            cls="text-gray-500",
        ),
        A(
            Button(
                "Start coding",
                Img(
                    src="images/github-mark-cropped.svg",
                    alt="Tailwind CSS logo",
                    width="40",
                    height="40",
                    cls="inline",
                ),
                cls="bg-blue-500 text-white text-2xl font-bold rounded-full px-4 py-2 hover:scale-105 hover:-translate-y-2 hover:bg-blue-300 transition-all",
            ),
            href="https://github.com/ninohdasilva/fasthtml-tailwind-template",
        ),
        cls="home-hero-section flex flex-col items-center contents-center pt-8 gap-4",
    )


def home():
    return Main(
        home_hero_section(),
        cls="container w-full mx-auto flex flex-col items-center justify-center px-8",
    )


@rt("/")
def get():
    return home()


if args.tailwind:
    subprocess.run(
        ["npx", "tailwindcss", "-i", "css/input.css", "-o", "css/output.css"]
    )
serve()
