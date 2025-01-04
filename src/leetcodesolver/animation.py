from manim import *

class TwoSumAnimation(Scene):
    def construct(self):
        # Create the input list and target value
        nums = [2, 7, 11, 15]
        target = 9

        # Create a dictionary to store the numbers and their indices
        num_map = VGroup()

        # Iterate through the input list
        for i in range(len(nums)):
            # Display the current number and its index
            text = Text("Number: " + str(nums[i]) + ", Index: " + str(i))
            self.add(text)

            # Check if the complement of the current number exists in the dictionary
            if (target - nums[i]) in num_map:
                # If it does, display a message indicating that we've found the solution
                text = Text("Solution found! Indices are: " + str(num_map[(target - nums[i])] + "," + str(i)), color=GREEN)
                self.add(text)

                # Display the indices of the numbers that add up to the target value
                result = num_map[(target - nums[i])]
                result = Tex(r"\boxed{" + str(result) + "}").next_to(text, RIGHT)
                self.add(result)
            else:
                # If it doesn't, add the current number and its index to the dictionary
                VGroup(num=Tex(r"num[" + str(nums[i]) + "]=" + str(i)), map=Tex(r"map[" + str(nums[i]) + "]=" + str(i))).add_to(num_map)

            # Display a pause before moving on to the next number
            self.wait(2)

        # If no solution is found, display a message indicating that
        if num_map == VGroup():
            text = Text("No solution found!", color=RED)
            self.add(text)

class Example(Scene):
    def construct(self):
        nums1 = [2, 7, 11, 15]
        target1 = 9

        # Create a dictionary to store the numbers and their indices
        num_map = VGroup()

        # Iterate through the input list
        for i in range(len(nums1)):
            # Display the current number and its index
            text = Text("Number: " + str(nums1[i]) + ", Index: " + str(i))
            self.add(text)

            # Check if the complement of the current number exists in the dictionary
            if (target1 - nums1[i]) in num_map:
                # If it does, display a message indicating that we've found the solution
                text = Text("Solution found! Indices are: " + str(num_map[(target1 - nums1[i])] + "," + str(i)), color=GREEN)
                self.add(text)

                # Display the indices of the numbers that add up to the target value
                result = num_map[(target1 - nums1[i])]
                result = Tex(r"\boxed{" + str(result) + "}").next_to(text, RIGHT)
                self.add(result)
            else:
                # If it doesn't, add the current number and its index to the dictionary
                VGroup(num=Tex(r"num[" + str(nums1[i]) + "]=" + str(i)), map=Tex(r"map[" + str(nums1[i]) + "]=" + str(i))).add_to(num_map)

            # Display a pause before moving on to the next number
            self.wait(2)

        # If no solution is found, display a message indicating that
        if num_map == VGroup():
            text = Text("No solution found!", color=RED)
            self.add(text)