:::::::: {.body role="main"}
:::::: {#exceptions .section}
# Exceptions[¶](#exceptions "Link to this heading"){.headerlink}

::::: {#module-tecplot.exception .section}
[]{#tecplot-exception}

## tecplot.exception[¶](#module-tecplot.exception "Link to this heading"){.headerlink}

The class hierarchy for PyTecplot exceptions are as follows. Exceptions
in parentheses are Python built-ins from which the PyTecplot exceptions
derive. One can use either the Python native errors or the more specific
"Tecplot" errors to catch exceptions:

:::: {.highlight-none .notranslate}
::: highlight
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
:::
::::

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotAttributeError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotAttributeError){.reference .internal}[¶](#tecplot.exception.TecplotAttributeError "Link to this definition"){.headerlink}

:   Undefined attribute.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotConnectionError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotConnectionError){.reference .internal}[¶](#tecplot.exception.TecplotConnectionError "Link to this definition"){.headerlink}

:   Unable to communcate with [[TecUtil Server]{.std
    .std-ref}](../install.html#tecutilserver){.reference .internal}.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotConversionWarning]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotConversionWarning){.reference .internal}[¶](#tecplot.exception.TecplotConversionWarning "Link to this definition"){.headerlink}

:   Implicit data conversion which loses precision.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotDeprecationWarning]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotDeprecationWarning){.reference .internal}[¶](#tecplot.exception.TecplotDeprecationWarning "Link to this definition"){.headerlink}

:   Removed feature.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotError){.reference .internal}[¶](#tecplot.exception.TecplotError "Link to this definition"){.headerlink}

:   Tecplot error.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotFutureWarning]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotFutureWarning){.reference .internal}[¶](#tecplot.exception.TecplotFutureWarning "Link to this definition"){.headerlink}

:   An interface has moved or been renamed.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotIndexError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotIndexError){.reference .internal}[¶](#tecplot.exception.TecplotIndexError "Link to this definition"){.headerlink}

:   Index out of range or invalid.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotInitializationError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotInitializationError){.reference .internal}[¶](#tecplot.exception.TecplotInitializationError "Link to this definition"){.headerlink}

:   Tecplot engine could not be initialized.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotInterfaceChangeError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotInterfaceChangeError){.reference .internal}[¶](#tecplot.exception.TecplotInterfaceChangeError "Link to this definition"){.headerlink}

:   A method or property has been moved, renamed or removed.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotInterruptError]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[message]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotInterruptError){.reference .internal}[¶](#tecplot.exception.TecplotInterruptError "Link to this definition"){.headerlink}

:   Tecplot 360 was interrupted.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotInvalidMessage]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotInvalidMessage){.reference .internal}[¶](#tecplot.exception.TecplotInvalidMessage "Link to this definition"){.headerlink}

:   Invalid message received when trying to connect.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotKeyError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotKeyError){.reference .internal}[¶](#tecplot.exception.TecplotKeyError "Link to this definition"){.headerlink}

:   Key not found.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotLibraryNotFoundError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotLibraryNotFoundError){.reference .internal}[¶](#tecplot.exception.TecplotLibraryNotFoundError "Link to this definition"){.headerlink}

:   Batch library was not found in PATH or DY/LD_LIBRARY_PATH.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotLibraryNotLoadedError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotLibraryNotLoadedError){.reference .internal}[¶](#tecplot.exception.TecplotLibraryNotLoadedError "Link to this definition"){.headerlink}

:   Batch library could not be loaded.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotLicenseError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotLicenseError){.reference .internal}[¶](#tecplot.exception.TecplotLicenseError "Link to this definition"){.headerlink}

:   Invalid or missing Tecplot license.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotLogicError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotLogicError){.reference .internal}[¶](#tecplot.exception.TecplotLogicError "Link to this definition"){.headerlink}

:   TecUtil method contract was violated.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotLookupError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotLookupError){.reference .internal}[¶](#tecplot.exception.TecplotLookupError "Link to this definition"){.headerlink}

:   Could not find requested object.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotMacroError]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[message]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotMacroError){.reference .internal}[¶](#tecplot.exception.TecplotMacroError "Link to this definition"){.headerlink}

:   Macro command failed to execute.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotNotImplementedError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotNotImplementedError){.reference .internal}[¶](#tecplot.exception.TecplotNotImplementedError "Link to this definition"){.headerlink}

:   Requested operation is planned but not implemented.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotOSError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotOSError){.reference .internal}[¶](#tecplot.exception.TecplotOSError "Link to this definition"){.headerlink}

:   Operating system error.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotOutOfDateEngineError]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[sdk_version_supported]{.pre}]{.n}*, *[[message]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotOutOfDateEngineError){.reference .internal}[¶](#tecplot.exception.TecplotOutOfDateEngineError "Link to this definition"){.headerlink}

:   Requested action is implemented in a newer version of the engine.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotOverflowError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotOverflowError){.reference .internal}[¶](#tecplot.exception.TecplotOverflowError "Link to this definition"){.headerlink}

:   Integer value out of required range.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotPatternMatchWarning]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}*, *[[msg]{.pre}]{.n}*, *[[mode]{.pre}]{.n}[[=]{.pre}]{.o}[[\'glob\']{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotPatternMatchWarning){.reference .internal}[¶](#tecplot.exception.TecplotPatternMatchWarning "Link to this definition"){.headerlink}

:   Pattern not found in list of names.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotRuntimeError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotRuntimeError){.reference .internal}[¶](#tecplot.exception.TecplotRuntimeError "Link to this definition"){.headerlink}

:   PyTecplot post-initialization error.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotSystemError]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[message]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotSystemError){.reference .internal}[¶](#tecplot.exception.TecplotSystemError "Link to this definition"){.headerlink}

:   Tecplot Engine error or failure.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotTimeoutError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotTimeoutError){.reference .internal}[¶](#tecplot.exception.TecplotTimeoutError "Link to this definition"){.headerlink}

:   TecUtil Server not responding in a timely fashion.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotTypeError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotTypeError){.reference .internal}[¶](#tecplot.exception.TecplotTypeError "Link to this definition"){.headerlink}

:   Incorrect or invalid type was used.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotValueError]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotValueError){.reference .internal}[¶](#tecplot.exception.TecplotValueError "Link to this definition"){.headerlink}

:   Bad value.

<!-- -->

*[exception]{.pre}[ ]{.w}*[[tecplot.exception.]{.pre}]{.sig-prename .descclassname}[[TecplotWarning]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/exception.html#TecplotWarning){.reference .internal}[¶](#tecplot.exception.TecplotWarning "Link to this definition"){.headerlink}

:   General warnings issued from PyTecplot.
:::::
::::::

::: clearer
:::
::::::::
