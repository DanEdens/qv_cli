"""
    Geo-Instruments
    Sitecheck Scanner
"""
import asyncio
import os

from sitecheck import Scanner
from sitecheck.Scanner.scanner import config


async def main():
    
    await Scanner.Scan()

 
if __name__ == "__main__":
    """Prevents main from running automatically when imported"""
    
    if os.environ['Edit'] == 'True': Scanner.edit()
    if os.environ['Update'] == 'True': config.pubFullConfig()
    if os.environ['Repl'] == 'True': Scanner.repl()
    else:
        asyncio.run(
            main()
            )
