from typing import Iterator, List
from pathlib import Path

import pathspec


def get_gitignore_pattern(dir_name: Path) -> List[str]:
    """
    Retrieve the .gitignore patterns from the specified directory.

    Args:
        dir_name (Path): The directory path to search for .gitignore file.

    Returns:
        List[str]: A list of patterns from the .gitignore file.
    """
    path = dir_name / ".gitignore"
    if not path.exists():
        return []
    with open(path, "r") as f:
        content = f.read()
    return content.split("\n")


def walk(dir_name: str) -> Iterator[str]:
    """
    Walk through the directory and return a list of Paths.

    Args:
        dir_name (str): The name of the directory to walk through.

    Returns:
        List[Path]: A list of Paths in the directory.
    """
    root = Path(dir_name)
    gitignore_patterns = get_gitignore_pattern(root)
    gitignore_patterns = [p for p in gitignore_patterns if p != ""]

    # Also add in .git directory and .gitignore files
    gitignore_patterns.append(".git")
    gitignore_patterns.append(".gitignore")

    spec = pathspec.GitIgnoreSpec.from_lines(gitignore_patterns)

    return spec.match_tree(root, negate=True)
