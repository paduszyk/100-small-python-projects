import random
from datetime import date, timedelta


def get_birthdays(num_people: int, leap_year: bool = False) -> list[date]:
    """Return birthdays for a specified number of random people."""
    # Handle leap years
    year, days_per_year = (2020, 366) if leap_year else (2021, 365)
    return [
        date(year, 1, 1) + timedelta(days=random.randint(0, days_per_year - 1))
        for _ in range(num_people)
    ]


def birthday_match_found(birthdays: list[date]) -> bool:
    """Return a bool indicating if there are at least two the same birthdays
    found in the specified birthdays list."""
    while birthdays:
        birthday = birthdays.pop()
        if birthday in birthdays:
            break
    else:
        return False
    return True


def simulation(
    num_people: int | None = 23,
    num_tests: int = 100_000,
    verbose_every: int = 0,
    leap_year: bool = False,
) -> None:
    """Perform birthday paradox simulation.

    Estimate probability of having birthday match in a group of people
    of the specified size `num_people` using `num_tests`randomized
    matching tests.
    """
    print("Birthday problem/paradox simulation", end="\n" * 2)

    if num_people is None:
        num_people = int(input("Specify the number of people: "))

    input(f"Press Enter to run the simulation for {num_people} people...")

    def match_rate(num_matches: int, num_tests: int) -> float:
        """Return match rate based on a number of matches."""
        return num_matches / num_tests * 100

    num_matches = 0
    for test_index in range(num_tests):
        num_matches += birthday_match_found(
            get_birthdays(
                num_people,
                leap_year,
            )
        )

        if verbose_every and test_index % verbose_every == 0:
            print(
                "{} tests performed, birthday match rate = {:.1f}".format(
                    test_index,
                    match_rate(num_matches, test_index + 1),
                )
            )

    print(
        (
            "\n"
            "Simulation completed. {} tests were run.\n"
            "Estimated probability of birthday match equals {:.1f}%."
        ).format(num_tests, match_rate(num_matches, num_tests)),
        end="\n" * 2,
    )


def main() -> None:
    """Run the simulation by using default settings."""
    simulation()


if __name__ == "__main__":
    main()
