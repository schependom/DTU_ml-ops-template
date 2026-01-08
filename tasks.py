from invoke import Context, task


@task
def template(ctx: Context, project_structure: str = "simple"):
    """Create a new project from the template."""
    if project_structure == "simple":
        ctx.run("cookiecutter -f --config-file configs/simple_config.yaml --no-input --verbose .")
    if project_structure == "advanced":
        ctx.run("cookiecutter -f --config-file configs/advanced_config.yaml --no-input --verbose .")


@task
def requirements(ctx: Context):
    """Install project requirements."""
    ctx.run("uv sync", echo=True, pty=True)


@task
def test(ctx: Context):
    """Run tests."""
    ctx.run("uv test", echo=True, pty=True)


@task
def clean(ctx: Context):
    """Clean up the project."""
    ctx.run("rm -rf repo_name")
    ctx.run("rm -rf simple_uv_repo")
    ctx.run("rm -rf advanced_uv_repo")
    ctx.run("rm -rf .pytest_cache")
    ctx.run("rm -rf .ruff_cache")


@task
def actions(ctx: Context):
    """Run Github actions."""
    ctx.run("act --list")
    ctx.run("act --artifact-server-path /tmp/artifacts")
