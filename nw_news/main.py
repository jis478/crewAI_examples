import json
import os
import shutil
from textwrap import dedent

from crewai import Agent, Crew, Task
from tasks import TaskPrompts

from tools.search_tools import SearchTools
from tools.template_tools import TemplateTools

# from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

class WebtoonAInewsCrew():
  def __init__(self, topic):
    self.agents_config = json.loads(open("config/agents.json", "r").read())
    self.topic = topic
    self.__create_agents()

  def run(self):
    final_result = self.__summarize_news()
    return final_result

  def __summarize_news(self):
    # print(TaskPrompts.collect().format(topic=self.topic))
    collect_news_task = Task(
      description=TaskPrompts.collect().format(topic=self.topic),
      agent=self.news_collector,
      expected_output="""A detailed list of news articles.""", # https://github.com/crewAIInc/crewAI/issues/973

    )

    # collect_news_task = Task(
    #   description=TaskPrompts.collect().format(topic=self.topic),
    #   agent=self.news_collector
    # )
    analyze_news_task = Task(
      description=TaskPrompts.analyze().format(topic=self.topic),
      agent=self.news_analyzer,
      expected_output="""A summarized news articles.""", # https://github.com/crewAIInc/crewAI/issues/973
    )

    crew = Crew(
      agents=[self.news_collector, self.news_analyzer],
      tasks=[collect_news_task, analyze_news_task],
      verbose=True
    )
    analyzed_news = crew.kickoff()
    return analyzed_news

  def __create_agents(self):
    news_collector_config = self.agents_config["news_collector"]
    news_analyzer_config = self.agents_config["news_analyzer"]


    self.news_collector = Agent(
      **news_collector_config,
      verbose=True,
      tools=[
        SearchTools.search_internet,
      ],
    )

    self.news_analyzer = Agent(
      **news_analyzer_config,
      verbose=True,
    )

if __name__ == "__main__":
  print("네이버웹툰 AI 뉴스 분석입니다.")
 
  topic = "네이버웹툰 AI"
  
  crew = WebtoonAInewsCrew(topic)
  result = crew.run()
  print("===================================")
  print(result)
  print("DONE!")
