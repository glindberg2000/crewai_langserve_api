
# CrewAI Integration with LangServe API
# Greg Lindberg
# greglindbereg@gmail.com

This documentation provides a guide on integrating CrewAI with LangServe, offering a streamlined approach to access CrewAI's AI capabilities through the LangServe API.

## Prerequisites

- LangChain CLI installed and updated.
- CrewAI installed as a project dependency.

## Installation

### CrewAI Installation

To incorporate CrewAI into your project, execute the following command:

```bash
pip install git+https://github.com/joaomdmoura/crewai.git
```

This installs CrewAI directly from the GitHub repository, ensuring access to the latest features.

## Configuration and Usage

### Setting Up CrewAI with LangServe

Configure your LangServe application to use CrewAI by updating the necessary project settings. This setup enables the routing of requests to CrewAI through the LangServe API:

https://mirror-feeling-d80.notion.site/Deploy-custom-LangChain-code-with-Hosted-LangServe-e87ef6e363c2441ba877ceb9facd5b31


### Sample Application

The sample application provided creates an endpoint for the CrewAI example app. By accepting a topic, the application leverages CrewAI's researcher and writer capabilities to produce a comprehensive blog post.

#### Endpoint Creation

1. Define an endpoint in your LangServe configuration to handle requests.
2. Ensure the endpoint accepts a `topic` parameter.
3. Configure the endpoint to use CrewAI's researcher and writer to generate a blog post based on the provided topic.

### Example Usage

```python
# Example code snippet for endpoint configuration and blog post generation from commandline. Push this to a repo then import it from smith.langchain.com to create hosted endpoint and montiro with langsmith. 

# Start up the langchain service

poetry run langchain serve

# access the local langchain endpoint and the CrewAI API:

curl -X POST http://localhost:8000/invoke -H "Content-Type: application/json" -d '{"input":"coinbase"}'

```

---

For more detailed information on configuration and advanced usage, refer to the CrewAI documentation and LangChain's guide on integrating custom services.
