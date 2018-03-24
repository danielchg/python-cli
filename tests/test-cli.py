import click
from click.testing import CliRunner
from cli.cli import main

def test_cli():
  runner = CliRunner()
  result = runner.invoke(main, input='dani\n')
  assert not result.exception
  assert result.output == 'Your Name: dani\nHello dani!\n'
