import click
import os

from hussh.api.file import download_file
from hussh.api.setup import share_auth, get_hash
from hussh.utils.constants import Constants, home
from hussh.utils.config import Config

@click.command()
@click.argument('file_id')
def connect(file_id):
    os_name = 'Linux'
    c = Config(os_name)
    username = c.read_key(Constants.CONFIG_USERNAME)
    api_key = c.read_key(Constants.CONFIG_KEY_API)
    if not username or not api_key:
        click.echo("Run `hussh setup` once before sharing")
        return
    click.echo("1. Authenticating with hussh server...")
    auth_token = share_auth(api_key, username)
    click.echo("2. Fetching ssh key...")
    pub_file = download_file(auth_token, file_id)

    file_path = home + "/.ssh/"+file_id
    with open(file_path, 'w') as f:
        f.write(pub_file)
    hash_data = get_hash(file_id)
    os_user = hash_data['os_user']
    ip = hash_data['ip']

    ssh_command = "ssh -i {file_path} {user}@{ip}".format(file_path=file_path, user=os_user,ip=ip)
    click.echo("3. Starting ssh connection...")
    click.echo("Running command "+ssh_command)
    os.system(ssh_command)
