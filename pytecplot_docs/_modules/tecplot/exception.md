::::: {.body role="main"}
# Source code for tecplot.exception

::: highlight
    """
    The class hierarchy for |PyTecplot| exceptions are as follows. Exceptions in
    parentheses are Python built-ins from which the |PyTecplot| exceptions
    derive. One can use either the Python native errors or the more specific
    "Tecplot" errors to catch exceptions:

    .. code-block:: none

        TecplotError (Exception)
         +--- TecplotConnectionError
         |     `--- TecplotTimeoutError
         +--- TecplotInitializationError (ImportError)
         |     +--- TecplotLicenseError
         |     +--- TecplotLibraryNotLoadedError
         |     `--- TecplotLibraryNotFoundError
         +--- TecplotLogicError (AssertionError)
         +--- TecplotLookupError (LookupError)
         |     +--- TecplotIndexError (IndexError)
         |     `--- TecplotKeyError (KeyError)
         +--- TecplotOSError (OSError)
         +--- TecplotRuntimeError (RuntimeError)
         |     +--- TecplotNotImplementedError (NotImplementedError)
         |     |     `--- TecplotOutOfDateEngineError
         |     `--- TecplotInterfaceChangeError (AttributeError)
         +--- TecplotSystemError (SystemError)
         |     +--- TecplotInterruptError
         |     `--- TecplotMacroError
         +--- TecplotTypeError (TypeError)
         `--- TecplotValueError (ValueError)

        TecplotWarning (Warning)
         +--- TecplotConversionWarning
         +--- TecplotDeprecationWarning (DeprecationWarning)
         +--- TecplotFutureWarning (FutureWarning)
         `--- TecplotPatternMatchWarning (SyntaxWarning)
    """
    import textwrap



    [docs]
    class TecplotError(Exception):
        """Tecplot error."""




    [docs]
    class TecplotConnectionError(TecplotError):
        """Unable to communcate with :ref:`TecUtil Server <TecUtilServer>`."""




    [docs]
    class TecplotTimeoutError(TecplotConnectionError):
        """TecUtil Server not responding in a timely fashion."""




    [docs]
    class TecplotInvalidMessage(TecplotConnectionError):
        """Invalid message received when trying to connect."""




    [docs]
    class TecplotAttributeError(TecplotError, AttributeError):
        """Undefined attribute."""




    [docs]
    class TecplotInitializationError(TecplotError, ImportError):
        """Tecplot engine could not be initialized."""




    [docs]
    class TecplotLibraryNotFoundError(TecplotInitializationError):
        """Batch library was not found in PATH or DY/LD_LIBRARY_PATH."""




    [docs]
    class TecplotLibraryNotLoadedError(TecplotInitializationError):
        """Batch library could not be loaded."""




    [docs]
    class TecplotLicenseError(TecplotInitializationError):
        """Invalid or missing Tecplot license."""




    [docs]
    class TecplotLogicError(TecplotError, AssertionError):
        """TecUtil method contract was violated."""




    [docs]
    class TecplotLookupError(TecplotError, LookupError):
        """Could not find requested object."""




    [docs]
    class TecplotIndexError(TecplotLookupError, IndexError):
        """Index out of range or invalid."""




    [docs]
    class TecplotKeyError(TecplotLookupError, KeyError):
        """Key not found."""




    [docs]
    class TecplotOSError(TecplotError, OSError):
        """Operating system error."""




    [docs]
    class TecplotOverflowError(TecplotError, OverflowError):
        """Integer value out of required range."""




    [docs]
    class TecplotRuntimeError(TecplotError, RuntimeError):
        """PyTecplot post-initialization error."""




    [docs]
    class TecplotNotImplementedError(TecplotRuntimeError, NotImplementedError):
        """Requested operation is planned but not implemented."""




    [docs]
    class TecplotOutOfDateEngineError(TecplotNotImplementedError):
        """Requested action is implemented in a newer version of the engine."""
        def __init__(self, sdk_version_supported, message=None):
            """
            Parameters:
                sdk_version (`tuple` of `integers <int>`): The earliest SDK version
                    that supports the requested action.
                message (`str`): Message to append to the exception.
            """
            from tecplot import version

            n = len(sdk_version_supported)
            if n < 3:
                sdk_version_supported = tuple(list(sdk_version_supported) +
                                              [0] * (3 - n))

            msg = textwrap.dedent('''
                The requested action requires an update to
                your installation of Tecplot 360.
                    Current Tecplot 360 version: {current}
                    Minimum version required: {required}
            '''.format(
                current='{}.{}-{}'.format(*version.sdk_version_info),
                required='{}.{}-{}'.format(*sdk_version_supported)))
            if message:
                msg += '\n' + textwrap.fill(textwrap.dedent(message))
            super().__init__(msg)




    [docs]
    class TecplotInterfaceChangeError(TecplotRuntimeError, AttributeError):
        """A method or property has been moved, renamed or removed."""




    [docs]
    class TecplotSystemError(TecplotError, SystemError):
        """Tecplot Engine error or failure."""
        def __init__(self, message=None):
            from tecplot.tecutil import _tecutil_connector
            msgs = []
            if _tecutil_connector.connected and _tecutil_connector.last_message:
                msgs.append(_tecutil_connector.last_message.message)
            if message:
                msgs.append(message)
            super().__init__('\n'.join(map(str, msgs)))




    [docs]
    class TecplotInterruptError(TecplotSystemError):
        """Tecplot 360 was interrupted."""




    [docs]
    class TecplotMacroError(TecplotSystemError):
        """Macro command failed to execute."""




    [docs]
    class TecplotTypeError(TecplotError, TypeError):
        """Incorrect or invalid type was used."""




    [docs]
    class TecplotValueError(TecplotError, ValueError):
        """Bad value."""




    [docs]
    class TecplotWarning(Warning):
        """General warnings issued from PyTecplot."""




    [docs]
    class TecplotPatternMatchWarning(TecplotWarning, SyntaxWarning):
        """Pattern not found in list of names."""
        def __init__(self, pattern, msg, mode='glob'):
            if mode == 'glob':
                if any(x in pattern for x in '*?[]'):
                    msg += ' For a literal match, the meta-characters: * ? [ ]'
                    msg += ' must be wrapped in square-brackets. For example,'
                    msg += ' "[?]" matches the character "?".'
            super().__init__(msg)




    [docs]
    class TecplotFutureWarning(TecplotWarning, FutureWarning):
        """An interface has moved or been renamed."""




    [docs]
    class TecplotConversionWarning(TecplotWarning):
        """Implicit data conversion which loses precision."""




    [docs]
    class TecplotDeprecationWarning(TecplotWarning, DeprecationWarning):
        """Removed feature."""



    class MESSAGES:
        PERFORMANCE_IMPROVEMENTS = '''\
    The performance of this PyTecplot method has been significantly improved in
    later versions of Tecplot 360. Please update your installation of Tecplot 360
    to the newest version for faster and more reliable script execution.
    '''
:::

::: clearer
:::
:::::
