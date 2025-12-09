from core.logger import Logger


class Log:
    def msg(status: str) -> None:
        Logger.log(status, "logs.vs", "./logs/")


class SearchCommand:
    def __init__(self) -> None:
        pass

    def execute(self, exploits: list, search_term: str) -> None:
        matching_exploits = [
            exploit
            for exploit in exploits
            if (
                search_term.lower() in exploit.name.lower()
                or search_term.lower() in exploit.author.lower()
                or search_term.lower() in exploit.description.lower()
            )
        ]

        if matching_exploits:
            print(
                f"\n    Search Results for '{search_term}'\n    {'=' * (24 + len(search_term))}"
            )
            print("""
    #   Name               Author         Date              Description
    -   ----               ------         ----              -----------""")
            for i, exploit_instance in enumerate(matching_exploits, 1):
                print(
                    f"    {i: <4}{exploit_instance.name: <19}{exploit_instance.author: <15}{exploit_instance.creation_date: <18}{exploit_instance.description}"
                )
            print()
        else:
            print(" ")
            Log.msg(f"No results found for -> {search_term}\n")

