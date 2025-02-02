import arel
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fletora.html import Tag
from fletora.plugins import spa_plugin


class App:
    _app: FastAPI | None = None
    _routes: dict[str, Tag] = {}

    def __new__(cls, *args, **kwargs):
        if cls._app is None:
            cls._app = FastAPI(*args, **kwargs)

        cls.mount()

        return cls

    @classmethod
    def add_route(cls, path, view):
        cls._routes[path] = view

    @classmethod
    def page(cls, path):
        def decorator(view):
            cls.add_route(path, view)
            return view

        return decorator

    @classmethod
    def mount(cls):
        hot_reload = arel.HotReload(paths=[arel.Path(".")])
        cls._app.add_websocket_route("/ws", route=hot_reload, name="ws")
        cls._app.add_event_handler("startup", hot_reload.startup)
        cls._app.add_event_handler("shutdown", hot_reload.shutdown)

        @cls._app.get("/{path:path}", response_class=HTMLResponse)
        async def root(path: str):
            path = "/" + path if path else "/"
            page = cls._routes.get(path, lambda: Tag("h1", "404 Not Found"))()

            return spa_plugin(page).render()
