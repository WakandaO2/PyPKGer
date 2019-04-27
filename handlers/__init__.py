import pkg_handler
import zip_handler

HANDLERS_BY_EXTENSION = {
    pkg_handler.PKGHandler.EXTENSION: pkg_handler.PKGHandler,
    zip_handler.ZIPHandler.EXTENSION: zip_handler.ZIPHandler
}
