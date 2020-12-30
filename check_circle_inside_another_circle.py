import math
import sys
# from test_cases import TestSum


def circle_inside_another_circle(c1, r1, c2, r2):
    """
    Determines if a circle is inside of another circle.

    Parameters
    ----------

    c1 : (x, y), center of circle 1.
        Tuple

    c2 : (x, y), center of circle 2.
        Tuple

    r1 : radius of circle 1.
        integer or float

    r2 : radius of circle 2.
        integer or float

    Returns
    -------
    boolean : True a circle is inside another circle, False otherwise
    """
    # calculate the distance between the centers of two circles
    d = distance_between_two_circles(c1, c2)

    if d < abs(r2 - r1):
        return True
    return False


def distance_between_two_circles(c1, c2):
    """
    calculates the distance between the ceners of two circles.

    Parameters
    ----------
    c1 : (x, y), center of circle 1.
        Tuple

    c2 : (x, y), center of circle 2.
        Tuple

    Returns
    -------
    d : distance between the centers of two circles
        float
    """
    x1, y1 = c1
    x2, y2 = c2

    x2_x1 = (x2 - x1) ** 2
    y2_y1 = (y2 - y1) ** 2
    d = math.sqrt(x2_x1 + y2_y1)

    return d


def verify_command_line_input():
    """
    Checks for correct input entered via command line arguments

    """
    input_1 = sys.argv[1:4]
    input_2 = sys.argv[4:]
    # print(len(sys.argv[1:]))
    # print(input_2)

    try:
        if len(sys.argv[1:]) != 6:
            raise ValueError(
                "Enter a total of three values per input --> x y r: ")

        # # make sure data is a float even if user entered int.
        if isinstance(float(input_1[0]), float) is False or isinstance(float(input_1[1]), float) is False or \
                isinstance(float(input_1[2]), float) is False or isinstance(float(input_2[0]), float) is False or \
                isinstance(float(input_2[1]), float) is False or isinstance(float(input_2[2]), float) is False:
            raise ValueError

        # Break up the input
        x1, y1, r1 = float(input_1[0]), float(input_1[1]), float(input_1[2])
        x2, y2, r2 = float(input_2[0]), float(input_2[1]), float(input_2[2])

        if r1 <= 0 or r2 <= 0:
            raise ValueError("Radius must be greater than 0:")
        else:
            c1_info = ((x1, y1), r1)
            c2_info = ((x2, y2), r2)
            return c1_info, c2_info
    except ValueError as err:
        print(f'{err}')
        return None


def get_user_input():
    """
    Gets the input from the user via the terminal

    Returns
    -------
    c1_info : (x1, y1), r1 -- The center and radius of circle 1
            Tuple
    c2_info : (x2, y2), r2 -- The center and radius of circle 2
            Tuple
    """

    while True:
        input_1 = input("x1 y1 r1: ")
        input_2 = input("x2 y2 r2: ")
        input_1 = input_1.split()
        input_2 = input_2.split()

        if len(input_1) != 3 or len(input_2) != 3:
            print("Enter a total of three values per input --> x y r: ")
            continue
        try:
            # Break up the input
            x1, y1, r1 = float(input_1[0]), float(
                input_1[1]), float(input_1[2])
            x2, y2, r2 = float(input_2[0]), float(
                input_2[1]), float(input_2[2])
        except ValueError:
            try:
                x1, y1, r1 = int(input_1[0]), int(input_1[1]), int(input_1[2])
                x2, y2, r2 = int(input_2[0]), int(input_2[1]), int(input_2[2])
            except ValueError:
                print('Enter integers or float numbers only.')
                continue

        # radius needs to be greater than 0
        if r1 <= 0 or r2 <= 0:
            print("Radius must be greater than 0:")
            continue
        else:
            # store user input
            c1_info = ((x1, y1), r1)
            c2_info = ((x2, y2), r2)
            return c1_info, c2_info


if __name__ == "__main__":
    # verify_command_line_input()
    # c1, c2 = get_user_input()
    pass
