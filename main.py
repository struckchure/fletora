import arel
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fletora import Tag as t
from fletora import spa_plugin

app = FastAPI()


def home_page():
    return t(
        "div",
        t("h1", "Welcome to My SPA"),
        t("p", "This is the home page."),
        t("a", "Go to About", href="/about"),
        style="background-color: black; color: white; padding: 10px;",
    )


def about_page():
    return t(
        "div",
        t("h1", "About Us"),
        t("p", "This isthe about page."),
        t("a", "Go Home", href="/"),
    )


routes = {
    "/": home_page,
    "/about": about_page,
}


@app.get("/{path:path}", response_class=HTMLResponse)
async def root(path: str):
    path = "/" + path if path else "/"
    page = routes.get(path, lambda: t("h1", "404 Not Found"))()

    return spa_plugin(page).render()


hot_reload = arel.HotReload(paths=[arel.Path(".")])
app.add_websocket_route("/ws", route=hot_reload, name="ws")
app.add_event_handler("startup", hot_reload.startup)
app.add_event_handler("shutdown", hot_reload.shutdown)
