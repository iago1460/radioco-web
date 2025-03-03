import re
from django.conf import settings

class HTMLMinifyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Compile regex patterns once for better performance
        self.comment_pattern = re.compile(r'<!--(?!\[if).*?-->', re.DOTALL)
        self.whitespace_patterns = [
            (re.compile(r'>\s+<'), '><'),  # Between tags
            (re.compile(r'^\s+|\s+$', re.MULTILINE), ''),  # Line starts/ends
            (re.compile(r'\s+/>'), '/>'),  # Self-closing tags
            (re.compile(r'\n'), ' '),  # Replace newlines with space
            (re.compile(r'\t'), ' '),  # Replace tabs with space
            (re.compile(r'\s{2,}'), ' '),  # Multiple spaces
        ]
        # Preserve space in these tags
        self.preserve_space_tags = {'pre', 'textarea', 'script', 'style'}

    def should_minify(self, response):
        return (
            response.get('Content-Type', '').startswith('text/html') and
            not settings.DEBUG and
            not response.get('Content-Encoding') and
            200 <= response.status_code < 300
        )

    def minify_html(self, content):
        # Convert bytes to string if needed
        if isinstance(content, bytes):
            content = content.decode('utf-8')

        # Store preserved content
        preserved = {}
        for tag in self.preserve_space_tags:
            pattern = re.compile(f'<{tag}[^>]*>.*?</{tag}>', re.DOTALL | re.IGNORECASE)
            for i, match in enumerate(pattern.finditer(content)):
                key = f'___PRESERVE_{tag}_{i}___'
                preserved[key] = match.group(0)
                content = content.replace(match.group(0), key)

        # Remove comments (except conditional comments for IE)
        content = self.comment_pattern.sub('', content)

        # Apply all whitespace patterns
        for pattern, replacement in self.whitespace_patterns:
            content = pattern.sub(replacement, content)

        # Restore preserved content
        for key, value in preserved.items():
            content = content.replace(key, value)

        return content

    def __call__(self, request):
        response = self.get_response(request)

        if self.should_minify(response):
            # Minify HTML
            response.content = self.minify_html(response.content).encode('utf-8')
            response['Content-Length'] = len(response.content)

        return response