from git import Repo, exc
from rich.console import Console
import shutil

cs = Console()
repo_path = './'   
try:
    repo = Repo(repo_path)
except:
    repo = None 

def is_gpg_available():
    return shutil.which('gpg') is not None


def git_status():
    output = repo.git.status()
    cs.print(f"[bold gray]{output}[/bold gray]")


def git_add_all():
    try:
        repo.git.add(all=True) 
        cs.print("[bold green]Add . berhasil[/bold green]")
    except Exception as e:
        cs.print(f"[bold red]Terjadi kesalahan: {e}[bold red]")
    

def git_commit(message):
    try:
        if is_gpg_available():
            repo.git.commit('-S', '-m', message)
            cs.print("[bold green]Commit berhasil (Verified)![/bold green]")
        else:
            raise Exception("GPG not found")
    except Exception:
        repo.git.commit('-m', message)
        cs.print("[bold yellow]GPG tidak tersedia/gagal. Commit berhasil (Unverified).[/bold yellow]")


def remote_url():
    try:
        cs.print(f"[bold yellow]{repo.remotes.origin.url}[/bold yellow]")  
    except Exception as e:
        cs.print(f"[bold red]Terjadi kesalahan: {e}[bold red]")


def git_pull():
    origin = repo.remotes.origin
    output = origin.pull()
    print(output)
    cs.print("[bold green]Pull berhasil[/bold green]")


def git_push_main(message):
    cs.print("[bold yellow]Add all...[/bold yellow]")
    repo.git.add(all=True) 
    cs.print("[bold green]Add . berhasil[/bold green]")
    
    cs.print("[bold yellow]Committing...[/bold yellow]")
    try:
        repo.git.commit('-S', '-m', message)
        cs.print("[bold green]Commit Verified berhasil![/bold green]")
    except Exception:
        repo.git.commit('-m', message)
        cs.print("[bold yellow]Commit Unverified berhasil![/bold yellow]")

    cs.print("[bold yellow]Pushing...[/bold yellow]")
    origin = repo.remotes.origin
    origin.push('main')
    cs.print("[bold green]Push ke main berhasil![/bold green]")


def current_branch():
    print(repo.active_branch.name)


def changes_diff():
    print(repo.git.diff(None))


def push_all_main(message):
    cs.print("[bold yellow]Add all...[/bold yellow]")
    repo.git.add(all=True) 
    
    cs.print("[bold yellow]Committing...[/bold yellow]")
    try:
        repo.git.commit('-S', '-m', message)
        cs.print("[bold green]Commit Verified berhasil![/bold green]")
    except Exception:
        cs.print("[bold red]GPG gagal, mencoba commit tanpa signature...[/bold red]")
        repo.git.commit('--no-gpg-sign', '-m', message)
        cs.print("[bold yellow]Commit Unverified berhasil (GPG dilewati).[/bold yellow]")


def initi_and_push(remote_url, repo_path='./', commit_message="First commit"):
    cs.print("[bold yellow]Init dan push....[/bold yellow]") 
    try:
        local_repo = Repo.init(repo_path)
        cs.print("[bold green]Init berhasil[/bold green]")
    except Exception:
        local_repo = Repo(repo_path)
        cs.print("[bold blue]Repo sudah ada, menggunakan repo yang tersedia[/bold blue]")

    local_repo.git.add(all=True)
    
    try:
        local_repo.git.commit('-S', '-m', commit_message)
        cs.print(f"[bold green]Commit Verified: {commit_message}[/bold green]")
    except:
        local_repo.git.commit('-m', commit_message) # Tadi kamu tulis 'm', harusnya '-m'
        cs.print(f"[bold yellow]Commit Unverified: {commit_message}[/bold yellow]")

    local_repo.git.branch('-M', 'main')

    try:
        origin = local_repo.create_remote('origin', remote_url)
    except exc.GitCommandError:
        origin = local_repo.remote(name='origin')
        with origin.config_writer as cw:
            cw.set("url", remote_url)
    
    cs.print(f"[bold yellow]Remote URL: {remote_url}[/bold yellow]")

    try:
        local_repo.git.push('--set-upstream', 'origin', 'main')
        cs.print("[bold green]Push berhasil![/bold green]")
    except Exception as e:
        cs.print(f"[bold red]Gagal push: {e}[/bold red]")