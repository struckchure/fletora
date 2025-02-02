import uvicorn

from fletora import App
from fletora import Tag as t

app = App()._app  # if you are using FastAPI CLI
route = App().page


@route("/")
def home_page():
    return t(
        "div",
        t("h1", "Welcome to My SPA"),
        t("p", "This is the home page."),
        t("a", "Go to About", href="/about"),
        style="background-color: blue; color: white; padding: 10px;",
    )


@route("/about")
def about_page():
    return t(
        "div",
        t("h1", "About Us"),
        t("p", "This isthe about page."),
        t("a", "Go Home", href="/"),
    )


if __name__ == "__main__":
    uvicorn.run("example:app", reload=True)
