from git import Repo, exc
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import pyfiglet

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
            "-m"
        )
        git.reset("--hard", "HEAD~1")
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
    try:
        repo.git.add(all=True)
        cs.print("[green]Add . berhasil[/green]")
    except:
        cs.print("[bold red]Terjadi kesalahan![/bold red]")

def git_pull():
    try:
        origin = repo.remotes.origin
        origin.pull()
        cs.print("[green]Pull berhasil[/green]")
    except:
        cs.print("[bold red]Terjadi kesalahan![/bold red]")

def git_push(branch="main"):
    try:
        origin = repo.remotes.origin
        origin.push(branch)
        cs.print(f"[green]Push ke {branch} berhasil[/green]")
    except:
        cs.print("[bold red]Terjadi kesalahan![/bold red]")

def remote_url():
    try:
        cs.print(f"[bold yellow]{repo.remotes.origin.url}[/bold yellow]")  
    except Exception as e:
        cs.print(f"[bold red]Terjadi kesalahan: {e}[bold red]")

def add_commit_push(message):
    try:
        git_add_all()
        repo.git.commit("-m", message)
        cs.print("[bold green]Commit dibuat!")
        git_push("main")
        cs.print("[bold yellow]Pushing...[/bold yellow]")
        cs.print("[bold green]Push berhasil![/bold green]")
        remote_url() 
    except:
        cs.print("[bold red]Terjadi kesalahan![/bold red]")


def init_and_push(remote_url, message="Initial commit", require_gpg=False, repo_path=repo_path):
    cs.print("[bold yellow]Init dan push....[/bold yellow]")
    
    try:
        repo = Repo.init(repo_path)
        cs.print("[bold green]Init berhasil[/bold green]")
    except Exception:
        repo = Repo(repo_path)
        cs.print("[bold blue]Repo sudah ada, menggunakan repo yang tersedia[/bold blue]")

    repo.git.add(all=True)
    cs.print("[bold green]Add . berhasil[/bold green]")
    
    commit = repo.index.commit(commit_message)
    cs.print(f"[bold green]Commit berhasil: {commit.hexsha[:7]}\nPesan commit: {commit_message}[/bold green]")

    repo.git.branch('-M', 'main')

    try:
        origin = repo.create_remote('origin', remote_url)
    except exc.GitCommandError:
        origin = repo.remote(name='origin')
        with origin.config_writer as cw:
            cw.set("url", remote_url)
    
    cs.print(f"[bold yellow]Remote URL: {remote_url}[/bold yellow]") 

def current_branch():
    print(repo.active_branch.name)

def changes_diff():
    print(repo.git.diff(None))

def inform():
    ascii = pyfiglet.figlet_format("KIT", font="slant") 
    styled = Text(ascii, style="bold green")

    cs.print("Welcome to KIT", style="white")
    cs.print(styled)
    cs.print("Deskripsi", justify="center", style="dim")

    description = (
        "Kit adalah library CLI untuk mempermudah dan mempersingkat perintah git\n"
        "Perintah yang tersedia: gp|acp|gm|gaa|ru|cb|cd|gs|iap"
    )
    cs.print(Panel(description, border_style="bright_black"))
