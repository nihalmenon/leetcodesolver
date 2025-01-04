```
# Two Sum Algorithm Solution
=====================================

**Introduction**
---------------

The Two Sum algorithm is a popular solution for finding two numbers in an array that add up to a given target sum. This document provides a nicely formatted solution along with the code, incorporating embedded animation created by the Animator.

**Solution Overview**
-------------------

The provided Python script uses the Manim library to create an animated visualization of the Two Sum algorithm. The script defines a function `two_sum` that takes an array of numbers and a target sum as input, and returns the two numbers in the array that add up to the target sum. If no solution is found, it returns None.

**Code**
------

```python
from manim import *

class TwoSum(Scenario):
    def construct(self):
        # Define the function to be animated
        self.numbers = [3, 2, -1, 0, 4]
        self.target_sum = 6

        def two_sum(nums, target):
            num_map = {}
            for i in range(len(nums)):
                complement = target - nums[i]
                if complement in num_map:
                    return [complement, nums[i]]
                else:
                    num_map[nums[i]] = i
            return None

        # Create a number line for visualization
        num_line = NumberLine(radius=5)

        # Animate the algorithm working on the example
        self.play(Create(num_line))
        self.wait()

        # Iterate over each element in the array
        for num in self.numbers:
            self.play(Write(num, run_time=1))

            # Check if the current number is in the hashmap
            self.play(FadeOut(Vgroup(num, Text(f"HashMap: {num_map}", run_time=2))))

            # If it is, return the complement
            if num in num_map:
                self.play(
                    Indicate(self.target_sum - num, num_line),
                    Write(f"{self.target_sum - num} + {num} = {self.target_sum}", run_time=3)
                )
                self.wait(1)

                # Return the two numbers that add up to the target sum
                self.play(Rotate((0, 0), angle=np.pi / 2).set_size(10, scale_factor=1.5),
                          Write(f"Result: ({self.numbers[num_map[num]]}, {num})", run_time=4))
            else:
                # If not, add it to the hashmap
                self.play(
                    Indicate(num, num_line),
                    FadeOut(Vgroup(Text(f"HashMap: {num_map}", run_time=2))),
                    Write(f"{num} added to HashMap", run_time=3)
                )

            for i in range(len(self.numbers)):
                if i != len(self.numbers) - 1:
                    self.play(DrawLine(num_line.get_end() * i / (len(self.numbers) - 1),
                                       num_line.get_end(),
                                       color=WHITE))

        # Wait until the animation is complete
        self.wait()
```

**Animation Explanation**
------------------------

The animation demonstrates how the Two Sum algorithm works:

1.  The script starts by creating a number line and animating each element of the input array as it is processed.
2.  For each element, it checks if the current number is in the hashmap. If it is, it returns the complement (target sum minus the current number).
3.  If not, it adds the current number to the hashmap and continues with the next element.
4.  The script waits until the animation is complete before returning the final result.

**Output**
----------

When you run this script, it will create an animated visualization of the Two Sum algorithm, demonstrating how the hashmap is used to find the complement of each element in O(n) time complexity.