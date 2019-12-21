from handlers.pkg_handler import PKGHandler
from handlers.zip_handler import ZIPHandler

HANDLERS_BY_EXTENSION = {
    PKGHandler.EXTENSION: PKGHandler,
    ZIPHandler.EXTENSION: ZIPHandler
}
