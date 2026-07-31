from rag_llm import generate_response

query = "Internet is not working"

context = """
Broadband Service Issue:
Internet may fail due to:
- Router failure
- Fiber cable damage
- Service outage

Recommended Action:
Restart router and contact support.
"""

response = generate_response(
    query,
    context
)

print(response)