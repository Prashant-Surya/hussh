import click
import progressbar
import time
import uuid
import getpass
import socket

from hussh.api.setup import share_auth, create_hash, setup as setup_api
from hussh.utils.config import Config
from hussh.utils.constants import Constants, home
from hussh.utils.ssh import generate_ssh_keys
from hussh.api.file import upload_file

@click.option("--ssh", "-s", default=True)
@click.command()
def share(ssh):
    os_name = 'Linux'
    c = Config(os_name)
    username = c.read_key(Constants.CONFIG_USERNAME)
    api_key = c.read_key(Constants.CONFIG_KEY_API)
    if not username or not api_key:
        click.echo("Run `hussh setup` once before sharing")
        return
    click.echo("1. Authenticating with hussh server...")
    auth_token = share_auth(api_key, username)
    share_using_keys(auth_token)

def share_using_keys(auth_token):
    click.echo("2. Generating ssh keys...")
    public, private = generate_ssh_keys()
    unique_id = str(uuid.uuid4())
    click.echo("3. Storing public key...")
    public_file_name = home + "/.ssh/hussh-"+unique_id+".pub"
    with open(public_file_name, "w") as f:
        f.write(str(public, 'utf-8'))
    click.echo("4. Uploading private key to hussh server...")
    file_response = upload_file(auth_token, private, unique_id)
    if file_response.status_code != 200:
        click.echo("Failed to upload ssh key. Please try again")
        return
    click.echo("5. Generating unique id for sharing ...")

    os_name = 'Linux'
    c = Config(os_name)
    os_user = getpass.getuser()
    api_key = c.read_key(Constants.CONFIG_KEY_API)
    hostname = socket.gethostname()   
    ip = socket.gethostbyname(hostname)
    create_hash(api_key, unique_id, os_user, ip)

    out = "Ask the receiver to run `hussh connect {id}` for connecting to your system".format(id=unique_id)
    click.echo(out)