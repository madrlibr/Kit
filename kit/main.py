from git import Repo, exc
from rich.console import Console


cs = Console()
repo_path = "./"

try:
    repo = Repo(repo_path)
except exc.InvalidGitRepositoryError:
    repo = None


def can_sign_commit(repo):
    try:
        repo.git.commit(
            "--allow-empty",
            "-S",
            "-m",
            "gpg-sign-test"
        )
        repo.git.reset("--hard", "HEAD~1")
        return True
    except Exception as e:
        cs.print(f"[red]GPG signing tidak tersedia:[/red] {e}")
        return False


def commit(message, require_gpg=False):
    if require_gpg:
        if not can_sign_commit(repo):
            raise RuntimeError("GPG diperlukan tapi tidak bisa digunakan")

    try:
        repo.git.commit("-S", "-m", message)
        cs.print("[bold green]Commit dibuat dengan signature GPG[/bold green]")
        return "signed"
    except Exception as e:
        cs.print(f"[yellow]Commit signed gagal:[/yellow] {e}")

        repo.git.commit("--no-gpg-sign", "-m", message)
        cs.print("[bold yellow]Commit dibuat TANPA signature[/bold yellow]")
        return "unsigned"


def git_status():
    cs.print(f"[gray]{repo.git.status()}[/gray]")


def git_add_all():
    repo.git.add(all=True)
    cs.print("[green]Add . berhasil[/green]")


def git_pull():
    origin = repo.remotes.origin
    origin.pull()
    cs.print("[green]Pull berhasil[/green]")


def git_push(branch="main"):
    origin = repo.remotes.origin
    origin.push(branch)
    cs.print(f"[green]Push ke {branch} berhasil[/green]")


def add_commit_push(message, require_gpg=False):
    git_add_all()

    try:
        commit(message, require_gpg=require_gpg)
    except:
        repo.git.commit("-m", message)
        cs.print("[bold green]Commit dibuat tanpa signature GPG[/bold green]")

    git_push("main")
    cs.print("[bold green]Push berhasil![/bold green]")

def init_and_push(remote_url, commit_message="Initial commit", require_gpg=False):
    global repo

    try:
        repo = Repo.init(repo_path)
        cs.print("[green]Repository di-init[/green]")
    except Exception:
        repo = Repo(repo_path)
        cs.print("[blue]Repo sudah ada[/blue]")

    repo.git.add(all=True)
    commit(commit_message, require_gpg=require_gpg)

    repo.git.branch("-M", "main")

    try:
        origin = repo.create_remote("origin", remote_url)
    except exc.GitCommandError:
        origin = repo.remote("origin")
        with origin.config_writer as cw:
            cw.set("url", remote_url)

    origin.push("--set-upstream", "origin", "main")
    cs.print("[green]Push awal selesai[/green]")

def remote_url():
    try:
        cs.print(f"[bold yellow]{repo.remotes.origin.url}[/bold yellow]")  
    except Exception as e:
        cs.print(f"[bold red]Terjadi kesalahan: {e}[bold red]")

def current_branch():
    print(repo.active_branch.name)

def changes_diff():
    print(repo.git.diff(None))