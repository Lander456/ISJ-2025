#!/usr/bin/env python3

# ukol za 2 body
def halves_of_even_double_of_odd(numbers: list[int]) -> list[int]:
    """Re-arranges and re-calculates the given list of integers so that
       halves of even numbers will go first, followed by doubles of odd ones

    >>> halves_of_even_double_of_odd([2,4,2,5,6])
    [1, 2, 1, 3, 10]
    >>> halves_of_even_double_of_odd([3,2,0,5,4])
    [1, 0, 2, 6, 10]
    >>> halves_of_even_double_of_odd([2])
    [1]
    >>> halves_of_even_double_of_odd([])
    []
    >>> halves_of_even_double_of_odd([3])
    [6]
    """

    lastEvenIndex = 0

    for num in numbers:

        if num % 2 == 0:

            numbers.remove(num)

            num = int(num / 2)

            numbers.insert(lastEvenIndex, num)

            lastEvenIndex += 1

        else:

            index = numbers.index(num)

            num = int(num * 2)

            numbers[index] = num

    return numbers

# ukol za 3 body
def multichoice_scoring(answers: list[int],
                        scoring: list[tuple[int, float, float]]
                        ) -> float:
    """Scores and return the answers to a multi-choice test
       (with exactly one correct answer per question).
       The choices selected by a participant are listed in answers, 
       if there were 3 questions and the participant selected the 1st option 
       for the 1st question, did not answer the second, and took the 2nd option
       for the 3rd question, the input shall correspond to [0, None, 1]
       Parameter scoring corresponds to the list of triples consisting of:
       - identification (index) of the right answer;
       - number of points for the right answer to the question;
  
            - negative number of points to be counted, if the answer is incorrect.
       Zero points should be given for non-answered questions.
       The answers and scoring lists should have the same length
       (does not need to be tested) and share the ordering of the questions.

    >>> multichoice_scoring([], [])
    0
    >>> multichoice_scoring([3, 4, None, 0], [(2, 3.5, -1.5), (4, 3, -1.5), (2, 2, -1), (0, 2, -1)])
    3.5
    """

    total = 0

    zippedList = list(zip(answers, scoring))

    for item in zippedList:

        if item[0] == item[1][0]:

            total += item[1][1]

        elif item[0] is None:

            continue

        else:

            total += item[1][2]

    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()
