import os
from datetime import datetime
from random import random


def increment_sample_counter(name, total):
    """
    Create or rename a counter file depending on the no of the current
    mosquitoes sample. The initial counter file needs to be in the root
    folder with this script...
    Example: An empty file called "sample_no_1.txt"

    :param total: Number
    :param name: String
    :return: Object
    """
    i = 0
    while i < total:
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


def mix_mosquitoes(samples_filename, num=2):
    with open(f"{samples_filename}.md", "a") as f:

        total_samples = 1000000
        number = increment_sample_counter('sample_no_', total_samples)

        if number != total_samples + 1:
            """
            We use a string representing the actual sample number with 7
            leading zeros.
            Example: "0000412"
            """
            new_sample_no = "%07d" % number

            f.write(f"\n```\n *===========================*"
                    f"\n | Sample Number:    {new_sample_no} |"
                    f"\n | Visible :             YES |"
                    f"\n | UV:             NO or YES |\n")

            print("\n *===========================*"
                  f"\n | Sample Number:    {new_sample_no} |"
                  f"\n | Visible :             YES |"
                  f"\n | UV:             NO or YES |")

            types = ["TO", "AE", "CT", "CP"]
            num = (1, num)[num > 0]
            n_side_len = 2 ** num
            shuffled = sorted([*types] * (4 ** (num - 1)),
                              key=lambda x: random())
            k = 0
            for i in range(n_side_len):
                row = " |  "
                sep = " *"
                for j in range(n_side_len):
                    row = f"{row}{shuffled[k]}  |  "
                    sep = f"{sep}------*"
                    k += 1

                f.write(f"{sep}\n{row}\n")
                print(f"{sep}\n{row}")
                pass

            nowTime = datetime.now().strftime('%Y.%m.%d %I:%M %p')
            f.write(" *------*------*------*------*"
                    "\n | TO: ..................... |"
                    "\n | AE: ..................... |"
                    "\n | CT: ..................... |"
                    "\n | CP: ..................... |"
                    "\n |                           |"
                    f"\n |       "
                    f"{nowTime} |"
                    "\n *------*------*------*------*"
                    "\n```\n")

            print(" *------*------*------*------*"
                  "\n | TO: ..................... |"
                  "\n | AE: ..................... |"
                  "\n | CT: ..................... |"
                  "\n | CP: ..................... |"
                  "\n |                           |"
                  f"\n |       "
                  f"{nowTime} |"
                  "\n *------*------*------*------*")
        else:
            print("GENERATING THE INITIAL FILE (sample_no_0) IN THE FOLDER")


if __name__ == "__main__":
    mix_mosquitoes("mix_mosquitoes", 2)
