from .html import Tag as t


def spa_plugin(child: t):
    """Wrap the content in a basic HTML structure."""
    return t(
        "html",
        t(
            "body",
            t("div", child.render(), id="app"),  # Load content dynamically
            t(
                "script",
                """
                    // WebSocket for listening to file changes
                    const socket = new WebSocket("ws://localhost:8000/ws");

                    socket.onmessage = function(event) {
                        if (event.data === "reload") {
                            location.reload();  // Reload the page if a change is detected
                        }
                    };

                    document.addEventListener('click', function(event) {
                        // Check if the clicked element is a link (<a> tag)
                        let target = event.target.closest("a");
                        if (target && target.href && target.href.startsWith(window.location.origin)) {
                            event.preventDefault();  // Prevent the default link behavior (full-page reload)
                            navigate(event, target.getAttribute("href"));  // Call custom navigate function
                        }
                    });

                    function navigate(event, path) {
                        event.preventDefault();  // Prevent default behavior
                        history.pushState({}, '', path);  // Update the browser's URL without reloading the page
                        loadPage(path);  // Load the content for the new page
                    }

                    function loadPage(path) {
                        fetch(path)
                            .then(response => response.text())
                            .then(pageContent => {
                                document.getElementById('app').innerHTML = pageContent;
                            })
                    }

                    window.onload = function () {
                        loadPage(window.location.pathname);  // Load the page when the window is first loaded
                    };

                    window.onpopstate = function () {
                        loadPage(window.location.pathname);  // Handle back/forward navigation
                    };
                """,
            ),
        ),
    )
