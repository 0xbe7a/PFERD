"""
Synchronizing files from ILIAS instances (https://www.ilias.de/).
"""

from .authenticators import IliasAuthenticator, KitShibbolethAuthenticator
from .crawler import IliasCrawler, IliasDirectoryFilter, IliasDirectoryType
from .downloader import (IliasDownloader, IliasDownloadInfo,
                         IliasDownloadStrategy, download_everything,
                         download_modified_or_new)
