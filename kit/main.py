from git import Repo, exc
from rich.console import Console

cs = Console()
repo_path = './'   
try:
    repo = Repo(repo_path)
except:
    repo = None 

def git_status():
    output = repo.git.status()
    cs.print(f"[bold gray]{output}[/bold gray]")

def git_add_all():
    repo.git.add(all=True) 
    cs.print("[bold green]Add . berhasil[/bold green]")

def git_commit(message):
    commit = repo.index.commit(message)
    cs.print(f"[bold green]Commit berhasil: {commit.hexsha}\nPesan commit: {message}[/bold green]")

def git_pull():
    origin = repo.remotes.origin
    output = origin.pull()
    print(output)
    cs.print("[bold green]Pull berhasil[/bold green]")

def git_push_main():
    origin = repo.remotes.origin
    print(origin.push('main'))

def remote_url():
    cs.print(f"[bold yellow]{repo.remotes.origin.url}[/bold yellow]")   

def current_branch():
    print(repo.active_branch.name)

def changes_diff():
    print(repo.git.diff(None))

def push_all_main(message):
    repo.git.add(all=True) 
    cs.print("[bold green]Add . berhasil[/bold green]")
    commit = repo.index.commit(message)
    cs.print(f"[bold green]Commit berhasil: {commit.hexsha}\nPesan commit: {message} [/bold green]")
    origin = repo.remotes.origin
    print(f"[bold green]{origin.push('main')}[/bold green]")
    cs.print("[bold green]Push berhasil![/bold green]")

def initi_and_push(remote_url, repo_path='./', commit_message="First commit"):
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

    try:
        repo.git.push('--set-upstream', 'origin', 'main')
        cs.print("[bold green]Push berhasil![/bold green]")
    except Exception as e:
        cs.print(f"[bold red]Gagal push: {e}[/bold red]")


