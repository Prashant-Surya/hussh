import click
import progressbar
import time
import uuid
import getpass

from hussh.api.setup import setup as setup_api
from hussh.utils.config import Config
from hussh.utils.constants import Constants, home
from hussh.utils.ssh import generate_ssh_keys
from hussh.api.file import upload_file
from hussh.utils.user import LinuxUser

@click.option('--user', '-u', default=True)
@click.command()
def setup(user):
    click.echo("Setting up the system for hussh....")
    os = 'Linux'
    c = Config(os)
    api_key = str(uuid.uuid4())
    uuid_str = uuid.uuid4().__str__().split('-')
    random_user = uuid_str[0]
    random_password = uuid_str[-1]
    if c.read_key(Constants.CONFIG_USERNAME) != None:
        click.echo("Setup already done.")
        return
    click.echo("Registering user in hussh...")
    data = setup_api(api_key, random_user, random_password)
    c.update_key(Constants.CONFIG_KEY_API, api_key)
    c.update_key(Constants.CONFIG_USERNAME, random_user)
    click.echo("Done. You're good to go.")
