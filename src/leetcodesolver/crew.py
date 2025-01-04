from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from leetcodesolver.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool


# from ollama.py
from leetcodesolver.ollama import llm

@CrewBase
class LeetcodesolverCrew():
	"""Leetcodesolver crew"""

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[SerperDevTool()],
			verbose=True,
			llm=llm,
			max_iter=1,
		)

	@agent
	def developer(self) -> Agent:
		return Agent(
			config=self.agents_config['developer'],
			verbose=True,
			llm=llm
		)

	@agent
	def animator(self) -> Agent:
		return Agent(
			config=self.agents_config['animator'],
			llm=llm,
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			human_input=True,
			ouput_file='question.md'
		)

	@task
	def developer_task(self) -> Task:
		return Task(
			config=self.tasks_config['developer_task'],
			output_file='solution.md',
		)
	
	@task
	def animator_task(self) -> Task:
		return Task(
			config=self.tasks_config['animator_task'],
			output_file='animation.py',
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Leetcodesolver crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)