"""
This program was written to trim the unnecessary numbers and timestamps from a zoom transcript
that I was attaching to a class project. As it would have been tedious to go through and erase
all ~800 lines, I wrote this program.
"""

BAD_STUFF = range(400)

def main():
    with open("transcript.txt") as file:
        write_file = open("clean_transcript.txt", "w")
        next(file)
        for line in file:
            bees = 0
            line = line.strip()
            tokens = line.split(":")
            if line == "":
                continue
            if tokens[0] == "00":
                continue
            for num in BAD_STUFF:
                try:
                    if int(line) == num:
                        bees = 1
                        break
                except:
                    pass
            if bees == 0:
                write_file.write(line)
                write_file.write("\n")

main()