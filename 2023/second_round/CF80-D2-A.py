def check_if_number_is_prime(odd_number: int) -> bool:
    for divisor in range(3, odd_number):
        if odd_number % divisor == 0:
            return False
    return True


def main():
    soldiers_beated_on_first_day, soldiers_beated_on_second_day = map(int, input().split())

    is_number_of_second_day_soldiers_beated_not_prime = (soldiers_beated_on_second_day % 2 == 0 or
                                                         not check_if_number_is_prime(soldiers_beated_on_second_day))
    if is_number_of_second_day_soldiers_beated_not_prime:
        print("NO")
    else:
        prime_found_between_then = False
        add_for_the_next_odd_number = 1 if soldiers_beated_on_first_day == 2 else 2

        for number in range(soldiers_beated_on_first_day + add_for_the_next_odd_number,
                            soldiers_beated_on_second_day, 2):
            prime_found_between_then = check_if_number_is_prime(number)
            if prime_found_between_then:
                break

        print("NO" if prime_found_between_then else "YES")


if __name__ == "__main__":
    main()
