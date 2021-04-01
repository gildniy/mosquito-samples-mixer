import datetime
import os
import random


def increment_sample_counter(name):
    """
    Create or rename a counter file depending on the no of the current
    mosquitoes sample. The initial counter file needs to be in the root
    folder with this script...
    Example: An empty file called "sample_no_1.txt"

    :param name: String
    :return: Object
    """
    i = 0
    while i < 1000000:
        """
        A 7 is a ten digit number, it can be relatively large 
        and cannot be reached easily.
        Example: 921559
        """
        if os.path.exists(f"{name}%s" % i):
            os.rename(f"{name}%s" % str(i), f"{name}%s" % str(i + 1))
            break
        i += 1
    else:
        with open('sample_no_0', "w"):
            pass

    return i + 1


def mix_mosquitoes(samples_filename):
    number = increment_sample_counter('sample_no_')

    if number != 0:

        with open(f"{samples_filename}.txt", "a") as f1:
            types = ("TO", "AE", "CT", "CP")
            has_visible = 'YES'
            has_uv = 'NO or YES'

            """
            We use a string representing the actual sample number with 7
            leading zeros.
            Example: "0000412"
            """
            new_sample_no = "%07d" % number

            # Table with sample identification details
            f1.write("\n\n *===========================*"
                     f"\n | Sample Number:    {new_sample_no} |"
                     f"\n | Visible :             {has_visible} |"
                     f"\n | UV:             {has_uv} |\n"
                     )

            print("\n *===========================*"
                  f"\n | Sample Number:    {new_sample_no} |"
                  f"\n | Visible :             {has_visible} |"
                  f"\n | UV:             {has_uv} |")

            for i in range(4):
                _sorted = sorted(types, key=lambda x: random.random())

                row = " |  "
                sep = " *"

                for j in range(4):
                    row = row + _sorted[j] + "  |  "
                    sep = sep + "------*"

                f1.write(f"{sep}\n{row}\n")
                print(f"{sep}\n{row}")

            # Tables footer with Term Mappings
            f1.write(" *------*------*------*------*"
                     "\n | TO: ..................... |"
                     "\n | AE: ..................... |"
                     "\n | CT: ..................... |"
                     "\n | CP: ..................... |"
                     "\n |                           |"
                     f"\n |       "
                     f"{datetime.datetime.now().strftime('%Y.%m.%d %I:%M %p')} |"
                     "\n *------*------*------*------*")

            print(" *------*------*------*------*"
                  "\n | TO: ..................... |"
                  "\n | AE: ..................... |"
                  "\n | CT: ..................... |"
                  "\n | CP: ..................... |"
                  "\n |                           |"
                  f"\n |       "
                  f"{datetime.datetime.now().strftime('%Y.%m.%d %I:%M %p')} |"
                  "\n *------*------*------*------*")
    else:
        print("GENERATING THE INITIAL FILE (sample_no_0) IN THE FOLDER")


if __name__ == "__main__":
    mix_mosquitoes("mix_mosquitoes")
