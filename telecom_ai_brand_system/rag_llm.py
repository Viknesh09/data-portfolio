def generate_response(query, context):

    query_lower = query.lower()

    if "internet" in query_lower or "broadband" in query_lower:

        return """
Issue Summary:
Customer is experiencing internet connectivity issues.

Possible Cause:
Router malfunction, broadband outage, or cable issue.

Recommended Solution:
1. Restart modem/router.
2. Check cable connections.
3. Verify service availability.

Next Action:
Contact ZENDS support if the issue persists.
"""

    elif "bill" in query_lower:

        return """
Issue Summary:
Customer has a billing-related concern.

Possible Cause:
Additional usage charges or add-on services.

Recommended Solution:
1. Review billing statement.
2. Check active plans and add-ons.

Next Action:
Contact billing support for clarification.
"""

    elif "network" in query_lower:

        return """
Issue Summary:
Customer is facing mobile network issues.

Possible Cause:
Weak signal or temporary network outage.

Recommended Solution:
1. Move to an open area.
2. Restart mobile device.

Next Action:
Contact support if coverage remains poor.
"""

    return """
Issue Summary:
Customer reported a service issue.

Recommended Solution:
Please contact customer support for assistance.
"""