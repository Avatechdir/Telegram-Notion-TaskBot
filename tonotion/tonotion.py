from notion.client import NotionClient

token = ''
# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2=token)

# Replace this URL with the URL of the page you want to edit
page = client.get_block("https://www.notion.so/2530a62bf25246f384b6b02af0244df9?v=41c23b27a0db481d98a9db92e6407791")

print("The old title is:", page.title)

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
page.title = "The title has now changed, and has *live-updated* in the browser!"
