from clidam.console import console
from clidam.deviantart import da

from rich.table import Table
import ascii_magic


def main():
    console.width = 80
    console.clear()
    daily = da.browse_dailydeviations()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style = "dim", width = 3)
    table.add_column("Title")
    table.add_column("Author")

    for i, dev in enumerate(daily):
        table.add_row(f"{i + 1}", dev.title, dev.author.username)

    console.rule("Daily Deviations")
    console.print(table)

    img = daily[0]
    url = img.thumbs[0]["src"]

    dev0 = ascii_magic.from_url(url, columns = 80)
    ascii_magic.to_terminal(dev0)
    print(url)

if __name__ == "__main__":
    main()
