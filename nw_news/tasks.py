from textwrap import dedent


class TaskPrompts():
  def collect():
    return dedent("""
      {topic} 에 대한 뉴스를 검색 및 추출해주세요. 반드시 논문에 {topic} 내용이 있는 경우만 가져오세요. 광고나 다른 영역에 {topic}이 있는 경우는 무시하세요.
    """)

  def analyze():
    return dedent("""
      주어진 news articles 을 bullet point를 이용해서 요약해주세요. 반드시 {topic} 과 관련된 news만 선택해서 요약해주세요. 각 news 마다 날짜와 출처를 포함해주세요. 친절하고 자세히 요약해주세요. 한국어 독자를 대상으로 하므로 한국어로 생성해주세요."
    """)

