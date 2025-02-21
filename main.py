# Libraries

from InquirerPy import prompt
from rich.progress import Progress
from rich.console import Console
from time import sleep
import time



# Get user input for the project

console = Console()

questions = [
    {"type": "input", "name":"title", "message":"Enter your project title: "},
    {"type": "input", "name":"description", "message":"Describe your project: "},
    {"type": "input", "name":"installation", "message":"Installation instructions: "},
    {"type": "input", "name":"instructions", "message":"Usage instructions: "},
    {"type": "list", "name":"license", "message": "choose a license: ",
    "choices":["MIT License", "Apache license 2.0", "GNU GPL v3", "GNU LGPL v3",
    "Creative commons", "Mozilla public license", "Unlicense" ]},
    {"type": "input", "name":"author", "message":"Author: "},
]

results = prompt(questions)

# Formatting the content dynamically

readme_content = f"""

# Title
{results['title']}

# Descritption
{results['description']}

# Installation
{results['installation']}

# Instruction
{results['instructions']}

# License
{results['license']}

# Author
{results['author']}

"""
    
    
# Create a markdown file

with open("README.md", "w") as file:
    file.write(readme_content)

file.close()


# Progress Bar Simulation

data = [{results['title']}, {results['description']}, {results['installation']}, 
        {results['instructions']}, {results['license']}, {results['author']}]
with console.status("[bold green]Fetching data...") as status:
    while data:
        num = data.pop(0)
        sleep(1)
        console.log(f"[green]Finish writing[/green] {num}")

    console.log(f'[bold][red]Done!')


# Show a progress bar
with Progress() as progress:
    task = progress.add_task("Processing...", total=100)
    for _ in range(10):
        time.sleep(0.3)
        progress.update(task, advance=10)

console.print("[bold green]File Completed![/bold green] ✅")