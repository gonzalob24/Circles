from check_circle_inside_another_circle import circle_inside_another_circle, verify_command_line_input, get_user_input


def main():
    """
    main function to execute code
    """

    if verify_command_line_input() is not None:
        c1_info, c2_info = verify_command_line_input()
        # information for each circle center and radius
        c1, r1 = c1_info
        c2, r2 = c2_info
        # Prints True or False
        print(circle_inside_another_circle(c1, r1, c2, r2))

        # Test cases within main. More unit tests are locates in test_cases
        try:
            assert circle_inside_another_circle(
                (0, 0), 4, (1, 1), 4) == False, "Test 1: Should be False"

            assert circle_inside_another_circle(
                (0, 0), 4, (0, 0), 9) == True, "Test 2: Should be True"
            assert circle_inside_another_circle(
                (-5, -3), 2, (-2, -2), 5) == False, "test 3: Should be False"

            print("3 tests passed!")
        except AssertionError as err:
            print(f'{err}')


if __name__ == "__main__":
    main()
