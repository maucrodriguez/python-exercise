import click
from cfn_flip import to_json as yaml_to_json
from utils import is_palindrome
from django.core import management

DIRECTORY_DESTINATION = "part2"


@click.group()
def main():
    """
    Thank you for asking for help.
    These tools are used to generate a Django project and convert CloudFormation code from YAML to JSON
    """
    pass


@main.command()
@click.argument("project_name")
def check_project_name(project_name):
    click.echo(
        f'{project_name} is{"" if is_palindrome(project_name) else " not"} a palindrome'
    )


@main.command()
@click.argument("project_name")
def start_django_project(project_name):
    if not is_palindrome(project_name):
        click.echo("Project name is not palindrome")
    else:
        management.call_command(
            "startproject", project_name, directory=DIRECTORY_DESTINATION
        )


@main.command()
@click.argument("file_path")
def convert_to_json(file_path):
    try:
        with open(file_path) as input_file:
            with open("output.json", "w") as output_file:
                output_file.write(yaml_to_json(input_file.read()))
                click.echo(f"File converted and placed at {output_file.name}")
    except Exception as e:
        click.echo(f"Could not find file located at {file_path}")


if __name__ == "__main__":
    main()
