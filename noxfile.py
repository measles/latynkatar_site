import nox


nox.options.sessions = ["pretty", "black"]


@nox.session
def pretty(session):
    session.run("npx", "prettier", ".", "--check", external=True)


@nox.session
def prettier(session):
    session.run("npx", "prettier", ".", "--write", external=True)


@nox.session
def black(session):
    session.install("black")
    session.run("black", "--check", "main.py", "noxfile.py", "lib")


@nox.session
def black_diff(session):
    session.install("black")
    session.run("black", "--diff", "main.py", "noxfile.py", "lib")


@nox.session
def blacked(session):
    session.install("black")
    session.run("black", "main.py", "noxfile.py", "lib")


@nox.session
def install_pretty(session):
    session.run(
        "npm",
        "install",
        "s--save-dev",
        "--seva-extract",
        "'prettier@3.3.3'",
        external=True,
    )


@nox.session
def flask(session):
    session.run("flask", "run", *session.posargs, external=True)
