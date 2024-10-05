# src/webkit_vuln_discovery/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CodeAnalysisTool, ExploitDevTool

@CrewBase
class WebkitVulnerabilityDiscoveryCrew():
    """Webkit Vulnerability Discovery Crew"""

    @agent
    def vulnerability_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['vulnerability_researcher'],
            verbose=True,
            tools=[CodeAnalysisTool()]  # Tools specialized for analyzing WebKit code.
        )

    @agent
    def exploit_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['exploit_developer'],
            verbose=True,
            tools=[ExploitDevTool()]  # Tools for developing PoC exploits.
        )

    @agent
    def red_team_operator(self) -> Agent:
        return Agent(
            config=self.agents_config['red_team_operator'],
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    @task
    def webkit_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['webkit_research_task'],
        )

    @task
    def exploit_development_task(self) -> Task:
        return Task(
            config=self.tasks_config['exploit_development_task'],
            output_file='exploit_poc.txt'
        )

    @task
    def red_team_simulation_task(self) -> Task:
        return Task(
            config=self.tasks_config['red_team_simulation_task'],
            output_file='simulation_report.md'
        )

    @task
    def vulnerability_reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['vulnerability_reporting_task'],
            output_file='final_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Webkit Vulnerability Discovery crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,  # The tasks will be executed in sequence
            verbose=True,
        )
