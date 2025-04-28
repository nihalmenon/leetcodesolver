from manim import *

class TwoSum(Scene):
    def construct(self):
        self.numbers = [3, 2, -1, 0, 4]
        self.target_sum = 6

        # Title
        title = Text("Two Sum Algorithm").to_edge(UP)
        self.play(Write(title))

        # Create array visualization
        array_rects = VGroup(*[Square(side_length=0.8).set_stroke(WHITE, 2) for _ in self.numbers])
        array_rects.arrange(RIGHT, buff=0.1)
        array_nums = VGroup(*[Text(str(n), font_size=24).move_to(rect) for n, rect in zip(self.numbers, array_rects)])
        array = VGroup(array_rects, array_nums).next_to(title, DOWN, buff=0.5)

        # Target sum display
        target_text = Text(f"Target Sum: {self.target_sum}", font_size=30).next_to(array, DOWN, buff=0.5)

        # Hashmap visualization
        hashmap_title = Text("HashMap:", font_size=30).align_to(array, LEFT).shift(DOWN * 2)
        hashmap_box = Rectangle(width=5, height=2.5).next_to(hashmap_title, RIGHT, buff=0.2)
        hashmap = VGroup(hashmap_title, hashmap_box)
        hashmap_content = VGroup().move_to(hashmap_box)

        self.play(Create(array), Write(target_text), Create(hashmap))

        # Algorithm animation
        pointer = Arrow(start=UP, end=DOWN, color=YELLOW).scale(0.5).next_to(array_rects[0], UP, buff=0.1)
        self.play(Create(pointer))
        found = False
        for i, num in enumerate(self.numbers):
            # Move pointer
            self.play(pointer.animate.next_to(array_rects[i], UP, buff=0.1))
            
            complement = self.target_sum - num
            complement_text = Text(f"{self.target_sum} - {num} = {complement}", font_size=24).next_to(target_text, DOWN)
            self.play(Write(complement_text))

            # Check if complement in hashmap
            if any(item.text == str(complement) for item in hashmap_content):
                # Found a pair
                self.play(
                    array_rects[i].animate.set_fill(GREEN, opacity=0.5),
                    array_nums[i].animate.set_color(GREEN)
                )
                for j, item in enumerate(hashmap_content):
                    if item.text == str(complement):
                        self.play(
                            array_rects[j].animate.set_fill(GREEN, opacity=0.5),
                            array_nums[j].animate.set_color(GREEN)
                        )
                        break
                
                result_text = Text(f"Found pair: ({complement}, {num})", font_size=30).next_to(hashmap, DOWN)
                found = True
                self.play(Write(result_text))
                break
            else:
                # Add to hashmap
                new_entry = Text(f"{num}", font_size=24).move_to(hashmap_box)
                hashmap_content.add(new_entry)
                self.play(Write(new_entry))
                
                # Rearrange hashmap content
                hashmap_content.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
                hashmap_content.move_to(hashmap_box)
                self.play(hashmap_content.animate.move_to(hashmap_box))

            self.play(FadeOut(complement_text))

        if i == len(self.numbers) - 1 and not found:
            no_solution_text = Text("No solution found", font_size=30).next_to(hashmap, DOWN)
            self.play(Write(no_solution_text))

        self.wait(2)