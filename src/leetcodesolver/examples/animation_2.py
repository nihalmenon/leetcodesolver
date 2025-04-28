
from manim import *

class GenScene(Scene):
    def construct(self):
        # Step 1: Introduce the problem
        array = [2, 7, 11, 15]
        target = 9
        array_text = Text(f"Array: {array}", font_size=36).to_edge(UP)
        target_text = Text(f"Target: {target}", font_size=36).next_to(array_text, DOWN)
        self.play(Write(array_text), Write(target_text))

        # Step 2: Iterate through the array
        hash_map = {}
        for i, num in enumerate(array):
            current_num_text = Text(f"Current Number: {num}", font_size=30).next_to(target_text, DOWN)
            complement = target - num
            complement_text = Text(f"Complement: {complement}", font_size=30).next_to(current_num_text, DOWN)
            self.play(Write(current_num_text), Write(complement_text))

            if complement in hash_map:
                # Highlight the pair
                pair_text = Text(f"Pair Found: ({complement}, {num})", font_size=30).next_to(complement_text, DOWN)
                indices_text = Text(f"Indices: ({hash_map[complement]}, {i})", font_size=30).next_to(pair_text, DOWN)
                self.play(Write(pair_text), Write(indices_text))
                break
            else:
                # Update hash map
                hash_map[num] = i
                hash_map_text = Text(f"Hash Map: {hash_map}", font_size=30).next_to(complement_text, DOWN)
                self.play(Write(hash_map_text))
                self.remove(current_num_text, complement_text, hash_map_text)

        # Step 3: Display the final result
        result_text = Text(f"Result: Indices ({hash_map[complement]}, {i})", font_size=36).next_to(indices_text, DOWN)
        self.play(Write(result_text))
