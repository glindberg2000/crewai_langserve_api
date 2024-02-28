import os
from crewai import Agent, Task, Crew
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.output_parsers import StrOutputParser
from langchain_core.language_models.llms import LLM

# from pydantic_settings import BaseSettings
from typing import Any, List, Optional, Mapping


# class Settings(BaseSettings):
#     OPENAI_API_KEY: str  # This matches the environment variable name


class CrewAIWrapper:
    def __init__(self, api_key: str):
        os.environ["OPENAI_API_KEY"] = api_key
        self.search_tool = DuckDuckGoSearchRun()
        self.researcher = Agent(
            role="Senior Research Analyst",
            goal="Uncover cutting-edge developments in tech topic",
            backstory="You work at a leading tech think tank...",
            verbose=True,
            allow_delegation=False,
            tools=[self.search_tool],
        )
        self.writer = Agent(
            role="Tech Content Strategist",
            goal="Craft compelling content on the latest advancements on any tech topic",
            backstory="You are a renowned Content Strategist...",
            verbose=True,
            allow_delegation=True,
        )

    def kickoff_crew(self, input_description: str):
        # Hardcoded additional information
        blog_description = "Write a blog post using the results from the researcher."

        # Use `input_description` as the analysis description
        analysis_description = input_description

        task1 = Task(description=analysis_description, agent=self.researcher)
        task2 = Task(description=blog_description, agent=self.writer)

        crew = Crew(
            agents=[self.researcher, self.writer],
            tasks=[task1, task2],
            verbose=2,
        )

        result = crew.kickoff()
        return result


class CustomCrewAILLM(LLM):
    def __init__(self, api_key: str):
        super().__init__()
        # Initialize CrewAIWrapper here if necessary or pass api_key directly to _call

    @property
    def _llm_type(self) -> str:
        return "custom_crew_ai"

    def _call(self, prompt: str, *args, **kwargs) -> str:
        # Directly instantiate and use CrewAIWrapper inside the call method
        crew_ai_wrapper = CrewAIWrapper(api_key=api_key)  # Use the api_key directly
        result = crew_ai_wrapper.kickoff_crew(prompt)
        return result


# if __name__ == "__main__":
# settings = Settings()  # Load settings with OPENAI_API_KEY
# api_key = settings.OPENAI_API_KEY


# Load OPENAI_API_KEY from environment variables
api_key = os.getenv("OPENAI_API_KEY")


# Initialize the custom LLM with the API key
custom_llm = CustomCrewAILLM(api_key=api_key)

# Define an output parser
output_parser = StrOutputParser()

# Setup the chain with the custom LLM and output parser
chain = custom_llm | output_parser

# Define a test input prompt
# input_prompt = "Provide an overview of the latest AI advancements."

# # Invoke the chain with the input prompt and print the result
# result = chain.invoke(input_prompt)
# print(result)
