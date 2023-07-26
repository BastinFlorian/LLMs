# I. Help Desk from Confluence data
## Retrieval QA on your Confluence database company
!["Streamlit"](../../images/use_cases/confluence_help_desk/help_desk.png)

## How it works ?
The process is the following:
- Loading data from Confluence
  - You can keep the Markdown style using [PR]('https://github.com/langchain-ai/langchain/pull/8246')
  - See the `help_desk.ipynb` where Markdown is kept
  - Otherwise you cannot split text in a smart manner using the [MarkdownHeaderTextSplitter]('https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/markdown_header_metadata')
- Load data withour Markdown conservation (easier while waiting for ou PR approval)
- RecursiveCharacterTextSplitter
- Open AI LLM et embedding
- QARetrievalChain
- Streamlit for visualizing data

## How to use ?
- Check the `config.py` and `env.template` file.
- To collect data from Confluence you will have to:
  - Create your own Conluence space with page informations
  - Create and feed your API key [here]('https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/')
  - Insert in the  `env.template` file:
    -  the space_key: `https://yoursite.atlassian.com/wiki/spaces/<space_key>/pages/`
    -  the space_name: `<space_name>/spaces/<space_key>/pages/`
-  `streamlit run confluence_help_desk.streamlit_app.py`