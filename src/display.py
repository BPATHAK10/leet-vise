from rich.console import Console
from rich.panel import Panel

console = Console()

class Display:
    @staticmethod
    def welcome():
        console.print(Panel.fit(
            """Welcome to [bold cyan]Leet-Vise[/bold cyan] - your LeetCode revision companion!

Commands during timer:
  [bold]h[/bold] - Show hint
  [bold]s[/bold] - Show solution
  [bold]e[/bold] - End current question early
  [bold]q[/bold] - Quit the program

Press [bold]ENTER[/bold] to start...
""", title="Leet-Vise", subtitle="Happy Coding!"))

    @staticmethod
    def show_question(question):
        console.print(Panel.fit(f"[bold]{question['title']}[/bold]\n[blue]{question['url']}[/blue]"))

    @staticmethod
    def show_hint(hint):
        console.print(Panel(hint or "[italic]No hint available.[/italic]", title="Hint"))

    @staticmethod
    def show_solution(solution):
        console.print(Panel(solution or "[italic]No solution available.[/italic]", title="Solution"))
