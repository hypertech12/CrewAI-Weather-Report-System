import warnings
warnings.filterwarnings("ignore")
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
import warnings

# Define your weather agent
class WeatherDataCollector:
    def __init__(self, model="llama3"):
        self.llm = OllamaLLM(model=model)

    def run(self, query):
        print("[Weather Data Collector] Processing:", query)
        prompt = PromptTemplate(
            input_variables=["query"],
            template="Provide a weather forecast based on this input: {query}"
        )
        final_prompt = prompt.format(query=query)
        response = self.llm.invoke(final_prompt)
        return response

# Main controller
def main():
    print("Welcome to the CrewAI Weather Report System!")
    query = input("Enter your weather query (e.g., 'New York weather this weekend'): ")

    print("\n[System] Collecting weather data...")
    collector = WeatherDataCollector()
    data_result = collector.run(query)

    print("\n[System] Forecast Summary:")
    print(data_result)

if __name__ == "__main__":
    main()
