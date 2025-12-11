import glob
from typing import Optional

def get_latest_file(pattern: str) -> Optional[str]:

    files = glob.glob(pattern)

    if not files:
        return None

    files.sort(reverse=True)
    return files[0]
