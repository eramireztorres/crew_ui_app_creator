import re

class PythonCodeExtractor:
    PYTHON_BLOCK_PATTERN = re.compile(
        r"```python[ \t]*\n(.*?)```", re.DOTALL | re.MULTILINE
    )
    def extract_code(self, content: str) -> str:
        matches = self.PYTHON_BLOCK_PATTERN.findall(content)
        return "\n\n".join(code.strip() for code in matches if code.strip())
    def has_valid_python_block(self, content: str) -> bool:
        return bool(self.PYTHON_BLOCK_PATTERN.search(content))
