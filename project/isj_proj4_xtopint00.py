#!/usr/bin/env python3

def first_pair_given_sum(nums: list[int], target: int) -> tuple[int,int]|None:
    """Returns the tuple of two first numbers from the input list that sum up
       to the target, or None if no such numbers are in the list.

    >>> first_pair_given_sum([1,2,1,5,3,6], 12) 

    >>> first_pair_given_sum([1,2,5,3,6], 8)
    (5, 3)

    >>> first_pair_given_sum([6], 6)

    >>> first_pair_given_sum([1,2,2,5,3,6], 4)
    (2, 2)
    """

    oldMaxIndex = len(nums)

    result = None

    for firstIdx in range(0, len(nums)):
        
        for secondIdx in range(firstIdx, len(nums)):
            
            if firstIdx == secondIdx:
                
                continue
            
            firstNum = nums[firstIdx]
            secondNum = nums[secondIdx]

            maxIndex = max(firstIdx, secondIdx)

            if maxIndex > oldMaxIndex:
                
               continue

            if firstNum + secondNum == target:
                
                result = (firstNum, secondNum)
                oldMaxIndex = maxIndex

    return result

                                 # The number we need to reach the target
                               
                                 # Return the two numbers
                                 # Store the current number
                                 # Return None if no solution is found



def to_be_credited_alpha(lead_actors: list[str], 
                         actors_in_scenes: list[list[str]]
                        ) -> list[str]:
    """Returns the list of cast members that need to be credited at the end
       (are not among lead actors listed first) in alphabetical order.

    >>> to_be_credited_alpha(['Olivier', 'Caine', 'Channing'], [(1, ['Caine', 'Matthews']), (2, ['Olivier', 'Matthews', 'Martin']), (3, ['Morris', 'Caine', 'Cawthorne'])]) 
    ['Cawthorne', 'Martin', 'Matthews', 'Morris']
    """

    outputList = []

    for scene in actors_in_scenes:

      for actor in scene[1]:

         if actor not in lead_actors and actor not in outputList:

            outputList.append(actor)

    outputList.sort()

    return outputList



def order_of_appearance(actors_in_scenes: list[tuple[int, list[str]]]
                       ) -> list[str]:
    """Returns the list of cast members in order of appearance 
       (listed the first time they appear in a scene in the input list).

    >>> order_of_appearance([(1, ['Caine', 'Matthews']), (2, ['Olivier', 'Matthews', 'Martin']), (3, ['Morris', 'Caine', 'Cawthorne'])]) 
    ['Caine', 'Matthews', 'Olivier', 'Martin', 'Morris', 'Cawthorne']
    """

    actors_in_scenes_flat_list = [actor for (scene, cast) in actors_in_scenes for actor in cast]

    outputList = []

    for actor in actors_in_scenes_flat_list:
       
       if actor not in outputList:
          
            outputList.append(actor)

    return outputList


if __name__ == "__main__":
    import doctest
    doctest.testmod()
