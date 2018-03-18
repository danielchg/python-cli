import click
from click.testing import CliRunner
import cli

def test_cli():
    @click.command()
    @click.argument('name')
    runtest = CliRunner()
    result = runtest.invoke(cli, input='dani\n')
    assert not result.exception
    assert resutl.output == 'Your Name: dani\nHello dani!\n'
