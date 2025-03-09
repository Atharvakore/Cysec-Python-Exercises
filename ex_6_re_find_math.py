import re


def find_math(text: str) -> set:
    # TODO: implement
    # remember to round the results to two decimal places
    pass


if __name__ == '__main__':
    assert (find_math('U}Jaq^oJ!39xinp)n}SKM~v1lK&Z]?b}>v&B|zRd@*igJ417-\t899>3>&672\t/\t782>wokY412/\x0b417kN200/ '
                      '776I+347\x0c/ 750^QcAAC\'7hYA6JyU`<gJ"bD&utab895\n/\x0c80}X|}p1jQk2nmm}HM!wo7zZ_9q=+U`a$`G{'
                      '}LUoC95Nab>^".OMq)\'z(G$f_996\n+\t294^fr=5L^OPW_u|884\x0c/\r334p945\t+\t640,'
                      '^Jp.jl$W5}.560\n*\x0c206+$,/iYng=M%!e+9+') == {0.86, 0.99, 0.26, 2.65, 0.46, 115360, 1290,
                                                                      11.19, 1585, -482})
